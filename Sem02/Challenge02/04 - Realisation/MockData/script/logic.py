import pandas as pd
import random
from datetime import datetime, timedelta
from models import Dim_Datum, Dim_Gemeente, Dim_Instroomtype, Feit_Gesprek


def create_dataset(config):
    # Datums
    start = datetime(config['start_jaar'], 1, 1)
    eind = datetime(config['eind_jaar'], 12, 31)
    n_dagen = (eind - start).days + 1
    datums = [start + timedelta(days=i) for i in range(n_dagen)]
    df_datum = pd.DataFrame([Dim_Datum.generate(i, d) for i, d in enumerate(datums, 1)])

    # Gemeenten
    gemeenten = [Dim_Gemeente.generate(i) for i in range(1, len(Dim_Gemeente.GEMEENTEN) + 1)]
    df_gemeente = pd.DataFrame(gemeenten)

    # Instroomtypen
    instroomtypen = [Dim_Instroomtype.generate(i) for i in range(1, len(Dim_Instroomtype.TYPES) + 1)]
    df_instroomtype = pd.DataFrame(instroomtypen)

    # Gewichten voor instroomtype (huisarts meest voorkomend)
    instroomtype_gewichten = [40, 25, 15, 12, 8]

    # Feit Gesprek
    gesprekken = []
    for i in range(1, config['n_gesprek'] + 1):
        datum_id = random.choice(df_datum['datum_id'].tolist())
        gemeente_id = random.choice(df_gemeente['gemeente_id'].tolist())
        instroomtype_id = random.choices(
            df_instroomtype['instroomtype_id'].tolist(),
            weights=instroomtype_gewichten,
            k=1
        )[0]
        gesprekken.append(Feit_Gesprek.generate(i, datum_id, gemeente_id, instroomtype_id))

    df_gesprek = pd.DataFrame(gesprekken)

    return {
        "Dim_Datum": df_datum,
        "Dim_Gemeente": df_gemeente,
        "Dim_Instroomtype": df_instroomtype,
        "Feit_Gesprek": df_gesprek,
    }
