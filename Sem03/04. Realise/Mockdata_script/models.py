import random


class Dim_Commodity:
    COMMODITIES = [
        (1, "Stroom", "kWh"),
        (2, "Gas", "m3"),
    ]

    @staticmethod
    def generate_all():
        return [
            {
                "commodity_id": cid,
                "naam": naam,
                "eenheid": eenheid,
            }
            for cid, naam, eenheid in Dim_Commodity.COMMODITIES
        ]


class Dim_Contractvorm:
    CONTRACTEN = [
        (1, "Vast 1 jaar", 12),
        (2, "Vast 3 jaar", 36),
        (3, "Dynamisch (Maandelijks)", 1),
    ]

    @staticmethod
    def generate_all():
        return [
            {
                "contractvorm_id": cid,
                "naam": naam,
                "looptijd_maanden": looptijd,
            }
            for cid, naam, looptijd in Dim_Contractvorm.CONTRACTEN
        ]


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
    def generate(id, klantgroep_ids, commodity_ids, contractvorm_ids, start_jaar, eind_jaar):
        jaar = random.randint(start_jaar, eind_jaar)
        maand = random.randint(1, 12)
        commodity_id = random.choice(commodity_ids)
        
        # Maandverbruik met decimale precisie (bijv. 4 cijfers achter de komma)
        if commodity_id == 1:  # Stroom in kWh
            maandverbruik = round(random.uniform(150.0, 450.0), 4)
        else:  # Gas in m3
            maandverbruik = round(random.uniform(50.0, 300.0), 4)

        return {
            "klantverbruik_id": id,
            "klantgroep_id": random.choice(klantgroep_ids),
            "commodity_id": commodity_id,
            "contractvorm_id": random.choice(contractvorm_ids),
            "jaar": jaar,
            "maand": maand,
            "maandverbruik": maandverbruik,
        }


class Feit_Inkoopprijs:
    @staticmethod
    def generate(id, commodity_id, contractvorm_id, jaar, maand):
        # Inkoopprijs per eenheid met 4 decimalen achter de komma
        if commodity_id == 1:
            inkoopprijs = round(random.uniform(0.0800, 0.2500), 4)
        else:
            inkoopprijs = round(random.uniform(0.4000, 1.2000), 4)

        return {
            "inkoopprijs_id": id,
            "commodity_id": commodity_id,
            "contractvorm_id": contractvorm_id,
            "jaar": jaar,
            "maand": maand,
            "inkoopprijs_euro": inkoopprijs,
        }