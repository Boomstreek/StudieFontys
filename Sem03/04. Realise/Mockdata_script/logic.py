import pandas as pd
import random
from models import Dim_Commodity, Dim_Contractvorm, Klantprofiel, Dim_Klant, Feit_Klantverbruik, Feit_Inkoopprijs


def create_dataset(config):
    start_jaar = config['start_jaar']
    eind_jaar = config['eind_jaar']
    geselecteerde_profielen = config.get('klantprofielen', [])
    n_klanten = config.get('n_klanten', 1)

    df_commodity = pd.DataFrame(Dim_Commodity.generate_all())
    df_contractvorm = pd.DataFrame(Dim_Contractvorm.generate_all())

    commodity_ids = df_commodity['commodity_id'].tolist()
    contractvorm_ids = df_contractvorm['contractvorm_id'].tolist()

    profiel_ids = [p['profiel_id'] for p in Klantprofiel.generate_all()]
    if geselecteerde_profielen:
        profiel_ids = [pid for pid in profiel_ids if pid in geselecteerde_profielen]

    # Maanden in de periode
    maanden = [(jaar, maand) for jaar in range(start_jaar, eind_jaar + 1) for maand in range(1, 13)]

    # KLANT: n_klanten per geselecteerd profiel
    klanten = []
    klant_profiel = {}
    klant_id = 1
    for pid in profiel_ids:
        for _ in range(n_klanten):
            klanten.append(Dim_Klant.generate(klant_id, pid))
            klant_profiel[klant_id] = pid
            klant_id += 1
    df_klant = pd.DataFrame(klanten)

    # KLANTVERBRUIK: per klant per commodity per maand.
    # Een klant houdt per commodity één contractvorm voor de hele periode.
    verbruiken = []
    for kid, pid in klant_profiel.items():
        contract_per_commodity = {cid: random.choice(contractvorm_ids) for cid in commodity_ids}
        for jaar, maand in maanden:
            for cid in commodity_ids:
                verbruiken.append(
                    Feit_Klantverbruik.generate(kid, pid, cid, contract_per_commodity[cid], jaar, maand)
                )
    df_klantverbruik = pd.DataFrame(verbruiken)

    # INKOOPPRIJS: per commodity per contractvorm per maand
    inkoopprijzen = []
    prijs_id = 1
    for jaar, maand in maanden:
        for cid in commodity_ids:
            for cvid in contractvorm_ids:
                inkoopprijzen.append(Feit_Inkoopprijs.generate(prijs_id, cid, cvid, jaar, maand))
                prijs_id += 1
    df_inkoopprijs = pd.DataFrame(inkoopprijzen)

    return {
        "Dim_Commodity": df_commodity,
        "Dim_Contractvorm": df_contractvorm,
        "Dim_Klant": df_klant,
        "Feit_Klantverbruik": df_klantverbruik,
        "Feit_Inkoopprijs": df_inkoopprijs,
    }