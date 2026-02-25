#!/bin/bash

# Vraag de gebruiker om de bestandsnaam
echo "Voer de naam van het .bpmn bestand in:"
read -r FILENAME

# Controleer of het bestand bestaat
if [ ! -f "$FILENAME" ]; then
    echo "❌ Fout: Bestand '$FILENAME' niet gevonden."
    exit 1
fi

echo "🚀 Bezig met converteren van $FILENAME naar PDF..."

# We draaien nu een image waar Chrome al in zit
docker run --rm \
  -v "$(pwd):/data" \
  -u $(id -u):$(id -g) \
  ghcr.io/puppeteer/puppeteer:latest \
  npx bpmn-to-image "/data/$FILENAME:pdf"

if [ $? -eq 0 ]; then
    echo "✅ Succes! Je PDF is klaar."
else
    echo "❌ De conversie is mislukt. Controleer of de bestandsnaam klopt (let op hoofdletters)."
fi
