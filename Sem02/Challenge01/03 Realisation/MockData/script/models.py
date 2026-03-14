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
    def generate(id, patientId):
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
            "annuleringsDatum": None,
            "annuleringsReden": None,
            "aantalHerplanningen":Operatie._get_random_herplanningen()
        }
    
class Functie:
    mogelijkeFuncties = ['Screener' , 'Chirurg', 'OK-planner']

    @staticmethod
    def generate (id):
        return {
            "functieId": id,
            "functieNaam": Functie.mogelijkeFuncties[id - 1]
        }

class Medewerker:
    @staticmethod
    def generate (id, functieId):
        return {
            "medewerkerId": id,
            "functieId": random.choice(functieId),
            "voornaam": fake.first_name(),
            "achternaam": fake.last_name(),
            "email": fake.email(),
            "telefoonnummer": "06" + "".join([str(random.randint(0, 9)) for _ in range(8)])
        }

class Tevredenheid:
    @staticmethod
    def generate (medewerkerId, patientId):
        if random.choice(['medewerker' , 'patient']) == 'medewerker':
            medewerkerId = random.choice(medewerkerId)
            patientId = None
        else:
            medewerkerId = None
            patientId = random.choice(patientId)

        return {
        "medewerkerId": medewerkerId,
        "patientId": patientId,
        "datum": (datetime.now() - timedelta(days=random.randint(0, 365))).date().isoformat(),
        "opmerking": fake.paragraph(nb_sentences=2),
        "tevredenheidsScore": random.randint(1, 10)
        }

class Rooster:
    @staticmethod
    def generate (id, medewerkerId):
        uren = list(range(0, 24))
        gewichten = [
            # hieronder leer ik python chaining. Wat vroeger van de whiskunde docent nooit mocht ;D
            3 if 8 <= uur <= 17 else 1
            for uur in uren
        ]
        startUur = random.choices(population=uren, weights=gewichten, k=1)[0]
        startMinuut = random.choice([0, 15, 30, 45])
        duurDienstUren = random.randint(4,8)

        startTijd = datetime.strptime(f"{startUur}:{startMinuut:02d}", "%H:%M")
        eindTijd = startTijd + timedelta(hours=duurDienstUren)

        return {
            "roosterId": id,
            "medewerkerId": random.choice(medewerkerId),
            "datum": (datetime.now() + timedelta(days=random.randint(0, 365))).date().isoformat(),
            "startTijd": startTijd,
            "eindTijd": eindTijd
        }

class Koppel_Uitvoering:
    @staticmethod
    def generate (operatieId, medewerkerId):

        return {
            "operatieId": operatieId,
            "medewerkerId": random.choice(medewerkerId),
            "gespreksduurTotaalMinuten": random.randint(2,10),
            "aantalTelefonischeDatumVoorstellen": random.randint(1, 5),
            "retourStroom48u": random.choice([True, False, False]),
            "aantalMinutenBezigMetPlanning": random.randint(10, 120),
            "aantalBelpogingen": random.randint(1, 4),
            "opmerking": fake.sentence() if random.random() < 0.5 else None
        }