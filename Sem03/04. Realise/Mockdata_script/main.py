import json
import os
from logic import create_dataset

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config.json')

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

output_dir = os.path.join(SCRIPT_DIR, config['output_dir'])
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Fabriek gestart voor energie-dataset...")
datasets = create_dataset(config)

file_format = config.get('format', 'csv').lower()

for name, df in datasets.items():
    if file_format == 'csv':
        file_path = os.path.join(output_dir, f"{name}.csv")
        df.to_csv(file_path, index=False)
    elif file_format == 'json':
        file_path = os.path.join(output_dir, f"{name}.json")
        df.to_json(file_path, orient='records', indent=4)
    elif file_format in ['xlsx', 'excel']:
        file_path = os.path.join(output_dir, f"{name}.xlsx")
        df.to_excel(file_path, index=False)
    else:
        # Fallback naar CSV als het formaat onbekend is
        file_path = os.path.join(output_dir, f"{name}.csv")
        df.to_csv(file_path, index=False)
    
    print(f"Opgeslagen: {file_path}")

print("Klaar! Alle tabellen en bestanden staan voor je klaar.")