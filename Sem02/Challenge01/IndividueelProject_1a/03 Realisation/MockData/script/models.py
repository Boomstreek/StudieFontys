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
    def _get_random_herplanningen():
        """Hulpfunctie voor de parabolische verdeling van herplanningen."""
        waarden = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        gewichten = [20, 30, 40, 25, 15, 10, 5, 3, 2, 1]
        return random.choices(waarden, weights=gewichten, k=1)[0]

    @staticmethod
    def generate(id, patientId):
        return {
            "operatieId": id,
            "patientId": random.choice(patientId),
            "typeOperatie": random.choice(['Knie', 'Heup', 'Hart', 'Oog', 'Steralisatie', 'Hersenen', 'Nieren']),
            "status": random.choice(['Gepland', 'Voltooid']),
            "deadline": (datetime.now() + timedelta(days=random.randint(30, 365))).date().isoformat(),
            "statusScreening": random.choice([True, False]),
            "annuleringsDatum": None,
            "annuleringsReden": None,
            "aantalHerplanningen": Operatie._get_random_herplanningen()
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
    def generate (id, medewerkerId, patientId):
        if random.choice(['medewerker' , 'patient']) == 'medewerker':
            medewerkerId = random.choice(medewerkerId)
            patientId = None
        else:
            medewerkerId = None
            patientId = random.choice(patientId)

        return {
            "tevredenheidId": id,
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

class Operatie_Kamer:
    @staticmethod
    def generate (id):
        
        return {
            "operatieKamerId": id,
            "naam": fake.first_name()
        }

class OkRooster:
    @staticmethod
    def _generate_times():
        """Genereert realistische tijden voor operaties."""
        start_date = datetime.now() + timedelta(days=random.randint(1, 30))
        
        start_uur = random.randint(7, 17)
        start_minuut = random.choice([0, 15, 30, 45])
        
        geplande_start = start_date.replace(
            hour=start_uur,
            minute=start_minuut,
            second=0,
            microsecond=0
        )
        
        duur = timedelta(hours=random.randint(1, 4))
        geplande_eind = geplande_start + duur
        
        afwijking = timedelta(minutes=random.randint(-30, 60))
        werkelijke_start = geplande_start + timedelta(minutes=random.randint(-15, 15))
        werkelijke_eind = geplande_eind + afwijking
        
        return geplande_start, geplande_eind, werkelijke_start, werkelijke_eind
    
    @staticmethod
    def generate(id, operatieKamerId):
        g_start, g_eind, w_start, w_eind = OkRooster._generate_times()

        return {
            "okRoosterId": id,
            "operatieKamerId": random.choice(operatieKamerId),
            "geplandeStartTijd": g_start.isoformat(),
            "geplandeEindTijd": g_eind.isoformat(),
            "werkelijkeStartTijd": w_start.isoformat(),
            "werkelijkeEindTijd": w_eind.isoformat(),
        }
    
class Koppel_Uitvoering:
    @staticmethod
    def generate (operatieId, medewerkerId, okRoosterId):
        

        return {
            "operatieId": operatieId,
            "medewerkerId": random.choice(medewerkerId),
            "okRoosterId": random.choice(okRoosterId),
            "gespreksduurTotaalMinuten": random.randint(2,10),
            "aantalTelefonischeDatumVoorstellen": random.randint(1, 5),
            "retourStroom48u": random.choice([True, False, False]),
            "aantalMinutenBezigMetPlanning": random.randint(10, 120),
            "aantalBelpogingen": random.randint(1, 4),
            "opmerking": fake.sentence() if random.random() < 0.5 else None
        }
    
class Afdeling:
    mogelijkeAfdelingen = ['Cardiologie', 'Neurologie', 'Orthopedie', 'Oogheelkunde', 'Urologie', 'Gynaecologie']

    @staticmethod
    def generate(id):
        return {
            "afdelingId": id,
            "afdelingsnaam": Afdeling.mogelijkeAfdelingen[id - 1],
            "aantalKamers": random.randint(5, 20)
        }

class Kamer:
    @staticmethod
    def generate(id, afdelingId):
        return {
            "kamerId": id,
            "afdelingId": random.choice(afdelingId),
            "aantalBedden": random.randint(1, 4),
            "kamerNummer": id
        }

class Opnamen:
    @staticmethod
    def generate(id, patientId, kamerId):
        startDatum = datetime.now() - timedelta(days=random.randint(0, 365))
        eindDatum = startDatum + timedelta(days=random.randint(1, 14))

        return {
            "opnamenId": id,
            "patientId": random.choice(patientId),
            "kamerId": random.choice(kamerId),
            "startDatum": startDatum.date().isoformat(),
            "eindDatum": eindDatum.date().isoformat()
        }