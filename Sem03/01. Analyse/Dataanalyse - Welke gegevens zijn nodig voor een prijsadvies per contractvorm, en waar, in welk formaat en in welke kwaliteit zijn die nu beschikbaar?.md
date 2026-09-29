## Algemene gegevens

|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |1.0|
|Datum huidige versie|29-9-2026|
|Referenties|Scope - Fontasya Electric.pdf versie 1.5|

## 1. Inleiding

### 1.1 Aanleiding en context

Fontasya Electric biedt energiecontracten aan huishoudens in vier vormen: flexibel, 1-jarig, 3-jarig en 5-jarig. Voor al deze vormen moet Fontasya periodiek tariefbesluiten vaststellen. Die besluiten zijn afhankelijk van data die verspreid staat over verschillende bronnen. Dit project werkt toe naar een platform met een uitlegbaar prijsmodel en een interactief dashboard, waarmee tariefbesluiten onderbouwd, reproduceerbaar en binnen de kaders van privacy, security en beheer kunnen worden genomen. Dit document vormt de dataonderbouwing: het stelt vast welke data nodig is en in hoeverre de aangeleverde data daaraan voldoet.

### 1.2 Doel en deelvraag

- **Deelvraag:** Welke gegevens zijn nodig voor een prijsadvies per contractvorm, en waar, in welk formaat en in welke kwaliteit zijn die nu beschikbaar?
    
- **Doel:** Een helder normenkader opstellen van de ideale databehoefte per contractvorm, de aangeleverde synthetische datasets daaraan toetsen, en de gaten benoemen zodat het team weet wat nodig is voor de eerste werkende versie van het prijsadviesproces.
    

### 1.3 Afbakening

- **Doelgroep:** Huishoudens
    
- **Contractvormen:** Flexibel, 1-jarig, 3-jarig, 5-jarig
    
- **Data:** Synthetische datasets aangeleverd via een python script
    
- **Energiesoort:** Hoofdzakelijk elektriciteit
    

## 2. De Ideale Databehoefte (De Norm)

De opbouw van een energietarief volgt de volgende formule:

tarief=inkoopkosten+profiel- en volumerisico+krediet- en overige risico’s+netbeheer & belastingen+uitvoeringskosten+marge

Dit vertaalt zich naar vier essentiële datagroepen:

1. **Inkoopprijzen:** Forward-curves (voor 1, 3 en 5 jaar) en day-ahead spotprijzen (voor flexibel).
    
2. **Verbruik & Klanten:** Standaard huishoudensprofielen (uur/kwartier) en de klantportefeuille (volumes en contractvormen).
    
3. **Kosten & Regels:** Netbeheerkosten, energiebelasting, vastrecht en interne uitvoeringskosten.
    
4. **Parameters & Logboek:** Doelmarges, risico-opslagen per looptijd, en een logboek om elke prijsberekening (prijsrun) te kunnen reproduceren.
    

## 3. Databehoefte per contractvorm (Matrix)

|Datagroep|Flexibel|1-jarig|3-jarig|5-jarig|Toelichting|
|---|---|---|---|---|---|
|**Day-ahead prijzen**|**X**|-|-|-|Flexibel volgt direct de kortetermijn marktuurprijs.|
|**Forward-curves**|-|**X**|**X**|**X**|Langere contracten dekken de inkoop vooraf af op de termijnmarkt.|
|**Verbruiksprofielen**|**X**|**X**|**X**|**X**|Nodig om in te schatten op welke momenten stroom wordt afgenomen.|
|**Klantportefeuille**|**X**|**X**|**X**|**X**|Aantallen, looptijden en volumes per contractvorm.|
|**Tariefcomponenten & Belasting**|**X**|**X**|**X**|**X**|Vaste kosten en overheidsheffingen gelden universeel.|
|**Churn / Opzeggedrag**|-|-|**X**|**X**|Bij langere looptijden neemt het risico op vroegtijdige opzegging toe.|

_(Legenda: X = essentieel)._

## 4. Beschikbare data: Bronregister en Inventarisatie

Fontasya heeft de data aangeleverd in een lokale DuckDB-omgeving (`dev.duckdb`) met diverse staging-tabellen (`stg_*`).

### 4.1 Bronregister

|Bron-ID|Tabel / Bron|Persoonsgegevens|
|---|---|---|
|**B01**|`stg_contracts`|Nee (geanonimiseerde IDs)|
|**B02**|`stg_customers`|Nee (`customer_token`, geen namen)|
|**B03**|`stg_electricity_consumption`|Nee|
|**B04**|`stg_gas_consumption`|Nee|
|**B05**|`stg_energy_balance`|Nee|
|**B06**|`stg_network_system`|Nee|
|**B07**|`stg_pv_assets` & `stg_pv_feedin`|Nee|

## 5. Datakwaliteit

Om de aangeleverde data te beoordelen, is getoetst op vier dimensies:

- **Volledigheid:** De tabellen zijn gestructureerd opgezet en bevatten geldige relaties via `customer_id` en `ean_code`.
    
- **Juistheid:** Waarden zijn technisch plausibel en sluiten aan bij verwachte datatypes in dbt.
    
- **Consistentie:** Eenheden en sleutels komen overeen tussen de contracten-, klanten- en verbruikslijnen.
    
- **Actualiteit & Formaat:** De data is aangeleverd in een modern, efficiënt formaat (DuckDB / Parquet-structuren), wat de technische verwerkbaarheid ten goede komt.
    

## 6. Gap-Analyse (Norm vs. Werkelijkheid)

- **Lange-termijnmarktdata:** Voor de 3- en 5-jaarcontracten ontbreken diepgaande historische langetermijnprijzen; dit moet worden opgevangen met gedocumenteerde aannames en scenario's.
    

## 7. Conclusies en Aanbevelingen

### 7.1 Antwoord op de deelvraag

Voor een degelijk prijsadvies per contractvorm zijn marktdata (spot- en forwardprijzen), verbruiksprofielen van huishoudens en een actuele klantportefeuille vereist. De aangeleverde DuckDB-datasets (`dev.duckdb`) bieden een uitstekende, schone technische structuur en dekken alle entiteiten af

### 7.2 Belangrijkste aanbevelingen

1. **Leg aannames vast:** Omdat lange-termijnmarktdata voor 3- en 5-jaarcontracten schaars is, moeten aannames en extrapolatiemethoden expliciet worden vastgelegd in een aannamenregister.
    
2. **Behoud eenheidstandaarden:** Zorg ervoor dat in de dbt-transformaties een eenduidige standaard wordt gehanteerd voor eenheden (zoals kWh vs. MWh en exclusief/inclusief btw).
    
3. **Opschaling voorbereiden:** Gebruik de huidige 200 records om de dbt-pipeline en het dashboard te bouwen, en plan tijdig een test met opgeschaalde data (richting de 27.000 records).
    

### 7.3 Openstaande vragen aan Fontasya

- Hoe worden de risico-opslagen voor de langere contracten (3 en 5 jaar) momenteel in de praktijk berekend?
    
- Zijn er historische tarieven en besluiten beschikbaar om het model mee te valideren?