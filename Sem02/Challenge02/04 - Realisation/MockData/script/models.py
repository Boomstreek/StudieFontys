import random
from datetime import datetime


class Dim_Datum:
    @staticmethod
    def generate(id, datum):
        return {
            "datum_id": id,
            "datum": datum.strftime("%Y-%m-%d"),
            "week": datum.isocalendar().week,
            "maand": datum.month,
            "jaar": datum.year,
        }


class Dim_Gemeente:
    GEMEENTEN = [
        ("Boxtel", "Brabant"),
        ("Esch", "Brabant"),
        ("Breda", "Brabant"),
        ("Lennisheuvel", "Brabant"),
        ("Liempde", "Brabant"),
    ]

    @staticmethod
    def generate(id):
        naam, regio = Dim_Gemeente.GEMEENTEN[id - 1]
        return {
            "gemeente_id": id,
            "gemeente_naam": naam,
            "regio": regio,
        }


class Dim_Instroomtype:
    TYPES = [
        "Huisarts verwijzing",
        "Zelfaanmelding",
        "Werkgever doorverwijzing",
        "Zorgverzekeraar initiatief",
        "GGD doorverwijzing",
    ]

    @staticmethod
    def generate(id):
        return {
            "instroomtype_id": id,
            "omschrijving": Dim_Instroomtype.TYPES[id - 1],
        }


class Feit_Gesprek:
    @staticmethod
    def generate(id, datum_id, gemeente_id, instroomtype_id):
        voltooid = random.random() < 0.82  # ~82% afgerond
        match_getoond = voltooid and random.random() < 0.70

        duur_minuten = int(random.triangular(10, 60, 25)) if voltooid else int(random.triangular(2, 20, 8))

        # Leefstijlscores alleen wanneer gesprek voltooid is
        if voltooid:
            def score():
                return round(random.triangular(1.0, 10.0, 6.5), 1)

            s_voeding = score()
            s_beweging = score()
            s_ontspanning = score()
            s_slaap = score()
            s_verbinding = score()
            s_middelen = score()
            leefstijlscore_totaal = round(
                (s_voeding + s_beweging + s_ontspanning + s_slaap + s_verbinding + s_middelen) / 6, 2
            )
        else:
            s_voeding = s_beweging = s_ontspanning = s_slaap = s_verbinding = s_middelen = None
            leefstijlscore_totaal = None

        return {
            "gesprek_id": id,
            "datum_id": datum_id,
            "gemeente_id": gemeente_id,
            "instroomtype_id": instroomtype_id,
            "voltooid": voltooid,
            "match_getoond": match_getoond,
            "duur_minuten": duur_minuten,
            "leefstijlscore_totaal": leefstijlscore_totaal,
            "score_voeding": s_voeding,
            "score_beweging": s_beweging,
            "score_ontspanning": s_ontspanning,
            "score_slaap": s_slaap,
            "score_verbinding": s_verbinding,
            "score_middelen": s_middelen,
        }
