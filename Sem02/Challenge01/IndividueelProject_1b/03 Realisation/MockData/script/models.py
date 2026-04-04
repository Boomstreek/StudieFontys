from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('nl_NL')

class Dim_Patient:
    @staticmethod
    def generate(id, row=None):
        return {
            "patient_id": id,
            "voornaam": fake.first_name(),
            "achternaam": fake.last_name(),
            "toestemming_portaal": random.choice([True, False])
        }

class Dim_Medewerker:
    @staticmethod
    def generate(id):
        uurtarief = random.randint(30, 50)
        overhead = round(uurtarief * random.uniform(0.45, 0.55))
        return {
            "medewerker_id": id,
            "voornaam": fake.first_name(),
            "achternaam": fake.last_name(),
            "functie": 'OK-Planner',
            "uurtarief": uurtarief,
            "overhead": overhead
        }

class Dim_Tevredenheid:
    @staticmethod
    def generate(id, medewerker_id, patient_id):
        return {
            "tevredenheid_id": id,
            "medewerker_id": medewerker_id,
            "patient_id": patient_id,
            "tevredenheid": random.randint(1, 10)
        }

class Dim_Datum:
    @staticmethod
    def generate(id, datum):
        return {
            "datum_id": id,
            "datum": datum.strftime("%Y-%m-%d"), 
            "dag": datum.day,
            "week": datum.isocalendar().week,
            "maand": datum.month,
            "kwartaal": (datum.month - 1) // 3 + 1,
            "jaar": datum.year
        }

class Dim_Belpoging:
    @staticmethod
    def generate(id, toestemming_portaal):
        if toestemming_portaal:
            return {
                "belpoging_id": id,
                "aantal_belpogingen" : 0,
                "duur_belpogingen_seconden": 0
            }
        
        # Parabolisch afnemende kans op aantal belpogingen
        waarden  = [1,  2,  3,  4,  5,  6,  7, 8, 9, 10]
        gewichten = [50, 25, 12,  6,  3,  2,  1, 1, 1,  1]
        aantal = random.choices(waarden, weights=gewichten, k=1)[0]

        # Duur per belpoging: mediaan tussen 2-4 min, max 15 min
        # Gebruik driehoeksverdeling: min=30s, mode=120s, max=900s
        duur_totaal = sum(
            int(random.triangular(30, 900, 120))
            for _ in range(aantal)
        )

        return {
            "belpoging_id": id,
            "aantal_belpogingen": aantal,
            "duur_belpogingen_seconden": duur_totaal
        }

class Feit_Planning:
    @staticmethod
    def generate(id, patient_id, medewerker_id, tevredenheid_id, datum_id, belpoging_id, duur_belpogingen_seconden, toestemming_portaal):
        # Duur planning: belpogingen + extra gesprekstijd (5-30 min, mediaan 8-12 min)
        extra_seconden = int(random.triangular(300, 1800, 600))  # 5-30 min, mode=10 min
        duur_planning_seconden = duur_belpogingen_seconden + extra_seconden
        duur_planning_seconden = min(duur_planning_seconden, 46400) # Maximale kosten is euro 999 per planning, kreeg op en bepaald moment 2,33k euro aan kosten gem eruit. 

        # Planning start: willekeurig op een werkdag tussen 08:00 en 17:00
        planning_start = datetime(2024, 1, 1) + timedelta(
            days=random.randint(0, 365),
            hours=random.randint(8, 16),
            minutes=random.choice([0, 15, 30, 45])
        )
        planning_eind = planning_start + timedelta(seconds=duur_planning_seconden)

        # Bevestiging
        if not toestemming_portaal:
            # Telefonisch: bevestiging op het moment dat het gesprek klaar is
            datetime_bevestiging = planning_eind
        else:
            # Digitaal: lineair 0-2 dagen, piek net voor 2 dagen (de meesten reageren niet)
            # Driehoeksverdeling: min=0, max=2 dagen, mode=1.9 dagen
            uren_later = random.triangular(0, 48, 45)  # in uren, mode ~45 uur
            datetime_bevestiging = planning_start + timedelta(hours=uren_later)

        return {
            "feit_id": id,
            "patient_id": patient_id,
            "medewerker_id": medewerker_id,
            "tevredenheid_id": tevredenheid_id,
            "datum_id": datum_id,
            "belpoging_id": belpoging_id,
            "duur_planning_seconden": duur_planning_seconden,
            "datetime_planning_start": planning_start.isoformat(),
            "datetime_planning_eind": planning_eind.isoformat(),
            "datetime_bevestiging": datetime_bevestiging.isoformat()
        }