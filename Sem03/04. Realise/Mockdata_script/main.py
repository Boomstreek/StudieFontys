import json
import os
from logic import create_dataset
from models import Klantprofiel

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config.json')

UITLEG_PROFIELEN = {
    "1": "Kleinverbruik Stad: Huishoudens in stedelijk gebied met hogere netbeheerkosten.",
    "2": "Kleinverbruik Dorp: Huishoudens in dorps/landelijk gebied met net afwijkende netbeheerkosten en iets hoger verbruik.",
    "3": "MKB / Zakelijk: Kleinzakelijke verbruikers met hoog verbruik, hogere netbeheerkosten en geen vermindering energiebelasting."
}

print("==========================================")
print("   ENERGIE MOCKDATA GENERATOR (MAANDELIJKS)")
print("==========================================")

print("\n[Uitleg klantprofielen]")
for uitleg in UITLEG_PROFIELEN.values():
    print(f" - {uitleg}")

print("\nBeschikbare klantprofielen:")
profielen = Klantprofiel.generate_all()
for p in profielen:
    print(f"  [{p['profiel_id']}] {p['naam']}")

alle_ids = [p['profiel_id'] for p in profielen]
keuze = input("\nWelke klantprofielen wil je meenemen? (Geef ID's comma-gescheiden, of druk op Enter voor 'alles'): ").strip()
if not keuze or keuze.lower() == 'alles':
    profiel_ids = alle_ids
else:
    try:
        profiel_ids = [int(x.strip()) for x in keuze.split(',')]
    except ValueError:
        print("Ongeldige invoer. Standaard wordt 'alles' gebruikt.")
        profiel_ids = alle_ids

n_klanten_input = input("Hoeveel klanten per profiel wil je genereren? (bijv. 50 of 200): ").strip()
n_klanten = int(n_klanten_input) if n_klanten_input.isdigit() else 50

start_jaar_input = input("Startjaar (bijv. 2023): ").strip()
eind_jaar_input = input("Eindjaar (bijv. 2025): ").strip()
start_jaar = int(start_jaar_input) if start_jaar_input.isdigit() else 2023
eind_jaar = int(eind_jaar_input) if eind_jaar_input.isdigit() else 2025

config = {
    "_uitleg_klantprofielen": UITLEG_PROFIELEN,
    "output_dir": "data_output",
    "format": "csv",
    "start_jaar": start_jaar,
    "eind_jaar": eind_jaar,
    "klantprofielen": profiel_ids,
    "n_klanten": n_klanten
}

with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

output_dir = os.path.join(SCRIPT_DIR, config['output_dir'])
os.makedirs(output_dir, exist_ok=True)

print("\nFabriek gestart... Bezig met genereren van maandelijkse data...")
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

    print(f"Opgeslagen: {file_path} ({len(df)} rijen)")

print("\nKlaar! Alle maandelijkse data is succesvol gegenereerd in de map:", output_dir)