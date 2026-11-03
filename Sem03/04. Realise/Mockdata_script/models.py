import math
import random
import secrets
import string


class Dim_Commodity:
    COMMODITIES = [(1, "Stroom", "kWh"), (2, "Gas", "m3")]

    @staticmethod
    def generate_all():
        return [{"commodity_id": cid, "naam": naam, "eenheid": eenheid} for cid, naam, eenheid in Dim_Commodity.COMMODITIES]


class Dim_Contractvorm:
    CONTRACTEN = [(1, "Vast 1 jaar", 12), (2, "Vast 3 jaar", 36), (3, "Dynamisch (Maandelijks)", 1)]

    @staticmethod
    def generate_all():
        return [{"contractvorm_id": cid, "naam": naam, "looptijd_maanden": looptijd} for cid, naam, looptijd in Dim_Contractvorm.CONTRACTEN]


class Klantprofiel:
    """
    Interne profielen om realistische klanten te genereren.
    Komt NIET als eigen tabel in de output (staat niet in de ERD);
    de waarden worden per klant in Dim_Klant vastgelegd.
    (profiel_id, naam, netbeheerkosten, vermindering_energiebelasting, btw_percentage,
     stroom kWh/maand (min, max), gas m3/maand winter (min, max), gas m3/maand zomer (min, max))
    """
    PROFIELEN = [
        (1, "Kleinverbruik Stad", 23, 560, 21, (180, 320), (120, 220), (15, 40)),
        (2, "Kleinverbruik Dorp", 21, 560, 21, (200, 360), (150, 260), (20, 50)),
        (3, "MKB / Zakelijk",     45,   0, 21, (800, 2500), (300, 900), (60, 200)),
    ]

    @staticmethod
    def generate_all():
        return [
            {
                "profiel_id": pid,
                "naam": naam,
                "netbeheerkosten": netbeheer,
                "vermindering_energiebelasting": vermindering,
                "btw_percentage": btw,
                "stroom_range": stroom,
                "gas_winter_range": gas_winter,
                "gas_zomer_range": gas_zomer,
            }
            for pid, naam, netbeheer, vermindering, btw, stroom, gas_winter, gas_zomer in Klantprofiel.PROFIELEN
        ]

    @staticmethod
    def get(profiel_id):
        return next(p for p in Klantprofiel.generate_all() if p["profiel_id"] == profiel_id)


class Dim_Klant:
    VOORNAMEN = ["Jan", "Sanne", "Pieter", "Lotte", "Daan", "Emma", "Bram", "Fleur", "Thijs", "Anouk",
                 "Ruben", "Iris", "Lars", "Noor", "Sem", "Julia", "Milan", "Eva", "Jesse", "Sophie"]
    ACHTERNAMEN = ["de Vries", "Jansen", "van den Berg", "Bakker", "Visser", "Smit", "Meijer", "de Boer",
                   "Mulder", "de Groot", "Bos", "Vos", "Peters", "Hendriks", "van Dijk", "Dekker"]
    BEDRIJFSTYPES = ["Bakkerij", "Kapsalon", "Garage", "Installatiebedrijf", "Bloemist", "Café", "Drukkerij", "Fysiotherapie"]

    @staticmethod
    def _naam(profiel_id):
        achternaam = random.choice(Dim_Klant.ACHTERNAMEN)
        if profiel_id == 3:
            return f"{random.choice(Dim_Klant.BEDRIJFSTYPES)} {achternaam}"
        return f"{random.choice(Dim_Klant.VOORNAMEN)} {achternaam}"

    @staticmethod
    def _wachtwoord(lengte=12):
        # Mock-wachtwoord; in een echte database zou je alleen een hash opslaan
        tekens = string.ascii_letters + string.digits
        return "".join(secrets.choice(tekens) for _ in range(lengte))

    @staticmethod
    def generate(klant_id, profiel_id):
        p = Klantprofiel.get(profiel_id)
        return {
            "klant_id": klant_id,
            "naam": Dim_Klant._naam(profiel_id),
            "wachtwoord": Dim_Klant._wachtwoord(),
            "netbeheerkosten": int(p["netbeheerkosten"]),
            "vermindering_energiebelasting": int(p["vermindering_energiebelasting"]),
            "btw_percentage": int(p["btw_percentage"]),
        }


def seizoensfactor(maand):
    """Vloeiende seizoenscurve: 1.0 in januari (piek), 0.0 in juli (dal)."""
    return (1 + math.cos(2 * math.pi * (maand - 1) / 12)) / 2


class Feit_Klantverbruik:
    @staticmethod
    def generate(klant_id, profiel_id, commodity_id, contractvorm_id, jaar, maand, klantfactor=1.0):
        """
        klantfactor: vaste factor per klant (bijv. 0.8-1.2), zodat een klant
        structureel wat meer of minder verbruikt dan het profielgemiddelde.
        """
        p = Klantprofiel.get(profiel_id)
        maandverbruik_stroom = None
        maandverbruik_gas = None
        ruis = random.uniform(0.92, 1.08)  # kleine maand-tot-maand variatie

        if commodity_id == 1:  # Stroom in kWh, licht hoger in de winter (verlichting)
            laag, hoog = p["stroom_range"]
            basis = (laag + hoog) / 2
            seizoen = 0.9 + 0.2 * seizoensfactor(maand)  # 0.9 (zomer) tot 1.1 (winter)
            maandverbruik_stroom = round(basis * seizoen * klantfactor * ruis, 2)
        else:  # Gas in m3, vloeiende curve tussen zomer- en winterniveau
            zomer = sum(p["gas_zomer_range"]) / 2
            winter = sum(p["gas_winter_range"]) / 2
            niveau = zomer + (winter - zomer) * seizoensfactor(maand)
            maandverbruik_gas = round(niveau * klantfactor * ruis, 2)

        return {
            "klant_id": klant_id,
            "commodity_id": commodity_id,
            "contractvorm_id": contractvorm_id,
            "jaar": jaar,
            "maand": maand,
            "maandverbruik_gas": maandverbruik_gas,
            "maandverbruik_stroom": maandverbruik_stroom,
        }


class Feit_Inkoopprijs:
    """
    Inkoopprijzen worden afgeleid van één marktprijsreeks per commodity:
    - Dynamisch (maandelijks): volgt de marktprijs van die maand.
    - Vast 1 jaar: prijs wordt elk januari vastgezet (marktprijs + risicopremie)
      en blijft 12 maanden gelijk.
    - Vast 3 jaar: prijs wordt vastgezet aan het begin van elk blok van 36 maanden
      (marktprijs + hogere risicopremie) en blijft die hele periode gelijk.
    """
    # (startprijs, ondergrens, bovengrens, seizoensamplitude, maandelijkse volatiliteit)
    MARKT = {
        1: (0.15, 0.08, 0.25, 0.10, 0.06),  # Stroom €/kWh
        2: (0.75, 0.40, 1.20, 0.25, 0.07),  # Gas €/m3, sterker seizoenseffect
    }
    RISICOPREMIE = {1: 1.05, 2: 1.10, 3: 1.00}  # per contractvorm_id

    @staticmethod
    def marktprijzen(commodity_id, maanden):
        """Random walk met seizoenseffect: winter duurder dan zomer."""
        start, laag, hoog, amplitude, vol = Feit_Inkoopprijs.MARKT[commodity_id]
        # Trend binnen een smallere band houden, zodat trend x seizoen altijd binnen
        # [laag, hoog] valt zonder af te kappen (geen vlakke lijnen op de grens).
        trend_laag = laag / (1 - amplitude)
        trend_hoog = hoog / (1 + amplitude)
        trend = start
        prijzen = {}
        for jaar, maand in maanden:
            trend *= 1 + random.gauss(0, vol)
            # Terugkaatsen op de grens in plaats van afkappen
            if trend < trend_laag:
                trend = trend_laag + (trend_laag - trend)
            elif trend > trend_hoog:
                trend = trend_hoog - (trend - trend_hoog)
            trend = min(max(trend, trend_laag), trend_hoog)
            seizoen = 1 + amplitude * (seizoensfactor(maand) - 0.5) * 2
            prijzen[(jaar, maand)] = trend * seizoen
        return prijzen

    @staticmethod
    def generate_reeks(start_id, commodity_id, contractvormen, maanden):
        """
        contractvormen: lijst van (contractvorm_id, looptijd_maanden)
        maanden: chronologische lijst van (jaar, maand)
        """
        markt = Feit_Inkoopprijs.marktprijzen(commodity_id, maanden)
        rijen = []
        prijs_id = start_id
        for index, (jaar, maand) in enumerate(maanden):
            for cvid, looptijd in contractvormen:
                # Startmaand van het lopende contractblok bepalen
                blok_start = maanden[(index // looptijd) * looptijd]
                prijs = markt[blok_start] * Feit_Inkoopprijs.RISICOPREMIE.get(cvid, 1.0)
                rijen.append({
                    "inkoopprijs_id": prijs_id,
                    "commodity_id": commodity_id,
                    "contractvorm_id": cvid,
                    "inkoopprijs_euro": round(prijs, 4),
                    "jaar": jaar,
                    "maand": maand,
                })
                prijs_id += 1
        return rijen