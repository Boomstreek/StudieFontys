# voor de data analyse
import pandas as pd
import sqlite3 as sql
import plotly.express as px

# voor de weergave in het dashboard
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# Lees de data van de Excel sheet in een python dataframe
frame_galgje = pd.read_excel("Galgje.xlsx")

# Maak een database en voeg het dataframe toe als tabel
database = sql.connect(":memory:")
frame_galgje.to_sql("spel", con=database, if_exists="replace")

print("\n1\n")

# Haal het aantal deelnemers per leeftijdsgroep op uit de database
frame_aantal_per_avi = pd.read_sql(
    "SELECT AVI, count(*) AS aantal FROM spel GROUP BY AVI", con=database
)
print(frame_aantal_per_avi)
graph_aantal_per_avi = px.bar(frame_aantal_per_avi, x="AVI", y="aantal")

print("\n2\n")

# Haal het aantal deelnemers per leeftijdsgroep op uit de database
frame_aantal_per_leeftijd = pd.read_sql(
    "SELECT leeftijd, count(*) AS aantal FROM spel GROUP BY leeftijd", con=database
)
print(frame_aantal_per_leeftijd)
graph_aantal_per_leeftijd = px.bar(
    frame_aantal_per_leeftijd,
    x="leeftijd",
    y="aantal",  # , color="AVI"
)

print("\n3\n")

# Laat een dashboard zien met de data
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H3("Aantal leerlingen per AVI leesniveau"),
                            html.P(
                                dcc.Graph(
                                    id="aantal_per_avi", figure=graph_aantal_per_avi
                                ),
                                className="m-5",
                            ),
                        ]
                    )
                )
            ],
            class_name="mt-5",
        ),
        dbc.Row(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H3("Aantal leerlingen per leeftijd"),
                            html.P(
                                dcc.Graph(
                                    id="aantal_per_leeftijd",
                                    figure=graph_aantal_per_leeftijd,
                                ),
                                className="m-5",
                            ),
                        ]
                    )
                )
            ],
            class_name="mt-5",
        ),
    ]
)

if __name__ == "__main__":
    app.run()
