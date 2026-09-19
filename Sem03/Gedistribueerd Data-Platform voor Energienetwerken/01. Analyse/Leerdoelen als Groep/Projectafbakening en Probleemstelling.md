# Metadata

- **Author:** Bram Wieringa
- **Date:** 14-09-2026
- **Version:** 1.0
- **Dependencies:** 
	- Leerdoelen Alfew.pdf
	- Leerdoelen in het kort - Timo.pdf
	- Persoonlijke inbreng Abdou.pdf
	- Projectafbakening en Leerdoelen Bram.pdf

## 1. Aanleiding & Context

De oorspronkelijke challenge-omschrijving *"Gedistribueerd Data-Platform voor Energienetwerken"* schetst een breed en diffuus probleem. Om tot een scherpe, haalbare en waardevolle projectomvang te komen, heeft het projectteam eerst de individuele leerdoelen en ambities in kaart gebracht.

Door de individuele wensen te spiegelen aan de vraagstukken binnen de energietransitie, is een heldere gemeenschappelijke deler en probleemstelling gedestilleerd.

### Het Probleem
Traditionele SCADA-systemen en centrale databases zijn gebouwd voor voorspelbare, centrale energieopwekking. Door de snelle toename van decentrale bronnen (zonnepanelen, wind) en dynamische verbruikers (elektrische voertuigen, warmtepompen) ontstaan er steeds sneller lokale pieken en dalen op het net (netcongestie). 

Centrale databases en gegevenssilo's zorgen hierbij voor vertraging, dataduplicatie en een gebrek aan flexibiliteit. Er is dringend behoefte aan een flexibel, graaf-gebaseerd dataplatform dat de fysieke relaties van het netwerk (transformatoren, kabels, wijken) koppelt aan realtime sensordata en omgevingsfactoren, om dreigende overbelasting tijdig te signaleren.

## 2. Teamambities en Leerdoelen

### Individuele Inbreng
* **Alfew (Infrastructuur - Leerjaar 3):**
  * **Focus:** Opzetten en onderbouwen van een schaalbare, container-gebaseerde server- en hostinginfrastructuur voor de gehele dataketen (Graph DB, DWH, API, Dashboard).
* **Timo (Management - Leerjaar 2):**
  * **Focus:** Verzamelen, schonen en analyseren van echte publieke open data (bijv. KNMI, ENTSO-E, netbeheerders) om het datamodel inhoudelijk te onderbouwen.
* **Abdou (Software - Leerjaar 2):**
  * **Focus:** Onderzoeken van de meest geschikte open-source backend-technologie, ontwerpen van het graaf-/ontologiemodel voor netwerkcomponenten en het bouwen van een API.
* **Bram (Management - Leerjaar 2):**
  * **Focus:** Genereren en realtime instromen van sensordata via fysieke/embedded apparatuur (opwek én verbruik), overhevelen van graaf-data naar een Analytics Data Warehouse (DuckDB) en het bouwen van waarschuwingsdashboards.

### Gezamenlijke Ambitie
Het team streeft naar een realistisch, werkend prototype op basis van een **volledige open-source techstack**. Om datakwaliteitsproblemen en realtime uitdagingen realistisch te simuleren, kiest het team ervoor om te werken met **echte open datastromen** en **fysieke/embedded sensorgeneratoren**, en gesimuleerde mockdata enkel als uiterste terugvaloptie te gebruiken.

## 3. Hoofdvraag

> **"Hoe kan op basis van open-source technologieën een schaalbaar en gevalideerd graaf-gebaseerd dataplatform worden ontworpen en gerealiseerd dat fysieke sensordata en publieke bronnen integreert, om realtime inzicht, waarschuwingen en prestatievergelijkingen te bieden bij dreigende netoverbelasting?"**

## 4. Deelvragen

### Infrastructuur & Systeemarchitectuur (Alfew)
1. Welke eisen stelt de gehele dataketen (graph database, datawarehouse, backend API en dashboard) aan een open-source server- en hostinginfrastructuur om zowel realtime operaties als analytische query's betrouwbaar uit te voeren?
2. Op welke wijze worden de container-gebaseerde hosting, netwerkbeveiliging en opslagomgeving (high-level en low-level design) ingericht en beheerd om de beschikbaarheid en schaalbaarheid van het volledige platform te borgen?

### Data-ontsluiting & Externe Analyse (Timo)
1. Welke relevante publieke gegevensbronnen (zoals KNMI, netbeheerders en ENTSO-E) zijn bepalend voor het modelleren van actuele energiestromen?
2. Op welke wijze kunnen deze echte open datastromen worden geanalyseerd en verwerkt om de onderliggende netwerk-ontologie inhoudelijk te onderbouwen en te voeden?

### Ontologie, Graph Database & Backend API (Abdou)
1. Hoe ziet een dynamisch ontologie- en datamodel er in een open-source graph database uit waarin netwerkcomponenten (transformatoren, kabels, wijken) en hun onderlinge relaties flexibel worden vastgelegd?
2. Welke open-source programmeertaal en backend-frameworks zijn het meest geschikt, en op welke wijze kan een hiermee gebouwde API de data uit de graph database efficiënt transformeren, valideren en via endpoints ontsluiten voor de analytics-laag?

### Sensorsimulatie, Datawarehouse & Dashboarding (Bram)
1. Hoe kan de sensordata van diverse energiebronnen (zon, wind, gas, kernenergie) én energieverbruikers (huishoudens, fabrieken, EV-laadparken) via open-source protocollen betrouwbaar worden gegenereerd en realtime worden ingestroomd?
2. Op welke wijze kan data uit de graph database worden getransformeerd naar een Analytics Data Warehouse (bijv. DuckDB) en welk prestativerschil (query-snelheid/schaalbaarheid) levert dit op ten opzichte van directe graph-bevraging?
3. Welke visualisaties en geautomatiseerde waarschuwingsmechanismen binnen het dashboard zijn noodzakelijk om dreigende netcongestie direct en uitlegbaar te presenteren?

## Bronnenlijst
Abdou. (2026). *Persoonlijke inbreng: Gedistribueerd Data-Platform voor Energienetwerken* [Ungepubliceerd document]. Fontys Hogeschool.
Gemini. (2026, 15 september). *Tekstuele verbetering en feedback op de uitwerking van onderzoeksvragen en de projectafbakening* [Large language model chat-log]. Google AI.
Lieuw A On, A. (2026). *Studieplan semester 6: Infrastructure niveau 3* [Ungepubliceerd document]. Fontys Hogeschool.
Timo. (2026). *Leerdoelen in het kort - Timo* (Versie 0.1) [Ungepubliceerd document]. Fontys Hogeschool.
Wieringa, B. (2026a). *Projectafbakening en Leerdoelen Bram* (Versie 1.0) [Ungepubliceerd document]. Fontys Hogeschool.
Wieringa, B. (2026b). *Samenvoeging van leerdoelen groepsgenoten en uitwerking naar conceptuele probleemstelling en projectafbakening* [Ungepubliceerd document]. Fontys Hogeschool.