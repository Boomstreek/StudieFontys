## Metadata
**Author: ** Bram Wieringa
**Date: ** 26-04-2026
**Version: ** 1.0
**Dependencies: **
- Transcriptie: AI-bot sessie.docx 
- Transcriptie: Kennismaken AI-groep S2.docx


## Probleemanalyse - AI-chatbot "Het Sociaal Knooppunt"

### 1. Achtergrond en opdrachtgever

De opdracht is afkomstig van Carla Renders, voorszitter van Stichting Richter Education, die inwoners van gemeente Boxtel ondersteunt bij het verbeteren van hun leefstijl en welzijn via het programma Leergebied® Gezond. De stichting werkt vanuit twee erkende gespreksmodellen:

- **Positieve Gezondheid** (Instituut voor Positieve Gezondheid) - een spinnenweb van zes dimensies waarbij gezondheid verder gaat dan ziekte, met nadruk op veerkracht, zingeving en zelfmanagement.
- **Het Leefstijlroer** (Vereniging Arts en Leefstijl) - een gespreksinstrument op basis van zes pijlers: voeding, beweging, ontspanning, slaap, verbinding en middelen.

Beide modellen zijn ontworpen als gestructureerde gesprekstools voor professionals en vormen de inhoudelijke basis van de beoogde chatbot.

### 2. Probleemstelling

#### 2.1 Kern van het probleem

Inwoners van gemeente Boxtel, met name mensen in kwetsbare posities zoals armoede, werkloosheid of sociale uitsluiting, hebben onvoldoende toegang tot een actueel en passend overzicht van leefstijl- en welzijnsactiviteiten in hun omgeving. Bestaande digitale leefstijlkaarten en websites zijn doorgaans verouderd en bieden geen persoonlijke matching op basis van iemands situatie en wensen.

Tegelijkertijd beschikt geen enkele professional in de gemeente over een volledig en actueel totaaloverzicht van het beschikbare leefstijlaanbod, waardoor ook zorgprofessionals en welzijnswerkers onvoldoende kunnen doorverwijzen.

#### 2.2 Doelgroep

De primaire doelgroep bestaat uit inwoners van gemeente Boxtel in de leeftijd van **15 tot 99 jaar**, met specifieke aandacht voor mensen die te maken hebben met de **gezondheidskloof**: personen met een laag inkomen, in armoede, werkeloos of arbeidsongeschikt. De taal van de tool mag niet ingewikkelder zijn dan **taalniveau B1**, zodat de chatbot ook toegankelijk is voor jongere en/of laaggeletterder gebruikers.

Secundair kunnen ook welzijnswerkers en zorgprofessionals de tool gebruiken als ondersteuningsmiddel tijdens gesprekken met inwoners.

#### 2.3 Gewenst eindresultaat

Carla heeft als succescriterium voor de komende negen weken geformuleerd: een **werkend demo-prototype** van een chatbot die:

1. leefstijl- en welzijnsvragen van inwoners beantwoordt via een gestructureerd gesprek;
2. de situatie van de gebruiker systematisch verkent aan de hand van één van de twee gespreksmodellen;
3. de uitkomsten matcht met het beschikbare leefstijlaanbod in gemeente Boxtel;
4. drie passende activiteiten als resultaat teruggeeft;
5. op verzoek van de gebruiker contact laat opnemen door een aanbieder (waarbij minimale persoonsgegevens worden verwerkt).

De tool wordt uiteindelijk ontsloten via de website **[www.sociaal-knooppunt.nl](http://www.sociaal-knooppunt.nl)** als zelfstandige applicatie of chatvenster.

### 3. Deelproblemen en uitdagingen

#### 3.1 Ontbrekende dataset

Er bestaat momenteel geen kant-en-klare, actuele dataset van activiteiten, locaties en aanbieders in gemeente Boxtel. Het verzamelen van echte data valt buiten de scope van negen weken. De projectgroep heeft besloten te werken met synthetische (zelf samengestelde) data als basis voor het proof of concept.

De langetermijnvisie van Carla, automatisch ophalen van actueel aanbod bij aanbieders, is als toekomstig uitbreidingspunt gedocumenteerd, maar wordt in dit project niet geïmplementeerd.

#### 3.2 Integratie van de gespreksmodellen

De vorige projectgroep combineerde beide gespreksmodellen tot één nieuw instrument. Carla twijfelt echter aan die aanpak: als de originele, geverifieerde modellen evolueren, wordt het onderhoud van een gecombineerd model complexer. De huidige projectgroep kiest er daarom voor om met **één van de twee modellen** te werken, zodat de implementatie beheersbaar blijft en toekomstige aanpassingen eenvoudiger door te voeren zijn.

De implementatie van het gespreksmodel in de system prompt vormt een technische uitdaging: de LLM moet het gesprek voeren volgens strikte, gestructureerde regels die leiden tot een systematische verkenning van de situatie van de gebruiker vóórdat er gematcht wordt.

#### 3.3 Keuze van het LLM en infrastructuur

De chatbot dient in het **Nederlands** te functioneren op minimaal taalniveau B1. Niet elk taalmodel is geschikt voor meertalige of Nederlandstalige toepassingen, wat nader onderzoek vereist. Vanwege het geen/beperkte budget en de beperkte looptijd wordt gekozen voor een lokale of eenvoudig te hosten oplossing, in plaats van een volledige cloudimplementatie via AWS.

De infrastructuur wordt in dit project als theoretisch stuk uitgewerkt: hoe de chatbot op schaal gehost kan worden op een productieomgeving, inclusief aandacht voor **AVG-compliance en data governance**, omdat de tool gezondheids- en persoonsgerelateerde informatie verwerkt.

#### 3.4 Gebruikersanonimiteit en privacy

Gebruikers blijven zo lang mogelijk anoniem. Pas wanneer een inwoner contact wil opnemen met een aanbieder, worden minimale persoonsgegevens (naam + e-mailadres of telefoonnummer) gevraagd. Medische gegevens worden nooit gekoppeld aan persoonsgegevens. De tool slaat wel de matchingsvariabelen op, zodat de aanbieder een beknopte samenvatting ontvangt van wat de inwoner zoekt.

#### 3.5 Onduidelijkheid over eindgebruiker en persona's

De doelgroep is breed omschreven. Om de database-inrichting en gesprekslogica te verfijnen, is het noodzakelijk om **twee tot drie concrete persona's** op te stellen van typische gebruikers. Deze dienen in afstemming met Carla geverifieerd te worden. Daarnaast is een **voorbeeldgesprek** (happy flow) gewenst dat als referentie dient voor de systeemprompt en de evaluatie van het prototype.

#### 3.6 Frontend en UX

De chatbot moet toegankelijk en begrijpelijk zijn voor een brede en digitaal niet altijd vaardige doelgroep. Hoewel UX-onderzoek naar conversational interfaces waardevol is, wordt besloten de frontend in eerste instantie buiten scope te houden. De focus ligt op een functionerende technische back-end met gesprekslogica. Indien er capaciteit is, kan UX als aanvullend onderdeel worden opgepakt.

### 4. Vorige projectgroep

Een eerdere studentengroep heeft al werk verricht aan dit project. Zij hebben een ontwerp van de gesprekslogica gemaakt en wireframes opgeleverd, maar er is **geen live werkende chatbot** getest door Carla. De vorige groep leverde losse onderdelen op zonder geïntegreerd geheel. De huidige projectgroep bouwt voort op de bestaande documentatie en de Robin vanuit zijn rol als begeleidende docent neemt contact op met de vorige studenten voor kennisoverdracht.

### 5. Samenvatting

|Aspect|Situatie|
|---|---|
|Opdrachtgever|Carla Renders, Stichting Richter Education|
|Doelgroep|Inwoners gemeente Boxtel, 15-99 jaar, focus op kwetsbare groepen|
|Taalniveau|B1 Nederlands|
|Gewenst prototype|Werkende chatbot met gestructureerde gesprekslogica en matching|
|Gespreksmodel|Positieve Gezondheid of Leefstijlroer (één van de twee)|
|Dataset|Synthetisch voor proof of concept|
|Privacy|Anoniem gebruik; persoonsgegevens alleen bij contactaanvraag|
|Infrastructuur|Theoretisch uitgewerkt, lokaal prototype|
|Frontend/UX|Buiten directe scope; eventueel aanvullend|
|Overdracht|Documentatie en keuzeonderbouwing voor volgende projectgroep|


### Bronnen

Anthropic. (2026). _Claude Sonnet 4.6_ [Large language model]. Gebruikt als AI-assistent voor het opstellen van deze probleemanalyse op basis van aangeleverde transcripties. [https://www.anthropic.com](https://www.anthropic.com)

Fontys Hogeschool ICT. (2026, 21 april). Kennismakingsgesprek AI-groep S2 [Vergaderingstranscriptie]. 

Fontys Hogeschool ICT. (2026, 23 april). AI-bot sessie [Vergaderingstranscriptie].

Stichting Richter Education. (z.d.). _Leergebied® Gezond_. Geraadpleegd op 26 april 2026, van [https://www.richter.education/](https://www.richter.education/)