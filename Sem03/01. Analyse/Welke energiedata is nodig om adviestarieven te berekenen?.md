## Algemene gegevens

|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |1.0|
|Datum huidige versie|03-10-2026|
|Referenties|Scope - Fontasya Electric.pdf versie 1.5|

## 1. Inleiding

### 1.1 Aanleiding en context
Fontasya Electric biedt huishoudens vier soorten energiecontracten aan: een flexibel contract en vastlopende contracten met een looptijd van 1, 3 of 5 jaar. Om klanten een passend en marktconform aanbod te kunnen doen, stelt het bedrijf hiervoor periodiek prijsadviezen op.

Door het plotselinge vertrek van de medewerker die deze prijsadviezen handmatig opstelde en het ontbreken van documentatie over het exacte rekenmodel is de werkwijze momenteel onbekend. Hierdoor kan Fontasya Electric op dit moment geen nieuwe tarieven afgeven. Er is binnen de organisatie wel data aanwezig, maar het is onduidelijk welke onderdelen hiervan bruikbaar of compleet zijn voor prijsmodellering. Ons is gevraagd om een gestructureerd proces, een passend rekenmodel en een nieuw prijsadvies te realiseren.

### 1.2 Aannames & Onderzoeksvraag
Voor de verdere uitwerking hanteren we de volgende uitgangspunten:

1. **Voorwaartse blik (Forward Curve):** Fontasya Electric wil zo snel mogelijk weer een onderbouwde voorwaartse blik (_forward curve_) kunnen werpen tot 5 jaar vooruit.
2. **Granulariteit op maandbasis:** De berekeningen worden op maandbasis uitgevoerd, aangezien een maand de kleinste contractperiode is binnen het aanbod.
3. **Methode-gestuurde aanpak:** We onderzoeken eerst welke berekeningsmethodieken er in de markt bestaan voor het bepalen van een forward curven n de bijbehorende databehoeften.
4. **Onderzoeksvraag:** Om tot de juiste berekeningsmethode en data-architectuur te komen, staat in deze analyse de volgende centrale vraag beschreven:
    > _Welke energiedata is nodig om adviestarieven te berekenen?_
    
### 1.3 Onderzoeksaanpak (DOT Framework)

De onderzoeksaanpak is opgebouwd volgens een top-down structuur: eerst het theoretisch/methodisch kader opstellen, daarna toetsen tegen de databeschikbaarheid. Op basis van het _DOT Framework_ ([ICT Research Methods](https://ictresearchmethods.nl/)) worden de volgende strategieën en methoden ingezet:

|**Onderzoeksstrategie**|**Methode**|**Toepassing binnen dit project**|
|---|---|---|
|**Library**|_Literature Study_ / _Available Product Analysis_|Onderzoeken van verschillende methodieken om een forward curve te bepalen en het in kaart brengen van de specifieke databehoefte per methode.|
|**Library**|_Data Analysis / Gap Analysis_|Na het vaststellen van de mogelijke methodes: de beschikbare interne (en externe) data analyseren en vergelijken met de vereiste databehoeften om te bepalen welke methode haalbaar en realistisch is.|
|**Showroom / Lab**|_Data Exploration_ / _Prototyping_|Het testen en valideren van de gekozen berekeningsmethode met de beschikbare dataset om te controleren of dit leidt tot logische en verantwoorde maandelijkse adviestarieven tot 5 jaar vooruit.|
|**Workshop**|_Data Modelling_ / _IT Architecture Sketching_|Het modelleren van het uiteindelijke datamodel en de verwerkingsketen op basis van de geselecteerde methode en de daadwerkelijk beschikbare databronnen.|

## 2. Methodieken voor Forward Curve Bepaling

### 2.1 Methode 1: Basis-indexering / Historische trendextrapolatie (Eenvoudig)

- **Beschrijving:** Het doortrekken van historische gemiddelden met een vaste opslag.
- **Voor- en nadelen:** Eenvoudig uit te voeren, maar houdt geen rekening met seizoensinvloeden en actuele groothandelsmarkten.
- **Databehoefte:** Historische afrekeningen, basistarief en inflatie-index.

### 2.2 Methode 2: Marktgebaseerde Forward Curve (Gemiddeld)
- **Beschrijving:** Bij deze methode wordt de basisdata van Methode 1 aangevuld met openbaar toegankelijke markt- en sectordata voor stroom en gas om de prijsontwikkeling per maand tot 5 jaar vooruit te schatten.
    
- **Voor- en nadelen:**
    - _Voordelen:_ Levert een marktconforme, actuele en objectieve voorwaartse blik op die aansluit bij de werkelijke inkooprisico's in de energiesector.
    - _Nadelen:_ Afhankelijk van de beschikbaarheid, actualiteit en verwerkingscomplexiteit van openbare marktdatastromen.
        
- **Databehoefte:**
    - **Interne basisdata:** Historische tarieven en geaggregeerd klantverbruik.
    - **Open markt- en sectordata:** Openbare tarieven van termijncontracten (stroom/gas) en landelijke standaardverbruiksprofielen.
    - **Onderzoekspunt t.a.v. databeschikbaarheid:** Welke openbare marktdata en profielen zijn kosteloos beschikbaar om dit zonder budget te realiseren?

#### 2.3 Methode 3: Profiel- en Risicogewogen Modellering (Geavanceerd)
- **Beschrijving:** Bij deze methode wordt Methode 2 verder uitgebreid door marktdata te combineren met gedetailleerde verbruiksprofielen op uurniveau en eventuele risico-opslagen.
    
- **Voor- en nadelen:**
    - _Voordelen:_ Zorgt voor de meest nauwkeurige en risico-afgedekte voorwaartse blik op de prijsontwikkeling per maand.
    - _Nadelen:_ Zeer complex om op te stellen en te onderhouden, en vereist een hoge mate van datagranulariteit en -kwaliteit.
        
- **Databehoefte:**
    - **Basisdata uit Methode 2:** Marktdata van termijncontracten en algemene verbruiksprofielen.
    - **Gedetailleerde profiel- en risicodata:** Uur- en meetdata op klantniveau, historische onbalansdata, klimaatgegevens en gedetailleerde risicomarges.
    - **Onderzoekspunt t.a.v. databeschikbaarheid:** In hoeverre is de benodigde hoge resolutie aan interne meetdata en externe risicoparameters gratis of binnen de organisatie beschikbaar?

### 2.4 Conclusie & Advies
Via Literatuuronderzoek en het vergelijken van bestaande methodes hebben we gekeken hoe de drie manieren om een prijsadvies te berekenen in elkaar zitten en welke data ze nodig hebben.

Hieruit bleek dat de methodes niet los van elkaar staan. Je kunt ze beter zien als een trap met drie treden:

- **Trede 1 (Eenvoudig):** Zorgt voor de basisinrichting en de eerste snelle prijsadviezen.
- **Trede 2 (Gemiddeld):** Gebruikt die basis en voegt daar actuele marktdata aan toe.
- **Trede 3 (Geavanceerd):** Bouwt weer voort op die marktdata en voegt daar gedetailleerde risico- en profielcijfers aan toe.
    
Omdat elke stap de bouwsteen is voor de volgende, kun je stap 2 of 3 simpelweg niet zetten zonder bij stap 1 te beginnen. Het advies om eerst met de eenvoudige methode te starten en daarna stapsgewijs uit te breiden, is dan ook een hele logische uitkomst van dit onderzoek.

## 3. Opbouw van de Energieprijs
Om te bepalen welke data er exact nodig is voor het berekenen van het adviestarief, moet eerst helder zijn hoe een energietarief (de uiteindelijke consumentenprijs) is opgebouwd. Een adviestarief voor een contract is namelijk opgebouwd uit verschillende vaste en variabele componenten.

### 3.1 Leveringskosten
- **Inkoopprijs** De basisprijs voor elketriciteit en gas die wordt ingekocht
- **Volumerisico** Opslag voor het risico dat een klant meer of minder verbruikt dan vooraf is ingekocht. Denk hierbij aan een strenge of zachte winter.
- **Groencertificaten** Als Fontasya Electric groene stroom wilt leveren, moet het groene stroom certificaten of co2 compensatie kopen.
- **Profielrisico (_Profilingskosten_):** Ontstaat wanneer een leverancier energie inkoopt via een _Baseload-contract_ (een vlak profiel waarbij $24/7$ een constant vermogen wordt geleverd, zoals $1\text{ MW}$). Kleinverbruikers hebben echter een seizoensgebonden verbruikspatroon.

	- **Zomer:** De klant verbruikt minder (bijv. $0{,}5\text{ MW}$). De leverancier heeft $0{,}5\text{ MW}$ overschot en moet dit op de markt verkopen tegen vaak lage zomerprijzen.
	- **Winter:** De klant verbruikt meer (bijv. $1{,}5\text{ MW}$). De leverancier komt $0{,}5\text{ MW}$ tekort en moet dit bijkopen op de markt tegen vaak hoge winterprijzen.

	>Het financiële nadeel van dit "goedkoop verkopen in de zomer en duur bijkopen in de winter" vormt het **profielrisico**, wat wordt afgedekt met een profielrisico-opslag.
- **Vormrisico (_Shape risk_):** Ontstaat wanneer een leverancier energie inkoopt via een _Baseload-contract_ (vlak $24/7$-profiel) of daggebaseerde contracten, terwijl het klantverbruik sterk wisselt per uur van de dag.

	- **Nacht (02:00 uur):** De klant slaapt en verbruikt nauwelijks stroom (bijv. $0{,}3\text{ MW}$). De leverancier heeft een overschot van $0{,}7\text{ MW}$ en moet dit op de spotmarkt verkopen tegen lage (of soms zelfs negatieve) nachtprijzen.
	- **Avondpiek (18:00 - 20:00 uur):** De klant kookt, kijkt tv en laadt de auto op (bijv. $1{,}8\text{ MW}$). De leverancier komt $0{,}8\text{ MW}$ tekort en moet dit op de spotmarkt bijkopen op het duurste moment van de dag.
    
	>Het financiële nadeel van het "goedkoop verkopen 's nachts en duur bijkopen tijdens de piekuren 's avonds" vormt het **vormrisico**, wat wordt afgedekt met een vormrisico-opslag.
- **Onbalanskosten:** Ontstaan wanneer de totale werkelijke afname van alle klanten van Fontasya Electric op een specifiek moment afwijkt van wat er vooraf bij de landelijke netbeheerder is ingekocht en voorspeld.

	>De landelijke netbeheerder, TenneT, moet het elektriciteitsnet elke seconde op exact 50 Hz balanceren. De kosten die TenneT maakt om deze acute afwijkingen op te lossen, worden achteraf als onbalansboetes/verrekeningen doorbelast aan de leverancier. Om dit onvoorspelbare risico op te vangen, wordt er een onbalans-opslag per kWh/m³ in het tarief verwerkt. 
- **Bruto Opslag / Leveranciersmarge:** Het vaste of procentuele bedrag per kWh/m³ (en/of per maand) dat boven op alle kale inkoopkosten, risico-opslagen en wettelijke verplichtingen wordt geteld ter dekking van de eigen bedrijfsvoering en het behalen van rendement.

	- **Dekking operationele kosten:** De marge dient voor het financieren van interne processen, zoals facturatie, klantenservice, ICT-infrastructuur, personeelskosten en marketing.
	- **Winst- / Rendementsdoelstelling:** Het nettorendement dat Fontasya Electric wil behalen op de verkoop van energie en contracten.
	- **Debiteurenrisico / Wanbetalersopslag:** Een klein onderdeel van de marge om het risico af te dekken dat individuele klanten hun energierekening niet kunnen of willen betalen.

### 3.2 Netbeheerkosten
- **Vaste Netbeheerkosten (per maand of per jaar)**
	- **Periodiek Aansluittarief:** Kosten voor de instandhouding van de fysieke aansluiting op het netwerk.
	- **Capaciteitstarief (Transporttarief):** Vaste kosten afhankelijk van de grootte van de aansluiting (bijv. $3 \times 25\text{A}$ voor stroom of $\text{G4/G6}$ voor gas).
	- **Meterserie- / Meettarief:** Kosten voor de huur en het beheer van de (slimme) meter.

### 3.3 Overheidsheffingen & Belastingen
Statische tarieven die door de Rijksoverheid worden bepaald en afgedragen worden aan de Belastingdienst.

1. **Variabele Overheidsheffingen (per kWh of m³)**
    - **Energiebelasting:** Gestaffelde belasting per kWh stroom en m³ gas (inclusief eventuele reductiezones voor schijf 1 kleinverbruik).
2. **Vaste Overheidsheffingen**
    - **Vermindering Energiebelasting:** Een vast jaarlijks belastingkrediet (heffingskorting) per elektriciteitsaansluiting met een verblijfsfunctie.
3. **Omzetbelasting (Btw)**
    - **Btw-tarief (21%):** Wordt berekend over de som van <u>**alle**</u> bovenstaande componenten

## Hoofdstuk 4: Energiedata-vereisten per Berekeningsmethode
In dit hoofdstuk analyseer je per methode welke specifieke energiedata noodzakelijk is om tot adviestarieven te komen.

### 4.1 Methode 1: Forward Curve op basis van Historische Data

- **Toelichting Werking Methode 1:** Voor deze methode pakken we de historische data van Fontasya Electric
    
- **Te berekenen Prijscomponenten:** Welke onderdelen van het adviestarief worden via deze methode berekend (bijv. basistarief, profielopslag, piek/dal-verhouding, onbalansdekking)?
    
- **Vereiste Energiedata:**
    
    - **Prijselementen:** Welke historische marktprijzen zijn nodig (bijv. EPEX/EEX spotprijzen, historische settlementprijzen)?
        
    - **Volume- & Profieldata:** Welke historische verbruiksgegevens, standaardjaarverbruiken (SJV) of profielcurves (e.g. Nedu-profielen) zijn vereist?
        
    - **Frequentie & Historie:** Welke tijdsresolutie (bijv. uurwaarden vs. dagwaarden) en welke historische periode (bijv. afgelopen 1, 2 of 3 jaar) is minimaal nodig?
        

### 4.3 [Eventueel] Methode 2: [Bijv. Marktgebaseerde / Dynamische / Termijnmarkt Methode]

_(Indien van toepassing op dezelfde manier uitwerken)_

- **Toelichting Werking Methode:** Korte uitleg van de alternatieve/aanvullende methode.
    
- **Te berekenen Prijscomponenten:** Specifieke tariefcomponenten behorend bij deze methode.
    
- **Vereiste Energiedata:** Welke specifieke data (zoals futures, beurskoersen, dynamische indices) hier voor nodig is.
    

### 4.4 Vergelijking & Datagaps (Gegevensbeschikbaarheid)

- **Vergelijking Data-behoefte:** Verschillen in databehoefte, complexiteit en verversingsfrequentie tussen de methoden.
    
- **Knelpunten & Datakwaliteit:** Welke benodigde energiedata is makkelijk ontsluitbaar en waar zitten eventuele ontbrekende gegevens of kwaliteitsrisico's?
    

## Hoofdstuk 5: Conclusie & Advies (Beantwoording Hoofdvraag)

### 5.1 Inleiding

- **Doel:** Het geven van het definitieve antwoord op de hoofdvraag en het presenteren van de benodigde datacatalogus voor adviestarieven.
    

### 5.2 Conclusie: Totale Energiedata-behoefte voor Adviestarieven

- **Beantwoording Hoofdvraag:** Een direct en helder antwoord op de vraag welke energiedata precies nodig is om adviestarieven te berekenen.
    
- **Definitief Data-overzicht (Data Matrix):** Een overzichtelijke tabel/matrix die per prijscomponent en per methode samenvat:
    
    - Welke specifieke databron/variabele nodig is
        
    - De vereiste granulariteit (bijv. per uur, per dag, per maand)
        
    - De benodigde historie/frequentie
        

### 5.3 Advies voor Data-ontsluiting & Inrichting

- **Advies voor Implementatie:** Welke databronnen prioriteit moeten krijgen om de berekening van de adviestarieven (te beginnen met Methode 1) operationeel te maken.
    
- **Aanbevelingen Datakwaliteit & Automatisering:** Hoe de benodigde energiedata betrouwbaar verwerkt en bijgehouden kan worden.
## Bronnen
https://www.acm.nl/nl/energie op 03-10-2026