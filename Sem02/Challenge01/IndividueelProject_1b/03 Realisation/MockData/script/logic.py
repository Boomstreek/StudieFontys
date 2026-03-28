import pandas as pd
import random
from datetime import datetime, timedelta
from models import Dim_Patient, Dim_Medewerker, Dim_Datum, Dim_Belpoging, Feit_Planning

def create_dataset(config):
    # Patiënten
    patient = [Dim_Patient.generate(i) for i in range(1, config['n_patient'] + 1)]
    df_patient = pd.DataFrame(patient)

    # Medewerkers
    medewerker = [Dim_Medewerker.generate(i) for i in range(1, config['n_medewerker'] + 1)]
    df_medewerker = pd.DataFrame(medewerker)

    # Datums
    start = datetime(config['start_jaar'], 1, 1)
    eind = datetime(config['eind_jaar'], 12, 31)
    n_dagen = (eind - start).days + 1
    datums = [start + timedelta(days=i) for i in range(n_dagen)]
    df_datum = pd.DataFrame([Dim_Datum.generate(i, d) for i, d in enumerate(datums, 1)])

    # Belpogingen 
    belpogingen = [Dim_Belpoging.generate(i, p['toestemming_portaal']) 
                   for i, p in enumerate(patient, 1)]
    df_belpoging = pd.DataFrame(belpogingen)

    # Feit Planning
    planning = [
        Feit_Planning.generate(
            id=i,
            patient_id=random.choice(patient)['patient_id'],
            medewerker_id=random.choice(df_medewerker['medewerker_id'].tolist()),
            datum_id=random.choice(df_datum['datum_id'].tolist()),
            duur_belpogingen_seconden=random.choice(belpogingen)['duur_belpogingen_seconden'],
            toestemming_portaal=random.choice(patient)['toestemming_portaal']
    )
    for i in range(1, config['n_planning'] + 1)
]
    df_planning = pd.DataFrame(planning)

    return {
        "Dim_Patient": df_patient,
        "Dim_Medewerker": df_medewerker,
        "Dim_Datum": df_datum,
        "Dim_Belpoging": df_belpoging,
        "Feit_Planning": df_planning
    }