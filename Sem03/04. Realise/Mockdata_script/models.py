import random

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

class Dim_Klantgroep:
    GROEPEN = [
        (1, "Kleinverbruik Stad", 22.50, 560.11, 21),
        (2, "Kleinverbruik Dorp", 21.00, 560.11, 21),
        (3, "MKB / Zakelijk", 45.00, 0.00, 21),
    ]

    @staticmethod
    def generate_all():
        return [
            {
                "klantgroep_id": kid,
                "naam": naam,
                "netbeheerkosten": netbeheer,
                "vermindering_energiebelasting": vermindering,
                "btw_percentage": btw,
            }
            for kid, naam, netbeheer, vermindering, btw in Dim_Klantgroep.GROEPEN
        ]

class Feit_Klantverbruik:
    @staticmethod
    def generate(id, klantgroep_id, commodity_id, contractvorm_id, datum):
        if commodity_id == 1:  # Stroom in kWh
            verbruik = round(random.uniform(5.0, 20.0), 4)
        else:  # Gas in m3
            maand = datum.month
            seizoen_factor = 2.2 if maand in [11, 12, 1, 2, 3] else 0.3
            verbruik = round(random.uniform(1.0, 12.0) * seizoen_factor, 4)

        return {
            "klantverbruik_id": id,
            "klantgroep_id": klantgroep_id,
            "commodity_id": commodity_id,
            "contractvorm_id": contractvorm_id,
            "datum": datum.strftime("%Y-%m-%d"),
            "jaar": datum.year,
            "maand": datum.month,
            "dag": datum.day,
            "dagverbruik": verbruik,
        }

class Feit_Inkoopprijs:
    @staticmethod
    def generate(id, commodity_id, contractvorm_id, datum):
        if commodity_id == 1:
            inkoopprijs = round(random.uniform(0.0800, 0.2500), 4)
        else:
            inkoopprijs = round(random.uniform(0.4000, 1.2000), 4)

        return {
            "inkoopprijs_id": id,
            "commodity_id": commodity_id,
            "contractvorm_id": contractvorm_id,
            "datum": datum.strftime("%Y-%m-%d"),
            "jaar": datum.year,
            "maand": datum.month,
            "inkoopprijs_euro": inkoopprijs,
        }