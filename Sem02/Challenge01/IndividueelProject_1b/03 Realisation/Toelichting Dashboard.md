## Metadata
**Author: ** Bram Wieringa
**Date: ** 17-04-2026
**Version: ** 1.0
**Dependencies: ** 
- OK-Planning Kosten - Analyse versie 1.3

## Inleiding
Dit dashboard is ontwikkeld als onderdeel van de financiële analyse van het OK-planningsproces. Het biedt inzicht in de operationele kosten en efficiëntie van het huidige planningsproces, met specifieke focus op de transitie van telefonisch patiëntcontact naar geautomatiseerde, asynchrone communicatie (patiëntenportaal).

Het dashboard sluit aan op de analyse _OK-Planning Kosten – Analyse (v1.3, Bram Wieringa, 2026)_ en vertaalt de daarin gedefinieerde KPI's naar visuele stuurinformatie voor de manager OK-planners.

## Achtergrond & Probleembeschrijving
Het huidige planningsproces is sterk afhankelijk van synchroon telefonisch contact. Dit leidt tot zogenoemd synchronisatieverlies: planners besteden een aanzienlijk deel van hun werktijd aan niet-effectieve handelingen zoals voicemailberichten, herhaalbelpogingen en wachttijd. Deze tijd wordt wel betaald, maar levert geen directe waarde op, ook wel aangeduid als Non-Value Added Time (NVAT).

Het dashboard maakt deze verborgen kostenpost zichtbaar en biedt de manager een sturingsinstrument om de business case voor digitalisering financieel te onderbouwen.

## Doelstelling Dashboard

Het dashboard heeft als doel inzicht te bieden in de huidige operationele kosten en efficiëntie van het planningsproces op basis van trenddata over de periode 2022–2024. Er is geen formele nulmeting uitgevoerd voorafgaand aan de introductie van digitale communicatiekanalen. De beschikbare data geeft daarmee een trendbeeld, maar maakt geen harde voor/na-vergelijking mogelijk. Het uitvoeren van een alsnog te definiëren nulmeting is de meest urgente vervolgstap om de werkelijke ROI van de digitalisering aantoonbaar te maken.

## KPI-definities

De volgende KPI's vormen de kern van het dashboard. Ze zijn gedefinieerd in de analyse en direct terug te vinden in de visualisaties:

|KPI|Definitie|Financiële invalshoek|
|---|---|---|
|**Cost per Booking (CPB)**|Totale loonkosten planners / aantal succesvolle planningen|Maakt de directe besparing per patiënt inzichtelijk|
|**Non-Value Added Time (NVAT)**|% werktijd besteed aan mislukte belpogingen en voicemails|Toont de verborgen kosten van inefficiëntie|
|**Digital Adoption Rate**|% patiënten dat digitaal bereikbaar is|Hoe hoger, hoe lager de handmatige beldruk|
|**Gem. tevredenheid patiënt** _Bonus KPI_|Gemiddelde score op schaal 0-10|Bewaakt of digitalisering de patiëntervaring niet schaadt|


## KPI-pagina

### Gemiddelde kosten per planning per periode

Deze lijndiagram toont de ontwikkeling van de Cost per Booking (CPB) per maand van januari 2022 tot en met december 2024. De trendlijn fluctueert tussen circa €20 en €26, zonder structurele daling. Dit bevestigt dat het huidige proces geen inherente kostenreductie realiseert. Omdat er geen formele nulmeting beschikbaar is, kan niet worden vastgesteld wat het kostenniveau was vóór eventuele digitale interventies.

KPI-kaart - Gem. Kosten per Planning: De gemiddelde kosten per planning over de meetperiode bedragen € 23,12.

### Tijd kwijt aan telefoneren per periode

Deze lijndiagram visualiseert de Non-Value Added Time (NVAT): het percentage werktijd besteed aan telefoneren, inclusief mislukte pogingen en voicemails. De grafiek toont een lichte daling over de meetperiode (van pieken rond 37% naar een bandbreedte van 20-35%), maar deze daling kan niet worden toegeschreven aan een specifieke maatregel bij gebrek aan een nulmeting.

KPI-kaart - Tijd kwijt aan telefoneren: Gemiddeld is 29% van de werktijd besteed aan telefoneren.

### Patiëntenportaal toestemming

Dit cirkeldiagram toont de Digital Adoption Rate: het aandeel patiënten dat toestemming heeft gegeven voor digitaal contact via het patiëntenportaal.

- Waar (toestemming gegeven): 50,4%
- Onwaar (geen toestemming): 49,6%

De helft van de patiënten is daarmee nog steeds alleen telefonisch bereikbaar, wat direct bijdraagt aan de NVAT en de CPB. De Digital Adoption Rate is de belangrijkste hefboom voor kostenbesparing: elke procentpunt stijging verlaagt direct het aandeel dure telefonische contacten.

### Gemiddelde tevredenheid patiënt

Dit meterdiagram toont de gemiddelde patiënttevredenheid op een schaal van 0 tot 10. De huidige score bedraagt 5,50. Deze KPI bewaakt of de overstap naar digitale communicatie de patiëntervaring niet negatief beïnvloedt. Dit is een bonus kpi, die geen grondslag heeft in de analyse.

## Pagina 2: Medewerkers

### Aantal planningen per medewerker per periode

Deze lijndiagram toont het aantal planningen per medewerker per maand over de periode 2022-2024. De volgende medewerkers zijn weergegeven:

- Annemijn Charon
- Fatima Diesbergen
- Fem van der Strigt
- Jade Persijn
- Nout van Ginneke

De grafiek maakt het mogelijk om de werklast per medewerker over tijd te vergelijken. 

### Aantal planningen per medewerker (staafdiagram)

Dit staafdiagram toont het totale aantal planningen per medewerker over de geselecteerde periode:

|Medewerker|Aantal planningen (ca.)|
|---|---|
|Fem van der Strigt|512|
|Jade Persijn|511|
|Fatima Diesbergen|503|
|Annemijn Charon|489|
|Nout van Ginneke|485|

De verdeling is relatief gelijkmatig. In combinatie met de NVAT-gegevens kan worden berekend hoeveel capaciteit per medewerker vrijkomt bij een hogere Digital Adoption Rate.


### Samenvattende KPI's (Medewerkers)

|KPI|Waarde|
|---|---|
|Gemiddelde prijs per uur|€ 66,20|
|Gemiddelde kosten per planning|€ 23,12|
|Gemiddeld minuten per planning|21,01|

Het uurtarief van € 66,20 (inclusief werkgeverslasten) vormt de basis voor de berekening van de CPB en de potentiële FTE-besparing. Elke minuut minder NVAT per planning resulteert in directe loonkostenreductie.


### Datumfilter

Via het filter _"Selecteer Datum"_ kan de gebruiker de weergave beperken tot 2022, 2023 of 2024. Alle grafieken en KPI's passen zich dynamisch aan op basis van de gekozen selectie, wat vergelijking tussen jaren mogelijk maakt.


## Gebruiksaanwijzing

1. Navigeer via het linkerpaneel tussen de pagina's KPI's en Medewerkers.
2. Gebruik de schuifbalken onder de lijndiagrammen om de tijdsperiode te verfijnen.
3. Gebruik het datumfilter op de medewerkerspagina om te filteren op jaar.
4. Hover over de grafieken voor exacte waarden per maand.
5. Gebruik de staafgrafiek bij Aantal planningen per medewerker om via Ctrl + klik één of meerdere medewerkers te selecteren en de overige visualisaties daarop te filteren.

## Bronvermelding

- Wieringa, B. (2026). _OK-Planning Kosten – Analyse_ (Versie 1.3). Ongepubliceerd document, Fontys ICT.

- Anthropic. (2026). _Claude_ (Versie claude-sonnet-4-6) [Large language model]. [https://claude.ai](https://claude.ai). Ingezet voor het opstellen en structureren van de dashboardtoelichting op basis van aangeleverde schermafbeeldingen van het Power BI dashboard en de financiële analyse. Claude heeft de KPI-definities vertaald naar beschrijvende tekst, de financiële context uit de analyse verwerkt in de toelichting per visualisatie, en de bronvermelding opgesteld in APA-stijl. Geraadpleegd op 17 april 2026.