import pandas as pd
from models import Patient, Operatie, Functie, Medewerker, Tevredenheid

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
    tevredenheden = [Tevredenheid.generate(medewerkerId, patientId) for i in range(config['n_tevredenheid'])]
    df_tevredenheid = pd.DataFrame(tevredenheden)
    df_tevredenheid.insert(0, 'tevredenheidId', range(1, len(df_tevredenheid) + 1))
    df_tevredenheid['medewerkerId'] = df_tevredenheid['medewerkerId'].astype('Int64')
    df_tevredenheid['patientId'] = df_tevredenheid['patientId'].astype('Int64')

    return {"Patient": df_patients, 
            "Operatie": df_operaties,
            "Functie": df_functies,
            "Medewerker": df_medewerkers,
            "Tevredenheid": df_tevredenheid
    }