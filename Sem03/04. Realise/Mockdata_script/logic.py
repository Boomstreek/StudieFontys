import pandas as pd
from models import Dim_Commodity, Dim_Contractvorm, Dim_Klantgroep, Feit_Klantverbruik, Feit_Inkoopprijs


def create_dataset(config):
    start_jaar = config['start_jaar']
    eind_jaar = config['eind_jaar']

    # Dimensies genereren
    df_commodity = pd.DataFrame(Dim_Commodity.generate_all())
    df_contractvorm = pd.DataFrame(Dim_Contractvorm.generate_all())
    df_klantgroep = pd.DataFrame(Dim_Klantgroep.generate_all())

    commodity_ids = df_commodity['commodity_id'].tolist()
    contractvorm_ids = df_contractvorm['contractvorm_id'].tolist()
    klantgroep_ids = df_klantgroep['klantgroep_id'].tolist()

    # Feit Klantverbruik genereren
    n_verbruik = config.get('n_verbruik_records', 1500)
    verbruiken = [
        Feit_Klantverbruik.generate(i, klantgroep_ids, commodity_ids, contractvorm_ids, start_jaar, eind_jaar)
        for i in range(1, n_verbruik + 1)
    ]
    df_klantverbruik = pd.DataFrame(verbruiken)

    # Feit Inkoopprijs genereren (voor elke combinatie van jaar, maand, commodity en contractvorm)
    inkoopprijzen = []
    prijs_id = 1
    for jaar in range(start_jaar, eind_jaar + 1):
        for maand in range(1, 13):
            for cid in commodity_ids:
                for cvid in contractvorm_ids:
                    inkoopprijzen.append(
                        Feit_Inkoopprijs.generate(prijs_id, cid, cvid, jaar, maand)
                    )
                    prijs_id += 1
    df_inkoopprijs = pd.DataFrame(inkoopprijzen)

    return {
        "Dim_Commodity": df_commodity,
        "Dim_Contractvorm": df_contractvorm,
        "Dim_Klantgroep": df_klantgroep,
        "Feit_Klantverbruik": df_klantverbruik,
        "Feit_Inkoopprijs": df_inkoopprijs,
    }