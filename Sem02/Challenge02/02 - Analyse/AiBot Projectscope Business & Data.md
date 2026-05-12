## Metadata
**Author: ** Bram Wieringa
**Date: ** 12-05-2026
**Version: ** 1.0
**Dependencies: **
- Projectscope
- HappyFlow
- Probleemanalyse

## Inleiding

Dit document beschrijft de scope van het Power BI dashboard dat meet of de AI-chatbot van Stichting Richter Education een succes is. Het dashboard is bedoeld voor de opdrachtgever (de stakeholder) en het projectteam.

Om te bepalen wat succes is, is eerst de kernvraag gesteld: wat doen we eigenlijk en waarom? We maken een chatbot om mensen die iets willen doen met leefstijlverbetering te koppelen aan een passende activiteit. De vraag is dan: werkt dat ook écht?

Om dat te beantwoorden moet het dashboard langs vier dimensies meten:

1. **Gebruik:** wordt de chatbot daadwerkelijk gebruikt?
2. **Kwaliteit van de match:** klopt het advies dat de chatbot geeft?
3. **Gebruikerservaring:** vinden inwoners de chatbot prettig en begrijpelijk?
4. **Impact:** leidt de chatbot tot echte deelname aan activiteiten?

## Projectscope - MoSCoW

### Must have

_Essentieel – zonder deze onderdelen is het dashboard niet geslaagd._

- Een werkend Power BI dashboard met minimaal één pagina voor minimaal twee uitgewerkt dimensie (Gebruik, Matchkwaliteit, Gebruikerservaring, Impact)
- Visualisatie van het aantal gestarte en voltooide gesprekken per week
- Inzicht in het voltooiingspercentage van gesprekken (% dat eindigt met een match-output)
- Inzicht in de match-acceptatierate (% gebruikers dat een voorgestelde activiteit opvolgt)
- Een koppeling aan de chatbot-backend als databron (via export of directe koppeling)
- KPI-cards bovenaan elke pagina met RAG-status (Rood/Oranje/Groen op basis van streefwaarden)
- Het dashboard verwerkt geen persoonsgegevens (privacy by design)

### Should have

_Belangrijk, maar niet strikt noodzakelijk om te slagen._

- Trechtervisualisatie (funnel) die toont op welke stap in het gesprek gebruikers afhaken
- Uitsplitsing van matches per Leefstijlroer-pijler (voeding, beweging, ontspanning, slaap, verbinding, middelen)
- Weergave van gemiddelde gesprekslengte in minuten
- Inzicht in het gebruik per apparaattype (desktop vs. mobiel)
- Weergave van het percentage gebruikers dat contactgegevens heeft achtergelaten (ja/nee, geen inhoud)
- Tijdfilter op weekniveau zodat trends over tijd zichtbaar zijn

### Could have

_Wenselijk als er tijd en capaciteit voor is._

- Gauge-visual voor de gebruikerstevredenheidsscore (CES, 1–5)
- Inzicht in doorverwijzingsconversie vanuit CRM-data van de stichting
- Weergave van het percentage "geen passende match" gesprekken
- Overzicht van nieuwe activiteitsverzoeken (activiteiten die gebruikers wensen maar niet bestaan)
- Automatische dagelijkse refresh van de data

### Won't have

_Buiten scope voor deze versie._

- Individuele gebruikersprofielen of herleidbare persoonsgegevens
- Real-time livestream van gesprekken
- Integratie met externe systemen buiten de chatbot-backend en het CRM van de stichting
- Meertalige weergave van het dashboard

## Databronnen

|Databron|Inhoud|Koppeling|
|---|---|---|
|Chatbot-backend (sessie-logs)|Gebruik, voltooiing, matchoutput, afhaakpunt|CSV-export of REST API|
|Contactformulier-log|Contactverzoeken (anoniem geaggregeerd)|Database of export|
|Enquêteresultaten|CES-score en vertrouwensmeting (optioneel)|CSV-export|
|CRM stichting|Opvolging en deelname aan activiteiten|Handmatige import|

## Minimale logvelden chatbot-backend

Voor het dashboard zijn onderstaande velden minimaal nodig in de sessie-logs van de chatbot:

|Veld|Type|Toelichting|
|---|---|---|
|`sessie_id`|String (hash)|Anoniem, niet herleidbaar tot persoon|
|`timestamp_start`|Datetime|Starttijd gesprek|
|`timestamp_einde`|Datetime|Eindtijd gesprek|
|`instroomtype`|Categorie|precies / beetje / helemaal_niet|
|`stap_afgebroken`|Integer / null|Null als gesprek volledig is|
|`match_output`|Array|Drie activiteit-ID's|
|`pijler_output`|Array|Drie Leefstijlroer-pijlers|
|`geen_match`|Boolean|True als geen passende activiteit gevonden|
|`contact_ingevuld`|Boolean|True als gebruiker contactgegevens achterliet|
|`offline_doorverwezen`|Boolean|True als doorverwezen naar inloop|
|`ces_score`|Integer / null|1–5, null als niet ingevuld|
|`device_type`|Categorie|desktop / mobiel|

## Vervolgstappen

1. Backlog-item aanmaken voor sessie-logging in de chatbot-backend op basis van bovenstaande velden
2. Streefwaarden per KPI valideren met de opdrachtgever
3. Power BI workspace inrichten en databronnen koppelen
4. Eerste dashboard bouwen zodra gebruikersdata beschikbaar is (na sprint 1)
5. Optioneel: enquête ontwerpen voor CES en vertrouwensmeting (sprint 2)

_Opgesteld op basis van: Projectscope v1.4, Probleemanalyse v1.0, Happy Flow v1.1 – AI-chatbot Sociaal Knooppunt_