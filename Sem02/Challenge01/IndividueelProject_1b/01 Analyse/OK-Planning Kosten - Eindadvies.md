## Metadata
**Author: ** Bram Wieringa
**Date: ** 12-04-2026
**Version: ** 1.0
**Dependencies: ** 
- OK-Planning Kosten - Analyse versie 1.3
- dashboardv4_1.png
- dashboardv4_2.png

## Begrippenlijst

|Begrip|Afkorting|Definitie|
|---|---|---|
|Cost per Booking|CPB|De gemiddelde loonkosten per succesvolle planning, berekend als totale personeelskosten gedeeld door het aantal gerealiseerde planningen.|
|Non-Value Added Time|NVAT|Het percentage van de werktijd dat besteed wordt aan handelingen die geen directe planningswaarde opleveren, zoals mislukte belpogingen en voicemails.|
|Digital Adoption Rate|DAR|Het percentage patiënten dat toestemming heeft gegeven voor digitaal contact via het patiëntenportaal, en daarmee bereikbaar is zonder telefonische interventie.|
|Full-Time Equivalent|FTE|Een rekeneenheid voor personeelscapaciteit waarbij 1,0 FTE gelijk staat aan één voltijds werkende medewerker.|
|Key Performance Indicator|KPI|Een meetbare prestatie-indicator waarmee de voortgang richting een strategisch doel wordt bijgehouden.|
|Return on Investment|ROI|Een maatstaf die de verhouding uitdrukt tussen de behaalde besparing of opbrengst en de gedane investering, uitgedrukt als percentage of ratio.|
|Synchronisatieverlies|-|Het verlies aan productieve tijd dat ontstaat wanneer twee partijen (planner en patiënt) niet gelijktijdig beschikbaar zijn voor telefonisch contact.|
|Asynchrone communicatie|-|Een communicatievorm waarbij zender en ontvanger niet gelijktijdig aanwezig hoeven te zijn, zoals SMS, e-mail of berichten via een patiëntenportaal.|
|Nulmeting|-|Een gecontroleerde meting van de beginsituatie, uitgevoerd vóór een interventie, die dient als referentiepunt om de impact van een verandering te kunnen aantonen.|
|Power BI|-|Een business intelligence-tool van Microsoft waarmee data visueel wordt weergegeven in interactieve dashboards en rapporten.|


## Inleiding
Dit adviesrapport is opgesteld in het kader van opdracht 1b van de Fontys ICT-opleiding en vormt de afronding van een tweeledige analyse van het OK-planningsproces. Waar opdracht 1a zich richtte op de logistieke en procesmatige optimalisatie van de werkstroom, verschuift de focus in dit rapport naar de financiële en bestuurlijke dimensie: wat is de business case achter de digitalisering van het patiëntcontact, en wat betekent dit concreet voor de organisatie?

### Aanleiding
Het OK-planningsproces binnen de onderzochte zorginstelling is in hoge mate afhankelijk van synchroon telefonisch contact. Planners bellen patiënten om afspraken te bevestigen of in te plannen. Wanneer een patiënt niet opneemt, volgen herhaalpogingen met als gevolg dat een aanzienlijk deel van de werktijd opgaat aan handelingen die geen directe planningswaarde opleveren. Dit wordt in dit rapport aangeduid als Non-Value Added Time (NVAT).

De introductie van digitale communicatiekanalen, zoals het patiëntenportaal, biedt een concrete kans om dit synchronisatieverlies te reduceren. Niet als technisch experiment, maar als financieel verantwoorde keuze die de werkdruk verlaagt en de beschikbare capaciteit van OK-planners effectiever benut.

### Doel van dit rapport
Dit rapport heeft drie doelstellingen:

1. Het inzichtelijk maken van de huidige operationele kosten en inefficiënties op basis van dashboarddata (2022–2024).
2. Het formuleren van een onderbouwde business case voor de overstap naar asynchrone digitale communicatie.
3. Het adviseren van concrete vervolgstappen waarmee de manager OK-planners de digitalisering financieel kan sturen en verantwoorden.

### Leeswijzer

Dit rapport is opgebouwd uit de volgende onderdelen:

- **Begrippenlijst:** Definities van alle gehanteerde termen en afkortingen, zodat het rapport toegankelijk is voor alle lezers.
- **Managementsamenvatting:** Een beknopt overzicht van het probleem, de belangrijkste bevindingen en de centrale aanbeveling, bedoeld voor lezers die snel inzicht willen.
- **Hoofdstuk 2 Probleemanalyse:** Een beschrijving van het huidige planningsproces, het financiële knelpunt en de kritische kanttekening rondom het ontbreken van een nulmeting.
- **Hoofdstuk 3 Data-onderbouwde Inzichten:** De bevindingen vanuit het ontwikkelde Power BI Dashboard, uitgesplitst naar KPI-pagina en Medewerker-pagina.
- **Hoofdstuk 4 Business Impact:** De verwachte financiële en kwalitatieve impact van de digitalisering, inclusief een risico-overzicht.
- **Hoofdstuk 5 Aanbevelingen:** Vier concrete aanbevelingen voor de manager OK-planners, gerangschikt op prioriteit.
- **Hoofdstuk 6 Vervolgstappen:** Een overzicht van te nemen acties, verantwoordelijken en tijdlijnen.
- **Hoofdstuk 7 Conclusie:** De eindconclusie en de belangrijkste boodschap van dit rapport.

## 1. Managementsamenvatting

Het planningsproces binnen de OK-afdeling leunt sterk op synchroon telefonisch contact met patiënten. Dit leidt tot aanzienlijk "synchronisatieverlies": OK-planners besteden gemiddeld 29% van hun werktijd aan telefoneren, waarvan een substantieel deel bestaat uit mislukte belpogingen en voicemail-loops. De gemiddelde kosten per planning bedragen € 23,12**, bij een uurtarief van € 66,20 en een gemiddelde planningstijd van 21 minuten.

De overstap naar asynchrone digitale communicatie (patiëntenportaal) biedt een directe kans om deze verborgen kostenpost te reduceren. Op dit moment heeft 50,4% van de patiënten toestemming gegeven voor digitaal contact, elke procentpunt stijging in deze adoptiegraad verlaagt direct de Cost per Booking.

Kritische kanttekening: Er is geen formele nulmeting uitgevoerd voorafgaand aan de implementatie. Hierdoor is het op dit moment niet mogelijk om de werkelijke besparing ten opzichte van de uitgangssituatie te kwantificeren. Het uitvoeren van een nulmeting is de meest urgente aanbeveling van dit rapport.

## 2. Probleemanalyse
### 2.1 Huidig proces
Het huidige planningsproces is gebaseerd op synchroon contact: een OK-planner belt de patiënt om een afspraak te bevestigen of te plannen. Wanneer de patiënt niet opneemt, volgt later opnieuw een belpoging of wordt een voicemail ingesproken, zonder garantie op terugkoppeling. Dit proces herhaalt zich totdat contact is gelegd.

### 2.2 Financieel knelpunt
Dit synchronisatieverlies heeft directe financiële gevolgen:

- Elke mislukte belpoging telt mee als loonkost zonder planningsresultaat.
- De Cost per Booking (€ 23,12) omvat daarmee niet alleen de effectieve planningstijd, maar ook alle vergeefse pogingen daaromheen.
- Met vijf medewerkers en een uurtarief van € 66,20 lopen de verborgen kosten van NVAT snel op.

### 2.3 Ontbrekende nulmeting
Een cruciaal gemis in de huidige analyse is het ontbreken van een formele nulmeting. De dashboarddata loopt van januari 2022 t/m december 2024, maar er is geen gecontroleerd startpunt vastgelegd vóór de introductie van digitale alternatieven. Dit betekent dat:

- Het niet mogelijk is om aan te tonen hoeveel de kosten zijn gedaald ten opzichte van de beginsituatie.
- De huidige cijfers (€ 23,12 CPB, 29% NVAT) mogelijk al een gedeeltelijk verbeterd beeld geven.
- De business case op dit moment onderbouwd is met trenddata, maar niet met een harde voor/na-vergelijking.


## 3. Data-onderbouwde Inzichten
### 3.1 Power BI Dashboard
Om de business case te onderbouwen is een Power BI Dashboard ontwikkeld met twee pagina's: een KPI-overzicht en een Medewerker-pagina. De data beslaat de periode januari 2022 tot en met december 2024. De medewerker-paginga is vooral bedoelt als oefening voor de schrijver van dit document, oefening in power-bi.

### 3.2 KPI-pagina: Operationele kerngetallen
**Gemiddelde kosten per planning (Cost per Booking):** De gemiddelde kosten per planning bedragen over de gehele meetperiode € 23,12. De trendlijn toont fluctuaties tussen circa €20 en €26, zonder een structurele daling. Dit bevestigt dat het huidige telefonische proces geen inherente kostenreductie realiseert. Zonder nulmeting is echter niet vast te stellen wat het kostenniveau was vóór eventuele digitale interventies.

**Tijd kwijt aan telefoneren (NVAT-indicator):** Gemiddeld besteden OK-planners 29% van hun werktijd aan telefoneren. De grafiek laat een lichte daling zien over de meetperiode (van pieken rond 37% naar een bandbreedte van 20–35%), maar dit kan niet worden toegeschreven aan een specifieke maatregel zolang er geen nulmeting beschikbaar is.

**Patiëntenportaal toestemming (Digital Adoption Rate):** Van alle patiënten heeft 50,4% toestemming gegeven voor digitaal contact, tegenover 49,6% zonder toestemming. Dit betekent dat de helft van de patiënten nog via het duurdere telefonische kanaal bereikt moet worden. Dit cijfer is de directe hefboom voor kostenbesparing.

**Gemiddelde patiënttevredenheid:** De tevredenheid wordt gemiddeld gewaardeerd met een 5,5 op 10. Dit is een matige score en suggereert dat het huidige contact niet als optimaal wordt ervaren, een bijkomend argument voor de overstap naar digitaal om te kijken wat het doet met dit cijfer.

### 3.3 Medewerker-pagina: Capaciteit en productiviteit

De vijf OK-planners realiseren elk tussen de ~485 en ~510 planningen over de gehele periode, met een beperkte onderlinge spreiding. Dit wijst op een gelijkmatige werkverdeling.

|Kengetal|Waarde|
|---|---|
|Gemiddelde prijs per uur|€ 66,20|
|Gemiddelde kosten per planning|€ 23,12|
|Gemiddeld minuten per planning|21,01 min|

### 3.4 Kernobservatie
De combinatie van 29% NVAT en een Digital Adoption Rate van slechts 50,4% vormt de kern van de inefficiëntie. Als de adoptiegraad stijgt naar bijvoorbeeld 75%, daalt het aandeel dure telefonische contacten significant, wat bij het huidige tariefniveau een directe besparing op loonkosten oplevert. Hoe groot die besparing precies is, kan pas worden aangetoond na het uitvoeren van een nulmeting.


## 4. Business Impact
### 4.1 Potentiële besparing (indicatief)
Hoewel een harde berekening pas mogelijk is na een nulmeting, is op basis van de beschikbare data een indicatieve schatting te maken:

- Bij een stijging van de Digital Adoption Rate van 50% naar 75% daalt het aandeel telefonische contacten met de helft van de huidige restgroep.
- Minder telefonische contacten betekent minder NVAT per medewerker per dag.
- Bij vijf medewerkers en een uurtarief van € 66,20 levert elke 1% daling in NVAT een meetbare kostenbesparing op jaarbasis op.

**Deze berekening blijft indicatief zolang geen nulmeting beschikbaar is.**

### 4.2 Kwalitatieve impact
- **Lagere werkdruk** voor OK-planners door minder belpogingen.
- **Betere inzetbaarheid** van vrijgekomen capaciteit voor complexere planningstaken.
- **Hogere patiënttevredenheid** als gevolg van meer controle over je eigen operatieplanning. (verwachting).

### 4.3 Risico's

|Risico|Toelichting|Mitigatie|
|---|---|---|
|Lage adoptiebereidheid|Oudere patiënten geven minder snel toestemming voor digitaal contact|Gerichte communicatie en begeleiding bij portaalregistratie|
|Ontbrekende nulmeting|Besparing is niet aantoonbaar zonder startpunt|Alsnog een nulmeting definiëren en vastleggen (zie aanbevelingen)|
|Datakwaliteit|Dashboarddata is gebaseerd op beschikbare registraties, mogelijke gaps|Validatie van bronsystemen vóór rapportage|


## 5. Aanbevelingen
**Aanbeveling 1 - Voer alsnog een nulmeting uit (prioriteit: hoog)** Definieer een gecontroleerd referentiepunt op basis van historische data (bijv. de situatie van januari 2022, vóór eventuele digitale interventies). Zonder dit startpunt blijft de business case indicatief en is het onmogelijk om de werkelijke ROI van de digitalisering aan te tonen richting directie.

**Aanbeveling 2 - Stel een adoptiedoelstelling in** Definieer een concreet target voor de Digital Adoption Rate, bijvoorbeeld 70% binnen 12 maanden. Monitor dit maandelijks via het dashboard en koppel er een actieplan aan voor patiënten die nog geen portaaltoestemming hebben gegeven.

**Aanbeveling 3 - Gebruik het dashboard als sturingsinstrument** Het Power BI Dashboard biedt nu al inzicht in CPB, NVAT en adoptiegraad. Zorg dat de manager dit actief gebruikt in periodieke overleggen om bij te sturen op individuele medewerkers en periodetrends.

**Aanbeveling 4 - Verhoog patiënttevredenheid als secondaire KPI** Een tevredenheidscore van 5,5/10 is een signaal dat het huidige contact voor verbetering vatbaar is. Meet na de digitale transitie opnieuw om aan te tonen of de score stijgt.

## 6. Vervolgstappen

|Stap|Actie|Verantwoordelijke|Tijdlijn|
|---|---|---|---|
|1|Nulmeting definiëren op basis van historische data (jan 2022)|Data-analist / Bram|Direct|
|2|Adoptiedoelstelling vaststellen met manager|Manager OK-planners|Maand 1|
|3|Actieplan portaalregistratie voor patiënten zonder toestemming|Planningsteam|Maand 1–2|
|4|Maandelijkse KPI-review instellen via dashboard|Manager|Maand 2|
|5|Herbeoordeling business case na nulmeting|Bram / Manager|Maand 3|
|6|Eindrapportage met harde voor/na-vergelijking richting directie|Manager|Maand 6–12|

## 7. Conclusie

De digitalisering van het patiëntcontact binnen de OK-planning is financieel en operationeel goed te onderbouwen op basis van de beschikbare dashboarddata. Een NVAT van 29% en een Cost per Booking van € 23,12 bij een uurtarief van € 66,20 tonen aan dat er structurele ruimte is voor efficiëntiewinst.

De grootste beperking van dit rapport is het ontbreken van een formele nulmeting. Zonder dit referentiepunt is de werkelijke besparing niet aantoonbaar, alleen indicatief. Dit is tegelijkertijd de meest urgente vervolgstap: door alsnog een nulmeting vast te leggen op basis van de vroegste beschikbare data, kan de business case worden omgezet van een indicatief advies naar een kwantitatief bewezen ROI.

Het Power BI Dashboard vormt hiervoor het fundament. Met de juiste sturing op Digital Adoption Rate en een gevalideerde nulmeting is de manager in staat om de digitalisering financieel te verantwoorden en de vrijgekomen capaciteit van OK-planners effectief in te zetten.

## 8. Bronvermelding

**Interne Documentatie** Wieringa, J.C.L. (2026). _OK-Planning - Financiële Analyse (versie 1.3 – Opdracht 1b)_. Ongepubliceerd document, Fontys ICT.

Wieringa, J.C.L. (2026). _OK-Planning - Analyse (versie 1.5 - Opdracht 1a)_. Ongepubliceerd document, Fontys ICT.

**Data** Power BI Dashboard - OK-Planning KPI's & Medewerkeranalyse (versie 4, 2026). Ontwikkeld door B. Wieringa op basis van interne planningsdata 2022–2024.

**AI-Assistentie** Claude (2026). _Ondersteuning bij rapportstructurering, tekstformulering en data-interpretatie_. Anthropic. Geraadpleegd op 12 april 2026.