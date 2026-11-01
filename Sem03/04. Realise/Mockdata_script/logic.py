import pandas as pd
import random
from datetime import datetime, timedelta
from models import Dim_Commodity, Dim_Contractvorm, Dim_Klantgroep, Feit_Klantverbruik, Feit_Inkoopprijs

def create_dataset(config):
    start_jaar = config['start_jaar']
    eind_jaar = config['eind_jaar']
    geselecteerde_klantgroepen = config.get('klantgroepen', [])
    n_klanten = config.get('n_klanten', 1)

    df_commodity = pd.DataFrame(Dim_Commodity.generate_all())
    df_contractvorm = pd.DataFrame(Dim_Contractvorm.generate_all())
    df_klantgroep = pd.DataFrame(Dim_Klantgroep.generate_all())

    if geselecteerde_klantgroepen:
        df_klantgroep = df_klantgroep[df_klantgroep['klantgroep_id'].isin(geselecteerde_klantgroepen)]

    commodity_ids = df_commodity['commodity_id'].tolist()
    contractvorm_ids = df_contractvorm['contractvorm_id'].tolist()
    klantgroep_ids = df_klantgroep['klantgroep_id'].tolist()

    start_date = datetime(start_jaar, 1, 1)
    end_date = datetime(eind_jaar, 12, 31)
    delta = timedelta(days=1)
    
    datums = []
    cur = start_date
    while cur <= end_date:
        datums.append(cur)
        cur += delta

    verbruiken = []
    verbruik_id = 1
    for datum in datums:
        for kg_id in klantgroep_ids:
            for cid in commodity_ids:
                for _ in range(n_klanten):
                    cvid = random.choice(contractvorm_ids)
                    verbruiken.append(Feit_Klantverbruik.generate(verbruik_id, kg_id, cid, cvid, datum))
                    verbruik_id += 1

    df_klantverbruik = pd.DataFrame(verbruiken)

    inkoopprijzen = []
    prijs_id = 1
    for datum in datums:
        for cid in commodity_ids:
            for cvid in contractvorm_ids:
                inkoopprijzen.append(Feit_Inkoopprijs.generate(prijs_id, cid, cvid, datum))
                prijs_id += 1

    df_inkoopprijs = pd.DataFrame(inkoopprijzen)

    return {
        "Dim_Commodity": df_commodity,
        "Dim_Contractvorm": df_contractvorm,
        "Dim_Klantgroep": df_klantgroep,
        "Feit_Klantverbruik": df_klantverbruik,
        "Feit_Inkoopprijs": df_inkoopprijs,
    }