from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('nl_NL')

class Patient:
    @staticmethod
    def generate(id, row=None):
        return {
            "patientId": id,
            "voornaam": fake.first_name(),
            "achternaam": fake.last_name(),
            "stad": fake.city(),
            "provincie": fake.province(),
            "postcode": fake.postcode(),
            "straat": fake.street_name(),
            "huisnummer": random.randint(1, 500),
            "gender": random.choice(['Male', 'Female', 'Non-binary']),
            "telefoonnummer": fake.phone_number(),
            "email": fake.email(),
            "toestemmingDigitaalPatientDossier": random.choice([True, False])
        }

class Operatie:
    @staticmethod
    def _generate_times():
        """Genereert realistische tijden voor operaties."""
        # Start op een willekeurige dag in de komende 30 dagen
        start_date = datetime.now() + timedelta(days=random.randint(1, 30), hours=random.randint(8, 16))
        
        # Duur van de operatie tussen 1 en 4 uur
        duur = timedelta(hours=random.randint(1, 4))
        
        geplande_start = start_date
        geplande_eind = start_date + duur
        
        # Werkelijke tijden: soms loopt het uit (tot 60 min) of is het eerder klaar
        afwijking = timedelta(minutes=random.randint(-30, 60))
        werkelijke_start = geplande_start + timedelta(minutes=random.randint(-15, 15))
        werkelijke_eind = geplande_eind + afwijking
        
        return geplande_start, geplande_eind, werkelijke_start, werkelijke_eind
    
    @staticmethod
    def _get_random_herplanningen():
        """Hulpfunctie voor de parabolische verdeling van herplanningen."""
        waarden = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        gewichten = [20, 30, 40, 25, 15, 10, 5, 3, 2, 1]
        return random.choices(waarden, weights=gewichten, k=1)[0]

    @staticmethod
    def generate(patientId):
        g_start, g_eind, w_start, w_eind = Operatie._generate_times()
        return {
            "operatieId": id,
            "patientId": random.choice(patientId),
            "geplandeStartTijd": g_start.isoformat(),
            "geplandeEindTijd": g_eind.isoformat(),
            "werkelijkeStartTijd": w_start.isoformat(),
            "werkelijkeEindTijd": w_eind.isoformat(),
            "typeOperatie": random.choice(['Knie', 'Heup', 'Hart', 'Oog', 'Steralisatie', 'Hersenen', 'Nieren']),
            "status": random.choice(['Gepland', 'Voltooid']),
            "statusScreening": random.choice([True, False]),
            "annuleringsDatum":
            "annuleringsReden":
            "aantalHerplanningen":Operatie._get_random_herplanningen()
        }