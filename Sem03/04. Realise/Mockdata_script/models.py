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


class Feit_Klantverbruik:
    WINTERMAANDEN = [11, 12, 1, 2, 3]

    @staticmethod
    def generate(klant_id, profiel_id, commodity_id, contractvorm_id, jaar, maand):
        p = Klantprofiel.get(profiel_id)
        maandverbruik_stroom = None
        maandverbruik_gas = None

        if commodity_id == 1:  # Stroom in kWh
            maandverbruik_stroom = round(random.uniform(*p["stroom_range"]), 2)
        else:  # Gas in m3, seizoensafhankelijk
            bereik = p["gas_winter_range"] if maand in Feit_Klantverbruik.WINTERMAANDEN else p["gas_zomer_range"]
            maandverbruik_gas = round(random.uniform(*bereik), 2)

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
    @staticmethod
    def generate(id, commodity_id, contractvorm_id, jaar, maand):
        if commodity_id == 1:
            inkoopprijs = round(random.uniform(0.0800, 0.2500), 4)
        else:
            inkoopprijs = round(random.uniform(0.4000, 1.2000), 4)

        return {
            "inkoopprijs_id": id,
            "commodity_id": commodity_id,
            "contractvorm_id": contractvorm_id,
            "inkoopprijs_euro": inkoopprijs,
            "jaar": jaar,
            "maand": maand,
        }