import json
import os
from logic import create_dataset

# Bepaal paden relatief aan dit script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config.json')

# Laad config
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

# Pad voor output
output_dir = os.path.join(SCRIPT_DIR, config['output_dir'])
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data genereren
print("Fabriek gestart...")
datasets = create_dataset(config)

# Opslaan
for name, df in datasets.items():
    file_path = os.path.join(output_dir, f"{name}.{config['format']}")
    df.to_csv(file_path, index=False)
    print(f"✅ Opgeslagen: {file_path}")

print("Klaar! Je dataset staat klaar.")