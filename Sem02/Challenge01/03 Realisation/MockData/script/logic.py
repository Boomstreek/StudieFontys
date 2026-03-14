import pandas as pd
from models import Patient, Operatie, Functie, Medewerker, Tevredenheid, Rooster, Operatie_Kamer, OkRooster, Koppel_Uitvoering, Afdeling, Kamer, Opnamen

def get_existing_patient_ids(csv_path):
    """Leest de bestaande CSV en geeft een lijst met ID's terug."""
    try:
        df = pd.read_csv(csv_path)
        return df['patientId'].tolist(), df
    except FileNotFoundError:
        print(f"Waarschuwing: {csv_path} niet gevonden, genereer nieuwe patiënten.")
        return None, None

def create_dataset(config):
    # Genereer Patient of lees in
    # Probeer bestaande patiënten te laden
    csv_path = 'data_output/Patient.csv' 
    existing_ids, df_patients = get_existing_patient_ids(csv_path)

    # Als CSV niet bestaat of leeg is: genereer nieuwe patiënten
    if existing_ids is None:
        patients = [Patient.generate(i) for i in range(1, config['n_patients'] + 1)]
        df_patients = pd.DataFrame(patients)
        patientId = df_patients['patientId'].tolist()
    else:
        patientId = existing_ids
    
    # Genereer Operatie
    operaties = [Operatie.generate(5000 + i, patientId) for i in range(config['n_operaties'])]
    df_operaties = pd.DataFrame(operaties)
    operatieId = df_operaties['operatieId'].tolist()
    
    #  Genereer Functie
    functies = [Functie.generate(i) for i in range (1, len(Functie.mogelijkeFuncties) +1)]
    df_functies = pd.DataFrame(functies)
    functieId = df_functies['functieId'].tolist()

    # Genereer Medewerker
    mederwerkers = [Medewerker.generate(i, functieId) for i in range (1, config['n_medewerkers'] + 1)]
    df_medewerkers = pd.DataFrame(mederwerkers)
    medewerkerId = df_medewerkers['medewerkerId'].tolist()

    # Genereer Tevredenheid
    tevredenheden = [Tevredenheid.generate(i, medewerkerId, patientId) for i in range(config['n_tevredenheid'])]
    df_tevredenheid = pd.DataFrame(tevredenheden)
    df_tevredenheid['medewerkerId'] = df_tevredenheid['medewerkerId'].astype('Int64')
    df_tevredenheid['patientId'] = df_tevredenheid['patientId'].astype('Int64')

    # Genereer Rooster
    rooster = [Rooster.generate(i, medewerkerId) for i in range (1, config['n_medewerkers'] * 5 + 1)]
    df_rooster = pd.DataFrame(rooster)

    # Genereer Operatie_Kamer
    operatie_kamer = [Operatie_Kamer.generate(i) for i in range(1, config['n_operatie_kamers'] + 1)]
    df_operatie_kamer = pd.DataFrame(operatie_kamer)
    operatieKamerId = df_operatie_kamer['operatieKamerId'].tolist()

    # Genereer OkRooster
    ok_rooster = [OkRooster.generate(i, operatieKamerId) for i in range(1, len(operatieId) + 1)]
    df_ok_rooster = pd.DataFrame(ok_rooster)
    okRoosterId = df_ok_rooster['okRoosterId'].tolist()

    # Genereer Koppel_Uitvoering
    koppel_uitvoering = [Koppel_Uitvoering.generate(oid, medewerkerId, okRoosterId) for oid in operatieId]
    df_koppel_uitvoering = pd.DataFrame(koppel_uitvoering)

    # Genereer Afdeling
    afdelingen = [Afdeling.generate(i) for i in range(1, len(Afdeling.mogelijkeAfdelingen) + 1)]
    df_afdelingen = pd.DataFrame(afdelingen)
    afdelingId = df_afdelingen['afdelingId'].tolist()

    # Genereer Kamer
    kamers = [Kamer.generate(i, afdelingId) for i in range(1, config['n_kamers'] + 1)]
    df_kamers = pd.DataFrame(kamers)
    kamerId = df_kamers['kamerId'].tolist()

    # Genereer Opnamen
    opnamen = [Opnamen.generate(i, patientId, kamerId) for i in range(1, config['n_opnamen'] + 1)]
    df_opnamen = pd.DataFrame(opnamen)

    return {"Patient": df_patients, 
            "Operatie": df_operaties,
            "Functie": df_functies,
            "Medewerker": df_medewerkers,
            "Tevredenheid": df_tevredenheid,
            "Rooster": df_rooster,
            "Operatie_Kamer": df_operatie_kamer,
            "OkRooster": df_ok_rooster,
            "Koppel_Uitvoering": df_koppel_uitvoering,
            "Afdeling": df_afdelingen,
            "Kamer": df_kamers,
            "Opnamen": df_opnamen
    }