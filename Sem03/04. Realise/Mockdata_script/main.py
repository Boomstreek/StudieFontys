import json
import os
from logic import create_dataset
from models import Dim_Klantgroep

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config.json')

print("==========================================")
print("   ENERGIE MOCKDATA GENERATOR (DAGELIJKS)  ")
print("==========================================")

print("\n[Uitleg Klantgroepen]")
print(" - Kleinverbruik Stad: Huishoudens in stedelijk gebied met gemiddeld hoger verbruik en hogere netbeheerkosten.")
print(" - Kleinverbruik Dorp: Huishoudens in dorps/landelijk gebied met net afwijkende netbeheerkosten.")
print(" - MKB / Zakelijk: Kleinzakelijke verbruikers met hogere netbeheerkosten en geen vermindering energiebelasting.")

print("\nBeschikbare klantgroepen:")
groepen = Dim_Klantgroep.generate_all()
for g in groepen:
    print(f"  [{g['klantgroep_id']}] {g['naam']}")

keuze_kg = input("\nWelke klantgroepen wil je meenemen? (Geef ID's comma-gescheiden, of druk op Enter voor 'alles'): ").strip()
if not keuze_kg or keuze_kg.lower() == 'alles':
    klantgroepen_ids = [g['klantgroep_id'] for g in groepen]
else:
    try:
        klantgroepen_ids = [int(x.strip()) for x in keuze_kg.split(',')]
    except ValueError:
        print("Ongeldige invoer. Standaard wordt 'alles' gebruikt.")
        klantgroepen_ids = [g['klantgroep_id'] for g in groepen]

n_klanten_input = input("Hoeveel records/klanten per dag per groep wil je genereren? (bijv. 1 of 5): ").strip()
n_klanten = int(n_klanten_input) if n_klanten_input.isdigit() else 1

start_jaar_input = input("Startjaar (bijv. 2023): ").strip()
eind_jaar_input = input("Eindjaar (bijv. 2024): ").strip()
start_jaar = int(start_jaar_input) if start_jaar_input.isdigit() else 2023
eind_jaar = int(eind_jaar_input) if eind_jaar_input.isdigit() else 2024

# Configuratie inclusief uitleg zodat deze bewaard blijft bij wegschrijven
config = {
    "_uitleg_klantgroepen": {
        "1": "Kleinverbruik Stad: Huishoudens in stedelijk gebied met gemiddeld hoger verbruik en hogere netbeheerkosten.",
        "2": "Kleinverbruik Dorp: Huishoudens in dorps/landelijk gebied met net afwijkende netbeheerkosten.",
        "3": "MKB / Zakelijk: Kleinzakelijke verbruikers met hogere netbeheerkosten en geen vermindering energiebelasting."
    },
    "output_dir": "data_output",
    "format": "csv",
    "start_jaar": start_jaar,
    "eind_jaar": eind_jaar,
    "klantgroepen": klantgroepen_ids,
    "n_klanten": n_klanten
}

with open(CONFIG_PATH, 'w') as f:
    json.dump(config, f, indent=4)

output_dir = os.path.join(SCRIPT_DIR, config['output_dir'])
os.makedirs(output_dir, exist_ok=True)

print("\nFabriek gestart... Bezig met genereren van dagelijkse data...")
datasets = create_dataset(config)

file_format = config.get('format', 'csv').lower()

for name, df in datasets.items():
    if file_format == 'json':
        file_path = os.path.join(output_dir, f"{name}.json")
        df.to_json(file_path, orient='records', indent=4)
    elif file_format in ['xlsx', 'excel']:
        file_path = os.path.join(output_dir, f"{name}.xlsx")
        df.to_excel(file_path, index=False)
    else:
        file_path = os.path.join(output_dir, f"{name}.csv")
        df.to_csv(file_path, index=False)
    
    print(f"Opgeslagen: {file_path}")

print("\nKlaar! Alle dagelijkse data is succesvol gegenereerd in de map:", output_dir)