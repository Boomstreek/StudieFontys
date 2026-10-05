## Algemene gegevens

|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |0.1|
|Datum huidige versie|05-10-2026|
|Referenties|Scope - Fontasya Electric.pdf versie 1.5|

## 1. Inleiding

### 1.1 Aanleiding en context
Fontasya Electric biedt huishoudens vier soorten energiecontracten aan: een flexibel contract en vastlopende contracten met een looptijd van 1, 3 of 5 jaar. Om klanten een passend en marktconform aanbod te kunnen doen, stelt het bedrijf hiervoor periodiek prijsadviezen op.

Door het plotselinge vertrek van de medewerker die deze prijsadviezen handmatig opstelde en het ontbreken van documentatie over het exacte rekenmodel is de werkwijze momenteel onbekend. Hierdoor kan Fontasya Electric op dit moment geen nieuwe tarieven afgeven. Er is binnen de organisatie wel data aanwezig, maar het is onduidelijk welke onderdelen hiervan bruikbaar of compleet zijn voor prijsmodellering. Ons is gevraagd om een gestructureerd proces, een passend rekenmodel en een nieuw prijsadvies te realiseren. 

Bij het opstellen van dit document is gebruikgemaakt van generatieve AI (Anthropic, 2026; Google, 2026); zie bijlage B.

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

### 2.3 Methode 3: Profiel- en Risicogewogen Modellering (Geavanceerd)
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
- **L1 Inkoopprijs** De basisprijs voor elketriciteit en gas die wordt ingekocht
- **L2 Volumerisico** Opslag voor het risico dat een klant meer of minder verbruikt dan vooraf is ingekocht. Denk hierbij aan een strenge of zachte winter.
- **L3 Groencertificaten** Als Fontasya Electric groene stroom wilt leveren, moet het groene stroom certificaten of co2 compensatie kopen.
- **L4 Profielrisico (_Profilingskosten_):** Ontstaat wanneer een leverancier energie inkoopt via een _Baseload-contract_ (een vlak profiel waarbij $24/7$ een constant vermogen wordt geleverd, zoals $1\text{ MW}$). Kleinverbruikers hebben echter een seizoensgebonden verbruikspatroon.

	- **Zomer:** De klant verbruikt minder (bijv. $0{,}5\text{ MW}$). De leverancier heeft $0{,}5\text{ MW}$ overschot en moet dit op de markt verkopen tegen vaak lage zomerprijzen.
	- **Winter:** De klant verbruikt meer (bijv. $1{,}5\text{ MW}$). De leverancier komt $0{,}5\text{ MW}$ tekort en moet dit bijkopen op de markt tegen vaak hoge winterprijzen.

	>Het financiële nadeel van dit "goedkoop verkopen in de zomer en duur bijkopen in de winter" vormt het **profielrisico**, wat wordt afgedekt met een profielrisico-opslag.
- **L5 Vormrisico (_Shape risk_):** Ontstaat wanneer een leverancier energie inkoopt via een _Baseload-contract_ (vlak $24/7$-profiel) of daggebaseerde contracten, terwijl het klantverbruik sterk wisselt per uur van de dag.

	- **Nacht (02:00 uur):** De klant slaapt en verbruikt nauwelijks stroom (bijv. $0{,}3\text{ MW}$). De leverancier heeft een overschot van $0{,}7\text{ MW}$ en moet dit op de spotmarkt verkopen tegen lage (of soms zelfs negatieve) nachtprijzen.
	- **Avondpiek (18:00 - 20:00 uur):** De klant kookt, kijkt tv en laadt de auto op (bijv. $1{,}8\text{ MW}$). De leverancier komt $0{,}8\text{ MW}$ tekort en moet dit op de spotmarkt bijkopen op het duurste moment van de dag.
    
	>Het financiële nadeel van het "goedkoop verkopen 's nachts en duur bijkopen tijdens de piekuren 's avonds" vormt het **vormrisico**, wat wordt afgedekt met een vormrisico-opslag.
- **L6 Onbalanskosten:** Ontstaan wanneer de totale werkelijke afname van alle klanten van Fontasya Electric op een specifiek moment afwijkt van wat er vooraf bij de landelijke netbeheerder is ingekocht en voorspeld.

	>De landelijke netbeheerder, TenneT, moet het elektriciteitsnet elke seconde op exact 50 Hz balanceren. De kosten die TenneT maakt om deze acute afwijkingen op te lossen, worden achteraf als onbalansboetes/verrekeningen doorbelast aan de leverancier. Om dit onvoorspelbare risico op te vangen, wordt er een onbalans-opslag per kWh/m³ in het tarief verwerkt. 
- **L7 Bruto Opslag / Leveranciersmarge / Vaste leveringskosten:** Het vaste of procentuele bedrag per kWh/m³ (en/of per maand/jaar) dat boven op alle kale inkoopkosten, risico-opslagen en wettelijke verplichtingen wordt geteld ter dekking van de eigen bedrijfsvoering en het behalen van rendement.

	- **Dekking operationele kosten:** De marge dient voor het financieren van interne processen, zoals facturatie, klantenservice, ICT-infrastructuur, personeelskosten en marketing.
	- **Winst- / Rendementsdoelstelling:** Het nettorendement dat Fontasya Electric wil behalen op de verkoop van energie en contracten.
	- **Debiteurenrisico / Wanbetalersopslag:** Een klein onderdeel van de marge om het risico af te dekken dat individuele klanten hun energierekening niet kunnen of willen betalen.
- **L8 Terugleverkosten:** kosten of vergoedingen voor teruggeleverde stroom. 

### 3.2 Netbeheerkosten
- **N1 Vaste Netbeheerkosten (per maand of per jaar)**
	- **Periodiek Aansluittarief:** Kosten voor de instandhouding van de fysieke aansluiting op het netwerk.
	- **Capaciteitstarief (Transporttarief):** Vaste kosten afhankelijk van de grootte van de aansluiting (bijv. $3 \times 25\text{A}$ voor stroom of $\text{G4/G6}$ voor gas).
	- **Meterserie- / Meettarief:** Kosten voor de huur en het beheer van de (slimme) meter.

### 3.3 Overheidsheffingen & Belastingen
Statische tarieven die door de Rijksoverheid worden bepaald en afgedragen worden aan de Belastingdienst.

- **O1 Variabele Overheidsheffingen (per kWh of m³)**
    - **Energiebelasting:** Gestaffelde belasting per kWh stroom en m³ gas (inclusief eventuele reductiezones voor schijf 1 kleinverbruik).
- **O2 Vaste Overheidsheffingen**
    - **Vermindering Energiebelasting:** Een vast jaarlijks belastingkrediet (heffingskorting) per elektriciteitsaansluiting met een verblijfsfunctie.
- **O3 Omzetbelasting (Btw)**
    - **Btw-tarief (21%):** Wordt berekend over de som van <u>**alle**</u> bovenstaande componenten

## Hoofdstuk 4: Energiedata-vereisten per Berekeningsmethode
Dit hoofdstuk beantwoordt de onderzoeksvraag uit: _welke energiedata is nodig om adviestarieven te berekenen?_ Per methode uit hoofdstuk 2 (trede 1 t/m 3) wordt bepaald hoe elke prijscomponent uit hoofdstuk 3 (L1 t/m O3) wordt doorgerekend en welke data daarvoor nodig is. Het uitgangspunt blijft een maandelijkse forward curve tot 5 jaar vooruit, voor stroom en gas, voor de vier contractvormen (flexibel, 1, 3 en 5 jaar).

### 4.1 Uitgangspunten
**Wie bepaalt de component?**

|**Component**|**Bepaald door**|**Hoe rekenen we door?**|
|---|---|---|
|L1 t/m L8|Markt en Fontasya|Afhankelijk van de methode|
|N1|Netbeheerders (tarieven ACM)|Geen CPI, aanname|
|O1 t/m O3|Rijksoverheid|Geen CPI, aanname|

**Aannames voor alle methodes**

1. N1 en O1 t/m O3 zijn voor jaar 2 t/m 5 niet bekend. We gaan uit van gelijkblijvende tarieven.
2. Stroom en gas krijgen aparte tarieven, profielen en curves, omdat gas veel sterker seizoensgebonden is.
3. L7 bestaat uit een vast deel (per aansluiting per maand) en een variabel deel (per kWh/m³). Alleen het variabele deel volgt het verbruiksprofiel.

### 4.2 Methode 1: Basis-indexering (Eenvoudig)

**Werkwijze.** Het historische klanttarief per commodity is het vertrekpunt. L7 (en het basistarief) wordt met een inflatie-index (CPI) doorgetrokken. N1 en O1 t/m O3 worden volgens de aannames toegevoegd. Over het totaal komt btw (O3).

**Benodigde data**

- Historische afrekeningen en tarieven per contractvorm en commodity (L1 zit hierin; een aparte kale inkoopprijs is waarschijnlijk niet vastgelegd)
- Historische opbouw van L7 in vast en variabel deel (anders wordt L7 als geheel geïndexeerd)
- CPI, alleen voor de eigen componenten (niet voor N1 en O1 t/m O3)
- Actuele N1-tarieven per aansluittype en O1 t/m O3
- Geaggregeerd jaarverbruik (kWh en m³)

**Niet nodig:** termijnprijzen, standaardprofielen, uur- en kwartierdata, onbalans- en klimaatdata. De risico's L2, L4, L5 en L6 zitten geaggregeerd in het historische tarief.

**Beperkingen**

- Geen echte maandcurve: een vlakke lijn met jaarlijkse CPI-stappen (jaarverbruik in 12 gelijke delen).
- Weinig onderscheid tussen contractvormen (alleen via historische tarieven per contractvorm).
- Gevoelig voor de gekozen referentieperiode (bijv. 2022). Dit toetsen we in de gap-analyse.
- Geen marktinformatie.

### 4.3 Methode 2: Marktgebaseerde Forward Curve (Gemiddeld)

**Wat verandert er t.o.v. Methode 1?**

- **L1:** termijnprijzen vervangen de historische inkoopprijs. Historie dient alleen nog voor controle.
- **Verbruik:** landelijke standaardprofielen vervangen de gelijke jaarverdeling. Dit raakt het variabele deel van L7, niet het vaste deel.
- **L4:** het verwachte profieleffect wordt berekend per maand (verbruiksgewogen versus vlak gemiddelde).
- **Contractvormen:** een vast contract is het gemiddelde van de termijnprijzen over de looptijd plus een risico-opslag. Het flexibele contract volgt de korte termijn.

**Extra data**

- Termijnprijzen stroom en gas (per maand, kwartaal, seizoen of jaar)
- Landelijke standaardverbruiksprofielen, apart voor stroom en gas
- Actuele prijs van groencertificaten (L3)

**Nog niet nodig:** uur- en kwartierdata, berekend vorm-, onbalans- en volumerisico (L2, L5 en L6 blijven een vaste inschatting), klimaatdata.

**Beperkingen en onderzoekspunten**

- **Horizon:** liquide termijnproducten lopen vaak minder ver dan 5 jaar, dus extrapolatie is nodig.
- **Granulariteit:** termijnprijzen zijn vaak per kwartaal of jaar. De verdeling naar maanden gaat via het standaardprofiel.
- **Kosteloze beschikbaarheid** van termijnprijzen en profielen (wordt beantwoord in de gap-analyse).
- Het restrisico (afwijkende winters) blijft een vaste inschatting.

### 4.4 Methode 3: Profiel- en Risicogewogen Modellering (Geavanceerd)

**Wat verandert er t.o.v. Methode 2?** De risico's worden per component berekend in plaats van geschat:

- **L4:** klantspecifiek profiel uit slimme-meterdata in plaats van landelijke profielen.
- **L5:** berekend op uurniveau (nacht versus avondpiek).
- **L6:** berekend uit onbalansprijzen en voorspelfouten.
- **L2:** berekend met klimaatdata (strenge of zachte winter).
- **L7:** het vaste deel blijft een kostprijsberekening. Het variabele deel (rendement en debiteurenrisico) wordt risicogewogen.

**Extra data**

|**Categorie**|**Data**|**Voor**|
|---|---|---|
|Meetdata|Uur-/kwartierdata per klant of segment|L4, L5|
|Spotmarkt|Historische day-ahead/spotprijzen per uur|L5|
|Onbalans|Onbalansprijzen en -volumes (TenneT), eigen voorspelfouten|L6|
|Klimaat|Temperatuur, graaddagen (bijv. KNMI)|L2|
|Risico|Prijsvolatiliteit, wanbetalingscijfers, bedrijfskosten per aansluiting, rendementsdoel|L7|

**Eisen en onderzoekspunt:** uur-/kwartierwaarden over voldoende jaren, zonder gaten, en AVG-proof (aggregatie of toestemming).

### 4.5 Overzicht per component

|**Component**|**Methode 1**|**Methode 2**|**Methode 3**|
|---|---|---|---|
|L1 Inkoopprijs|Historisch klanttarief|Termijnprijzen|Termijnprijzen|
|L2 Volumerisico|Geaggregeerd|Vaste inschatting|Berekend (klimaat)|
|L3 Groencertificaten|In tarief|Vaste opslag|Berekend|
|L4 Profielrisico|Geaggregeerd|Berekend (standaardprofiel)|Berekend (klantprofiel)|
|L5 Vormrisico|Geaggregeerd|Vaste inschatting|Berekend (uurniveau)|
|L6 Onbalanskosten|Geaggregeerd|Vaste inschatting|Berekend|
|L7 Bruto opslag|Historisch, CPI (vast + variabel)|Vast + variabel (maandprofiel), CPI|Vast: kostprijs; variabel: risicogewogen|
|L8 Terugleverkosten|Aanname|Aanname|Aanname|
|N1 Netbeheerkosten|Aanname|Aanname|Aanname|
|O1 t/m O3 Heffingen en btw|Aanname|Aanname|Aanname|
|Contractvormen onderscheiden|Beperkt|Via termijnprijzen|Via termijnprijzen en risico|
|Echte maandcurve|Nee|Ja|Ja|

### 4.6 Conclusie

- **Methode 1** heeft alleen interne historische tarieven, publieke tarieven en CPI nodig. Ze is snel te realiseren, maar geeft geen echte maandcurve.
- **Methode 2** voegt termijnprijzen en standaardprofielen toe. Pas hier ontstaan een maandcurve en onderscheid per looptijd. Haalbaarheid hangt af van de horizon en gratis beschikbaarheid.
- **Methode 3** vraagt daarbovenop meet-, spot-, onbalans- en klimaatdata. Ze is het nauwkeurigst, maar ook het meest data-intensief.

De benodigde data groeit dus mee per trede. De gap-analyse toetst dit aan de data die Fontasya heeft.

## 5: Conclusie en vervolgstap

### 5.1 Antwoord op de onderzoeksvraag

_Welke energiedata is nodig om adviestarieven te berekenen?_ De benodigde data groeit per trede mee :

|**Trede**|**Benodigde data**|**Resultaat**|
|---|---|---|
|**1. Basis-indexering**|Historische afrekeningen en tarieven per contractvorm en commodity, opbouw van L7 (vast en variabel), CPI, N1-tarieven, O1 t/m O3, geaggregeerd jaarverbruik|Snel advies, maar vlakke curve|
|**2. Marktgebaseerd**|Trede 1, plus termijnprijzen stroom en gas, landelijke standaardverbruiksprofielen en prijzen voor groencertificaten (L3)|Echte maandcurve en onderscheid per looptijd|
|**3. Profiel- en risicogewogen**|Trede 2, plus uur-/kwartierdata per klant of segment, spot- en onbalansprijzen, klimaatdata en risicoparameters|Nauwkeurigste, risicogewogen curve|

Voor N1 en O1 t/m O3 is in alle treden een aanname nodig (gelijkblijvende tarieven), omdat die door de ACM en de Rijksoverheid worden vastgesteld.

### 5.2 Datachecklist voor de gap-analyse

Uit hoofdstuk 4 volgen de datavragen die in de gap-analyse worden getoetst:

|**Nr.**|**Datavraag**|**Trede**|**Componenten**|
|---|---|---|---|
|1|Zijn er historische afrekeningen en tarieven per contractvorm en commodity, en over hoeveel jaar? Welke periode is representatief (bijv. rond 2022)?|1|L1|
|2|Is L7 in de historische tarieven te splitsen in een vast en variabel deel?|1|L7|
|3|Is het jaarverbruik per klant of klantgroep beschikbaar?|1, 2|alle|
|4|Welke aannames voor N1 en O1 t/m O3 zijn vastgelegd en bij welke bron?|1, 2, 3|N1, O1 t/m O3|
|5|Welke termijnprijzen zijn gratis beschikbaar, tot welke horizon en met welke granulariteit?|2|L1|
|6|Welke landelijke standaardverbruiksprofielen zijn gratis beschikbaar, apart voor stroom en gas?|2|L4|
|7|Welke prijzen voor groencertificaten (L3) zijn beschikbaar?|2|L3|
|8|Is er uur- of kwartierdata (slimme meter) en is gebruik toegestaan (AVG)?|3|L4, L5|
|9|Zijn er onbalans- en spotprijzen, en eigen voorspelfouten?|3|L5, L6|
|10|Zijn er klimaatdata en historisch verbruik om L2 te berekenen?|3|L2|
|11|Zijn er bedrijfskosten per aansluiting, wanbetalingscijfers en een rendementsdoel?|3|L7|

### 5.3 Conclusie en vervolgstap
De methodes vormen een trap: elke trede bouwt voort op de vorige. Het voorlopige advies is daarom te starten met Methode 1 en stapsgewijs uit te breiden naar Methode 2 en 3.

De vervolgstap is de gap-analyse, die in een apart document volgt. Daarin wordt de checklist uit §5.2 getoetst aan de data die Fontasya Electric heeft. Zo wordt bepaald tot welke trede het rekenmodel nu haalbaar is.

## Bijlage A: Bronnen
Anthropic. (2026). _Claude_ (Claude Sonnet 5.5) [Groot taalmodel]. [https://claude.ai](https://claude.ai)

Autoriteit Consument en Markt. (2025, 27 november). _ACM stelt tarieven 2026 regionale netbeheerders en TenneT vast_. [https://www.acm.nl/nl/node/28517](https://www.acm.nl/nl/node/28517)

Belastingdienst. (z.d.). _Energiebelasting_. Geraadpleegd op 5 oktober 2026, van [https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/overige_belastingen/belastingen_op_milieugrondslag/energiebelasting](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/overige_belastingen/belastingen_op_milieugrondslag/energiebelasting)

Fontasya Electric. (2026). _Scope - Fontasya Electric_ (Versie 1.5) [Ongepubliceerd document].

Google. (2026). _Gemini_ (Modelversie van oktober 2026) [Groot taalmodel]. [https://gemini.google.com](https://gemini.google.com)

ICE Endex. (z.d.). _Dutch TTF natural gas futures_. Geraadpleegd op 5 oktober 2026, van [https://www.ice.com/products/27996665/Dutch-TTF-Gas-Futures](https://www.ice.com/products/27996665/Dutch-TTF-Gas-Futures)

ICT Research Methods. (z.d.). _ICT research methods_. Geraadpleegd op 3 oktober 2026, van [https://ictresearchmethods.nl/](https://ictresearchmethods.nl/)

Rijksoverheid. (z.d.). _Opbouw energierekening_. Geraadpleegd op 3 oktober 2026, van [https://www.rijksoverheid.nl/onderwerpen/energie-thuis/vraag-en-antwoord/opbouw-energierekening](https://www.rijksoverheid.nl/onderwerpen/energie-thuis/vraag-en-antwoord/opbouw-energierekening)

TenneT. (z.d.-a). _Balancing markets_. Geraadpleegd op 3 oktober 2026, van [https://www.tennet.eu/nl-en/markets/dutch-market/balancing-markets](https://www.tennet.eu/nl-en/markets/dutch-market/balancing-markets)

TenneT. (z.d.-b). _Settlement prices_. Geraadpleegd op 3 oktober 2026, van [https://www.tennet.eu/nl-en/node/1645/](https://www.tennet.eu/nl-en/node/1645/)

## Bijlage B: AI-verantwoording

**Gebruikte AI-tools.** Bij dit onderzoek zijn twee generatieve AI-tools gebruikt: Claude (Anthropic, 2026) en Gemini (Google, 2026). Beide zijn ingezet als sparringpartner en voor redactionele ondersteuning. De inhoudelijke keuzes, de eindredactie en de verantwoordelijkheid voor dit document liggen bij de auteur.
 
|**Onderdeel**|**Tool**|**Aard van de ondersteuning**|**Rol van de auteur**|
|---|---|---|---|
|Methodes en databehoefte (hoofdstuk 2)|Gemini|Structureren van de drie methodes en hun databehoefte|Selectie van de methodes en toetsing aan de context van Fontasya Electric|
|Opbouw van de energieprijs (hoofdstuk 3)|Gemini|Structureren van de prijscomponenten|Inhoudelijke controle, eigen definities en nummering (L1 t/m O3)|
|Databehoefte per methode (hoofdstuk 4)|Claude|Herschrijven en compacter maken, kritische review van de logica, voorstel voor de opzet per component|Beoordeling van de voorstellen, schrappen of overnemen van punten (bijv. de aanname over de energiebelasting is geschrapt)|
|Conclusie en datachecklist (hoofdstuk 5)|Claude|Opzet van de conclusie en de datachecklist|Eindredactie en controle op relevantie voor de gap-analyse|
|Taal en bronnenlijst|Claude|Controle op spelling en grammatica, opmaak van de bronnen in APA-stijl|Controle van de bronnen en de raadpleegdata|
 
**Controle.** Alle door AI gegenereerde teksten en rekenregels zijn door de auteur beoordeeld en waar nodig aangepast. Feiten over wet- en regelgeving en tarieven zijn gecontroleerd bij de primaire bronnen (zie Bronnen). Er zijn geen persoonsgegevens van klanten of vertrouwelijke bedrijfsdata met de tools gedeeld.