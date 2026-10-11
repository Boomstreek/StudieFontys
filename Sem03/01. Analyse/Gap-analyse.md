# Gap-analyse: is trede 1 (basisindexering) mogelijk met de data van Fontasya Electric?

## Algemene gegevens
### Metadata
| | |
|---|---|
| Naam student | Bram Wieringa |
| Versienummer | 0.1 |
| Datum huidige versie | |
| Referenties | Scope - Fontasya Electric.pdf v1.5; Welke energiedata is nodig om adviestarieven te berekenen? v0.1; Fontys (e-mail R. van der Veen, 17-09-2026) |

## 1. Inleiding

### 1.1 Aanleiding en context
In het kort, momenteel zijn er geen nieuwe tarieven mogelijk, advies uit vorig document is om te starten met Methode 1. Bij het opstellen van dit document is gebruikgemaakt van generatieve AI (Anthropic, 2026); zie bijlage B.

### 1.2 Onderzoeksvraag
- Hoofdvraag: *Welke van de benodigde data is beschikbaar, en is trede 1 op dit moment mogelijk?*
- Deelvragen:
  1. Welke data heeft Fontasya Electric voor trede 1 en hoe bruikbaar is die?
  2. Welke data ontbreekt en hoe is dat op te lossen (aanname, extern, opvragen)?
  3. Is trede 1 daarmee haalbaar, en onder welke voorwaarden?
  
### 1.3 Afbakening
- Toetsing van datavragen 1 t/m 4 (trede 1)
- Stroom en gas apart, vier contractvormen (flexibel, 1, 3, 5 jaar)
- Trede 2 en 3 worden niet getoetst

### 1.4 Onderzoeksaanpak (DOT Framework)
- Library / Data Analysis (Gap Analysis)
- Vervolg: Showroom / Lab (prototype trede 1)

## 2. Werkwijze
### 2.1 Bronnen
- Interne data: export/bestanden van Fontasya
- Externe data: ACM (N1), Belastingdienst/Rijksoverheid (O1 t/m O3), CBS (CPI)

### 2.2 Beoordelingscriteria per dataset
| Criterium | Vraag |
|---|---|
| Aanwezigheid | Bestaat de data? |
| Volledigheid | Zitten er gaten in? |
| Historie | Over hoeveel jaar? Is de periode representatief (bijv. 2022)? |
| Granulariteit | Per contractvorm en commodity? Per maand of per jaar? |
| Actualiteit | Hoe recent is het laatste tarief? |
| Toegankelijkheid | Format, gratis? |

### 2.3 Scoring
- 🟢 Beschikbaar en bruikbaar
- 🟡 Gedeeltelijk, bruikbaar met aanname
- 🔴 Ontbreekt of onbruikbaar
- ⚪ Nog onbekend

### 2.4 Beslisregel
- Trede 1 is haalbaar als datavraag 1 t/m 4 minimaal 🟡 scoren met onderbouwde aanname
- Eén 🔴 op een verplichte vraag = trede 1 nog niet haalbaar, met actie om dit op te lossen

## 3. Inventarisatie interne data
Alle data is synthetisch en komt uit de generator van Fontys (e-mail R. van der Veen, 17-09-2026). Het is gegenereerd als testset met 500 klanten; de volledige generator levert 30.000 huishoudens.

|   |   |   |   |
|---|---|---|---|
|Tabel|Wat staat erin|Periode|Aantal rijen|
|stg_customers|Kenmerken van de klant: klantsoort, regio, wel of geen zonnepanelen, jaardoel voor verbruik|n.v.t.|500|
|stg_contracts|Eén actief contract per klant: contractvorm, start en einde, tarief stroom en gas, vaste maandvergoeding, status|start 2024-01 t/m 2025-12|500|
|stg_pv_assets|Zonnepaneel-installaties (PV) per klant|n.v.t.|222|
|stg_electricity_consumption|Stroomverbruik per klant per dag|2026|182.500|
|stg_gas_consumption|Gasverbruik per klant per dag|2026|182.500|
|stg_pv_feedin|Per dag: opwek van zonnepanelen, eigen gebruik, teruglevering en terugleverprijs|2026|81.030|
|stg_energy_balance|Energiebalans per dag: verbruik, zonnepanelen, eigen productie, inkoop|2026|365|
|stg_market_price|Marktprijzen per dag (day-ahead, intraday, onbalans, gas spot, gas forward 1 jaar)|2026|365|
|stg_network_system|Netwerk per dag: distributie, transport, verlies, balancering, congestie|2026|365|
|stg_weather_forecast|Weersverwachting per dag, met verwachte opbrengst van wind en zon|2026|365|
|stg_generation_assets|Eigen installaties voor stroomproductie (3 wind, 2 zon): vermogen, kosten, afschrijving|n.v.t.|5|
|stg_generation_production|Productie per installatie per dag, met kostprijs per MWh|2026|1.825|
|stg_procurement_trades|Inkoop per dag (eigen wind en zon, teruglevering van klanten, inkoop op de markt, gas)|2026|1.825|
|stg_portfolio|Per contractvorm: aantal klanten, jaarverbruik, gemiddelde tarieven, geschatte kans op opzeggen|n.v.t.|4|
|stg_price_recommendation|Prijsadvies per maand voor elke contractvorm (12 maanden × 4 vormen)|2026|48|
|stg_data_quality|Kwaliteitsscores per dataset, zoals de generator die zelf meldt|n.v.t.|12|

### 3.1 Datakwaliteit

**Wat goed is**

- Het verbruik is compleet. Er zijn geen dubbele, lege of negatieve waarden. Alle 500 klanten hebben voor alle 365 dagen een regel, voor stroom en gas.
- Alles hangt goed aan elkaar. Er zijn geen contracten, verbruiksregels of zonnepaneel-installaties zonder klant.
- De tabellen lijken te kloppen met elkaar. Het verbruik van alle klanten per dag is gelijk aan de energiebalans. 
- Een handelsregel is uniek door `trade_id` en `source_type` samen. `trade_id` alleen is niet genoeg, want dat nummer is per dag hetzelfde voor vijf regels.

**Wat opvalt in de nagemaakte data** (dit komt door het script, niet door Fontasya)

1. **Contractstatus.** Elke klant heeft precies één actief contract, dus alle 500 contracten staan op ACTIVE. Er zijn geen beëindigde of verlengde contracten en niemand zegt op (churn). Bij 164 van de 183 1-jaarscontracten is de einddatum al voorbij (peildatum 11-10-2026), terwijl ze nog ACTIVE zijn. Alle 183 klanten met een 1-jaarscontract hebben ook verbruik na hun einddatum (50.885 regels). 
2. **Netwerkdata.** Elke dag heeft een andere `network_id` (365 dagen, 365 id's). Distributie (40,3–43,1 €/MWh) en transport (13,3–14,9 €/MWh) veranderen elke dag. De echte netbeheertarieven staan juist een heel jaar vast. Deze tabel is daarom niet bruikbaar voor N1.
3. **Gaseenheden.** De adviesprijs voor gas is 4,1–6,0 €/m³, zeer hoog. Verschillinde eenheden in procurement trades.
	1. |Waar|Gasprijs|Oordeel|
|---|---|---|
|`stg_price_recommendation` (advies)|4,1–6,0 €/m³|Onrealistisch, ongeveer 10 keer te hoog|
|`stg_market_price` (gasspot)|circa 0,47 €/m³ (55 €/MWh)|Ziet er normaal uit|
|`stg_contracts` (tarief voor klanten)|1,29–1,45 €/m³|Ziet er normaal uit voor een totaalprijs aan huishoudens|
|`stg_procurement_trades`|volume in m³, prijs in €/MWh|Eenheden niet gelijk, dus niet te vermenigvuldigen|
4. **Churnrisico is niet bruikbaar.** `estimated_churn_risk` is de geschatte kans dat een klant opzegt. Het getal verandert sterk tussen runs (2,0–2,4% bij 200 klanten, 4,3–6,4% bij 500) en komt niet uit de data. Bij 500 klanten gaat het ook niet omhoog bij langere contracten.
5. **Kwaliteitsscores zijn niet berekend.** De tabel `stg_data_quality` zegt voor alle 12 datasets "OK", met scores boven 0,96. Maar `stg_customers` heeft in werkelijkheid geen enkel leeg veld (volledigheid 1,0, de tabel zegt 0,987). De fouten uit punt 1 worden niet gemeld.
6. **Weinig variatie.** Er is één regio (NL_ZUID) en alleen huishoudens. 222 van de 500 klanten (44,4%) hebben zonnepanelen (PV).

**Wat ontbreekt voor trede 1**

- **Weinig geschiedenis.** Alles behalve de startdatum van de contracten gaat over 2026. Ook de volledige set (30.000 × 365 regels) heeft maar één jaar. Andere jaren ontbreken. Voor trede 1 lossen we dit op met een aanname: het basistarief is het gemiddelde contracttarief van 2024–2025.
- **Eén tarief per contract.** Er is geen reeks van tarieven in de tijd en er zijn geen afrekeningen. Tarieven van contracten uit 2024 en 2025 verschillen minder dan 0,5% (1 jaar stroom: 0,2821 in 2024 en 0,2834 in 2025). Het contracttarief per contractvorm is wel ons vertrekpunt (L1).
- **N1, O1 t/m O3 en CPI.** Deze zitten niet in de data. Ze komen uit externe bronnen (ACM, Belastingdienst/Rijksoverheid, CBS) en worden apart opgehaald. Dit is datavraag 4.
- **L3 en L8 zijn geen aparte data voor trede 1.** We nemen aan dat het groencertificaat (L3) en de terugleverkosten (L8) in het historische contracttarief zitten en daarmee worden meegenomen. Dit vragen we na bij de product-owner/stakeholder.

**Beperking: kleine en nagemaakte dataset**

De analyse is gedaan op nagemaakte data van 500 klanten. Dat is 1,7% van de 30.000 huishoudens die het script maximaal maakt. Een eerdere run met 200 klanten gaf bijna dezelfde gemiddelde tarieven per contractvorm (verschil kleiner dan 0,5%). De gemiddelden zijn dus stabiel. Kleine groepen blijven onzeker, bijvoorbeeld een klantsoort binnen de 5-jaarscontracten. Het verbruik is gemaakt uit een jaardoel en is niet gemeten. De scores gaan daarom over wat er in de data zit en hoe die is opgebouwd, niet over de kwaliteit van de echte systemen van Fontasya. We weten ook niet of de verdeling over contractvormen en klantsoorten klopt met de echte klanten. Controleer de uitkomsten daarom met echte data van Fontasya voordat ze worden gebruikt voor prijsbesluiten.

## 4. Gap-analyse trede 1

### 4.1 Datavragen

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|Nr.|Datavraag|Component|Bron|Score|Wat ontbreekt|
|1|Historische afrekeningen en tarieven per contractvorm en commodity; welke periode is representatief?|L1|`stg_contracts` (tarief bij afsluiten, 2024–2025), `stg_portfolio` (gemiddelden), `stg_price_recommendation` (maandadvies 2026)|🟡|Geen afrekeningen, geen tarieven door de tijd. De adviesprijzen zijn niet te vergelijken met de contracttarieven.|
|2|L7 te splitsen in vast en variabel deel?|L7|`stg_contracts` (maandvergoeding en tarief per kWh of m³), `stg_price_recommendation` (risico-opslag, doelmarge), `stg_generation_production` (kostprijs eigen productie)|🟡|Het vaste deel staat apart. Het contracttarief zelf is niet op te delen in inkoop, marge en certificaat.|
|3|Jaarverbruik per klant of klantgroep|alle|`stg_electricity_consumption`, `stg_gas_consumption`, `stg_customers`, `stg_portfolio`|🟢|Alleen 2026 en gemaakt uit jaardoelen (niet gemeten).|
|4|Aannames N1 en O1 t/m O3 en bron|N1, O1 t/m O3|Niet in de data. `stg_network_system` is geen goede vervanger voor N1.|⚪|De externe bronnen (ACM, Belastingdienst/Rijksoverheid, CBS) zijn nog niet bekeken.|
|||||||

### 4.2 Aanvullende checks trede 1

|   |   |   |   |
|---|---|---|---|
|Onderwerp|Check|Score|Opmerking|
|CPI|Welke index en bron wordt gebruikt voor L7?|⚪|Niet in de data. Extern ophalen (CBS).|
|L3|Zit groencertificaat in het tarief?|🟡|Niet te zien in de data. Aanname: het zit in het contracttarief. Navragen bij de product-owner.|
|L8|Terugleverkosten: aanname of in tarief?|🟡|Alleen een vergoeding voor teruglevering, geen kosten. Aanname: eventuele kosten zitten in het contracttarief. Navragen bij de product-owner.|
|Contractvormen|Zijn er tarieven per looptijd (1, 3, 5 jaar) en flexibel?|🟢|Alle vier zijn er, elk met tarief voor stroom en gas.|

### 4.3 Beoordeling per criterium

|   |   |   |   |
|---|---|---|---|
|Criterium|Datavraag 1 (tarieven)|Datavraag 2 (vast/variabel)|Datavraag 3 (jaarverbruik)|
|Aanwezigheid|🟢 Tarief per contract aanwezig|🟡 Vast deel apart, de rest niet|🟢 Aanwezig, ook per contractvorm|
|Volledigheid|🟢 Alle contracten ingevuld|🟡 Geen opbouw van de contracttarieven|🟢 Alle klanten, alle dagen|
|Historie|🟡 Alleen contracten uit 2024–2025|🟡 Hetzelfde|🟡 Alleen 2026|
|Granulariteit|🟢 Per contractvorm en commodity|🟡 Vast per contract, opslagen alleen in het advies|🟢 Per klant per dag|
|Actualiteit|🟢 Laatste contract start eind 2025|🟢 Advies en kostprijs voor 2026|🟡 Heel 2026, maar deels gemaakt voor de toekomst|

Datavraag 4 heeft ⚪ en is daarom hier niet beoordeeld.

## 5. Overzicht en haalbaarheid trede 1

### 5.1 Samenvatting

|   |   |   |   |   |
|---|---|---|---|---|
|Datavraag|Score|Blokkeert dit?|Actie|Eigenaar|
|1 Tarieven en historie|🟡|Nee|Aanname voor het basistarief onderbouwen. Vragen of er meer jaren kunnen komen.|Product-owner|
|2 Vast en variabel (L7)|🟡|Nee. Zonder opbouw wordt L7 als geheel geïndexeerd.|Vragen wat L7 is.|Product-owner|
|3 Jaarverbruik|🟢|Nee|n.v.t.|n.v.t.|
|4 N1, O1 t/m O3|⚪|Nog niet bekend|Externe bronnen ophalen (ACM, Belastingdienst, CBS).Product-owner of Student?|
|L3 en L8 (extra check)|🟡|Nee|Aannemen dat ze in het contracttarief zitten. Navragen.|Product-owner|

**Conclusie.** Trede 1 kan voorlopig, onder voorwaarden. Datavraag 1 tot en met 3 scoren minstens 🟡 (dus geen 🔴). De conclusie is pas definitief als datavraag 4 is uitgezocht. Voor L3 en L8 nemen we aan dat ze in het contracttarief zitten. Dat vragen we na bij de product-owner.

### 5.2 Overzicht per component

De kolom Methode 1 vul je zelf aan uit het onderzoeksdocument. Onderdelen die hier niet staan, zijn niet bekeken.

|   |   |   |
|---|---|---|
|Component|Is de data er?|Aanname / bron|
|L1 (tarieven)|🟡 Contracttarieven per contractvorm|Basistarief = gemiddeld contracttarief per contractvorm|
|L3 (groencertificaat)|🟡 Niet los te zien|Aanname: zit in het contracttarief. Navragen.|
|L7 (vast/variabel)|🟡 Vast deel wel, de opbouw niet|Zonder opbouw wordt L7 als geheel geïndexeerd.|
|L8 (terugleverkosten)|🟡 Alleen de vergoeding|Aanname: eventuele kosten zitten in het contracttarief. Navragen.|
|N1|⚪ Niet in de data|ACM (extern)|
|O1 t/m O3|⚪ Niet in de data|Belastingdienst/Rijksoverheid (extern)|
|CPI|⚪ Niet in de data|CBS (extern)|

### 5.3 Risico's en beperkingen

- **Indexeren is niet te controleren.** De tarieven veranderen bijna niet in de tijd. Je kunt dus niet nagaan of indexeren met de CPI de echte tariefwijzigingen goed voorspelt. De contractvormen verschillen wel duidelijk van elkaar: een langer contract kost meer. Het risico "weinig verschil tussen contractvormen" geldt dus niet.
- **Keuze van de referentieperiode.** Er zijn maar twee jaren waarin contracten starten. Daarom is niet te testen hoe gevoelig het resultaat is voor deze keuze.
- **Kleine en nagemaakte data.** Zie de beperking bij 3.1. De scores gaan over de opbouw van de data en niet over de echte systemen.
- **Onderdelen van het script die we niet gebruiken.** De adviesprijzen, het churnrisico en de kwaliteitsscores zijn niet gebruikt (zie 3.1).

## 6. Vragen aan de product-owner

Om trede 1 goed te kunnen onderbouwen is extra data nodig in het script. Dit zijn de vragen voor de product-owner of een stakeholder van Fontasya.

### 6.1 Data die aan het script moet worden toegevoegd

|   |   |   |   |
|---|---|---|---|
|Nr.|Wat moet er bij?|Waarom?|Datavraag|
|1|Tarieven en verbruik over meer jaren|Nu is er alleen 2026. Zonder meer jaren is niet te zien hoe tarieven veranderen.|1|
|2|Tariefgeschiedenis per contract (tarief per maand of per jaar) of afrekeningen per klant|Nu is er één tarief per contract. Voor indexeren heb je het historische tarief nodig.|1|
|3|De opbouw van het tarief in vaste en variabele delen (L7)|Nu is alleen de vaste maandvergoeding apart te zien.|2|
|4|Of het groencertificaat (L3) en de terugleverkosten (L8) in het tarief zitten, of een aparte kolom ervoor|Nu is dit niet te zien.|L3 en L8|
|5|Verlengde en beëindigde contracten, met kloppende status en einddatum|Nu staat alles op ACTIVE, ook als de einddatum voorbij is.|1 en 3|
|6|N1-tarieven per aansluittype, belastingen (O1 t/m O3) en de CPI|Deze zitten niet in het script. Vragen of ze toegevoegd kunnen worden, of dat wij ze zelf ophalen (ACM, Belastingdienst, CBS).|4|

### 6.2 Vragen over wat er al in het script zit

|   |   |   |
|---|---|---|
|Nr.|Vraag|Waarom?|
|1|Klopt de omrekening van het gasadvies?|Het gasadvies lijkt veel te hoog ten opzichte van de gasprijs op de markt (zie 3.1).|
|2|Zitten risico-opslag en marge in de adviesprijs, of komen ze erbovenop?|Nu blijft bij sommige contractvormen bijna niets over voor de inkoop (zie 3.1).|
|3|Is het advies alleen de leveringsprijs, terwijl het contracttarief een totaalprijs is met belastingen en netkosten?|Het advies ligt veel lager dan het contracttarief. Dit is een vermoeden.|
|4|Is de vaste maandvergoeding het vaste deel van L7, en het tarief per kWh of m³ het variabele deel?|Nodig voor datavraag 2.|
|5|Zijn 1-jaarscontracten na de einddatum stilzwijgend verlengd?|Die klanten hebben nog verbruik na de einddatum (zie 3.1).|

## Bijlage A: Bronnen

Anthropic. (2026). Claude (Claude Sonnet 5.5) [Groot taalmodel]. https://claude.ai

Veen, R. van der. (2026, 17 september). _Generate dataset Fontasya Electric_ [Script en toelichting per e-mail]. Fontys ICT.

## Bijlage B: AI-verantwoording

**Gebruikte AI-tools.** Er is één AI-tool gebruikt: Claude (Anthropic, 2026). Claude hielp bij de opzet van het document, bij het analyseren van de data en bij het schrijven van de code voor de staging. De keuzes, de eindredactie en de verantwoordelijkheid liggen bij de auteur.

|   |   |   |   |
|---|---|---|---|
|Onderdeel|Tool|Wat deed de tool|Wat deed de auteur|
|Opzet van de gap-analyse (hoofdstukken, beoordelingscriteria, scoremodel, beslisregel)|Claude|Voorstel voor de opzet, op basis van de datachecklist uit het onderzoeksdocument (§5.2)|Het voorstel beoordeeld, gekozen voor trede 1 en de hoofdvraag aangepast|
|Analyse van `dev.duckdb` en de voorbeeldbestanden van het script (data bekijken, bevindingen, voorstel voor scores en tekst)|Claude|Vragen aan de data gesteld en een voorstel gedaan voor scores en tekst|De data aangeleverd, scores en aannames beoordeeld en aangepast|
|Staging-code (dbt-modellen en tests)|Claude|Code herschreven, uitgebreid en gecontroleerd|Code beoordeeld, gedraaid en in het project gezet|

**Controle.** Alle teksten van AI zijn door de auteur gelezen en waar nodig aangepast. De data is nagemaakt (met onder andere EAN-codes, coördinaten, postcode4 en klanttokens). Er zijn dus geen persoonsgegevens van klanten of vertrouwelijke bedrijfsdata met de tool gedeeld.