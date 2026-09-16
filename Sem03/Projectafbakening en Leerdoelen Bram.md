# Metadata

- **Author:** Bram Wieringa
- **Date:** 14-09-2026
- **Version:** 1.0
- **Dependencies:** None

## Aanleiding
De opdrachtomschrijving van het project is dermate diffuus dat er geen heldere probleemstelling uit gedestilleerd kan worden. Om toch een scherpe koers te bepalen, beantwoordt ieder groepslid eerst de volgende drie vragen:

1. Wat wil ik dit semester leren?
2. Hoe past dit binnen het project?
3. Wat heb ik daarvoor nodig?

Wanneer alle vier de groepsleden deze vragen hebben beantwoord, zoeken we naar de gemeenschappelijke deler om als groep een heldere en gedragen probleemstelling te formuleren.

## Persoonlijke Inbreng: Bram

### 1. Wat wil ik leren dit semester?

Het opzetten van een graph database en het vullen hiervan met data afkomstig uit embedded sensoren die verschillende energieopwekkers en -verbruikers simuleren. Vervolgens wil ik deze data integreren met een datawarehouse en ontsluiten via een dashboard. Mijn voorkeur gaat uit naar een volledig open-source techstack.

### 2. Hoe past dit binnen het project?

We bouwen een graph database die gevoed wordt met data uit inkomende fysieke sensoren. Hiermee simuleren we diverse energiebronnen en -verbruikers. Vervolgens transporteer ik deze data naar een datawarehouse om het dashboard van actuele data te voorzien. Het gehele proces wordt bij voorkeur ingericht met open-sourcetooling.

### 3. Wat heb ik daarvoor nodig?

- **Hardware:** Sensoren en/of microcontrollers die de benodigde metingen en data genereren.
- **Graph database:** Een databaseoplossing die deze datastromen efficiënt kan verwerken.
- **Serveromgeving:** Een geschikte server (of containeromgeving) om de graph database, het datawarehouse en het dashboard op te laten draaien.


Hoe kan een graaf-gebaseerde data-architectuur worden ontworpen en gerealiseerd om dynamische netwerk- en sensordata betekenisvol te koppelen, zodat dreigende netoverbelasting tijdig inzichtelijk wordt gemaakt?

In hoeverre biedt een graaf-gebaseerde ontologie betere flexibiliteit en realtime inzicht in netoverbelasting vergeleken met een traditionele centrale database-aanpak binnen een smart grid-omgeving?

Op welke wijze kan een ontologie-gebaseerd dataplatform worden ingericht dat heterogene energiesensordata transformeert en visualiseert om risico's op netcongestie automatisch te signaleren?

## Wat wil iedereen samengevat:
### Induvidueel:
Alfew, Infrastructuur opzetten
Timo, Verzamelen van data uit publieke databronnen en dit analyseren
Abdou, Python en data uit verschillende bronnen inlezen. Graph databases en ontology structuren API maken dat data aan een dashboard geeft
Bram, Graphdata overzetten naar een datawarehouse, combinerern met andere data en kijken of er iets nuttigs over gezegd kan worden. Daarnaast voorkeur om data te generen via echte neppe sensoren, en dus niet te werken met mockdata.

### Gezamelijk:
Realistische data infrastructuur maken (kan via embedded devices kan je simuleren, embedded devices is realistiscer omdat dit problemen met data gaat geven)Graph database opzetten, data daaruit (via API) naar een datawarehouse plaatsen, daar het te combineren met andere openbare bronnen, daaruit dashboards met inzichten te maken. 

## Voorstel Hoofdvraag
>_Hoe kan op basis van open-source technologieën een schaalbaar en gevalideerd graaf-gebaseerd dataplatform worden ontworpen en gerealiseerd dat fysieke sensordata en publieke bronnen integreert, om realtime inzicht, waarschuwingen en prestatievergelijkingen te bieden bij dreigende netoverbelasting?_

### Deelvragen
#### Deelvragen Alfew
- Welke eisen stelt de gehele dataketen (graph database, datawarehouse, backend API en dashboard) aan een open-source server- en hostinginfrastructuur om zowel realtime operaties als analytische query's betrouwbaar uit te voeren?
- Op welke wijze worden de container-gebaseerde hosting, netwerkbeveiliging en opslagomgeving (high-level en low-level design) ingericht en beheerd om de beschikbaarheid en schaalbaarheid van het volledige platform te borgen?

#### Deelvragen Timo
- Welke relevante publieke gegevensbronnen (zoals KNMI, netbeheerders en ENTSO-E) zijn bepalend voor het modelleren van actuele energiestromen?
- Op welke wijze kunnen deze echte open datastromen worden geanalyseerd en verwerkt om de onderliggende netwerk-ontologie inhoudelijk te onderbouwen en te voeden?

#### Deelvragen Abdou
- Hoe ziet een dynamisch ontologie- en datamodel er in een open-source graph database uit waarin netwerkcomponenten (transformatoren, kabels, wijken) en hun onderlinge relaties flexibel worden vastgelegd?
- Welke open-source programmeertaal en backend-frameworks zijn het meest geschikt, en op welke wijze kan een hiermee gebouwde API de data uit de graph database efficiënt transformeren, valideren en via endpoints ontsluiten voor de analytics-laag?

#### Deelvragen Bram
- Hoe kan de sensordata van diverse energiebronnen (zon, wind, gas, kernenergie) én energieverbruikers (huishoudens, fabrieken, EV-laadparken) via open-source protocollen betrouwbaar worden gegenereerd en realtime worden ingestroomd?
- Op welke wijze kan data uit de graph database worden getransformeerd naar een Analytics Data Warehouse (bijv. DuckDB) en welk prestativerschil (query-snelheid/schaalbaarheid) levert dit op ten opzichte van directe graph-bevraging?
- Welke visualisaties en geautomatiseerde waarschuwingsmechanismen binnen het dashboard zijn noodzakelijk om dreigende netcongestie direct en uitlegbaar te presenteren?