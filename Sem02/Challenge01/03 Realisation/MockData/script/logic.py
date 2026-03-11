import pandas as pd
from models import Patient, Operatie

def get_existing_patient_ids(csv_path):
    """Leest de bestaande CSV en geeft een lijst met ID's terug."""
    try:
        df = pd.read_csv(csv_path)
        return df['patientId'].tolist(), df
    except FileNotFoundError:
        print(f"Waarschuwing: {csv_path} niet gevonden, genereer nieuwe patiënten.")
        return None, None

def create_dataset(config):
    # 1. Probeer bestaande patiënten te laden
    csv_path = 'PATIENT.csv' # Zorg dat dit bestand in dezelfde map staat als main.py
    existing_ids, df_patients = get_existing_patient_ids(csv_path)

    # 2. Als CSV niet bestaat of leeg is: genereer nieuwe patiënten (jouw oude logica)
    if existing_ids is None:
        patients = [Patient.generate(i) for i in range(1, config['n_patients'] + 1)]
        df_patients = pd.DataFrame(patients)
        p_ids = df_patients['patientId'].tolist()
    else:
        p_ids = existing_ids
    
    # 3. Genereer Operaties (nu gebruikmakend van de lijst met p_ids uit stap 1 of 2)
    operaties = [Operatie.generate(5000 + i, p_ids) for i in range(config['n_operaties'])]
    df_operaties = pd.DataFrame(operaties)
    
    return {"PATIENT": df_patients, "OPERATIE": df_operaties}