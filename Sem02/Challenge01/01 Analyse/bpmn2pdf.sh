#!/bin/bash

# 1. Input vragen
ls -a
echo "------------------------------------------------"
echo "Voer de naam van het .bpmn bestand in:"
read -r FILENAME

# 2. Check of bestand bestaat
if [ ! -f "$FILENAME" ]; then
    echo "Fout: Bestand '$FILENAME' niet gevonden."
    exit 1
fi

# 3. Omgevingsvariabele instellen voor Arch Linux
export PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

echo "Bezig met converteren naar PDF..."

# 4. De tool direct lokaal aanroepen
bpmn-to-image "$FILENAME":"${FILENAME%.*}.pdf" --no-sandbox

if [ $? -eq 0 ]; then
    echo "Succes! De PDF staat in je map."
else
    echo "Er ging iets mis met de conversie."
    exit 1
fi
