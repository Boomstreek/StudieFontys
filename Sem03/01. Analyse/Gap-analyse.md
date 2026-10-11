# Gap-analyse: is trede 1 (basisindexering) mogelijk met de data van Fontasya Electric?

## Algemene gegevens
### Metadata
| | |
|---|---|
| Naam student | Bram Wieringa |
| Versienummer | 0.1 |
| Datum huidige versie | |
| Referenties | Scope - Fontasya Electric.pdf v1.5; Welke energiedata is nodig om adviestarieven te berekenen? v0.1 |

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
- Trede 2 en 3: mogelijk alleen een vooruitblik (hoofdstuk 6), geen volledige toetsing

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
|Tabel|Inhoud|Periode|Rijen|
|---|---|---|---|
|stg_contracts|Contractvorm, start/einde, tarief stroom en gas, vaste maandvergoeding, status|start 2024-01 t/m 2025-12|200|
|stg_customers|Segment, regio, PV ja/nee, jaarverbruik-target|n.v.t.|200|
|stg_electricity_consumption|Dagverbruik stroom per klant|2026-01-01 t/m 2026-12-31|73.000|
|stg_gas_consumption|Dagverbruik gas per klant|idem|73.000|
|stg_energy_balance|Dagtotalen verbruik, PV, day-ahead- en gasprijs|idem|365|
|stg_network_system|Distributie, transport, verlies, balancering, congestie|idem|365|
|stg_pv_assets|PV-installaties per klant|n.v.t.|86|
|stg_pv_feedin|Dagelijkse teruglevering en terugleverprijs|2026|31.390|


### 3.1 Datakwaliteit
Beperking (Dit is op basis van 200 klanten, dus een subset van de data.)

**Goed**
- Geen dubbelen, nulls of negatieven in het verbruik. Alle 200 klanten hebben alle 365 dagen, voor stroom en gas.
- De EAN-codes komen overeen tussen contracten, klanten en verbruik.
- De dagtotalen over alle klanten komen exact overeen met `stg_energy_balance`.

**Aandachtspunten**

1. **Geen historie.** Alles behalve de contractstart is alleen 2026. Een referentieperiode als 2022 zit er niet in.
2. **Eén tarief per contract.** Er is geen tarieftijdreeks en geen tabel met afrekeningen. De tarieven per afsluitjaar zijn bijna gelijk: 1 jaar stroom 0,2833 (2024) tegenover 0,2835 (2025).
3. **Contractstatus klopt niet.** Alle 200 contracten staan op ACTIVE, ook 58 van de 64 1-jaarscontracten waarvan de einddatum al voorbij is. Er zijn geen beëindigde contracten of verlengingen, dus ook geen churn.
4. **Verbruik na einde contract.** 64 klanten (alle 1 jaar) hebben samen 17.500 verbruiksrijen na hun einddatum.
5. **Verbruik is geen meting.** Het loopt tot 31-12-2026, dus 81 dagen in de toekomst. De jaarsom per klant is exact gelijk aan `annual_*_target` (afwijking maximaal 0,02). Het jaarverbruik is dus gegenereerd, geen waarneming.
6. **Netwerkdata niet bruikbaar als N1.** `stg_network_system` heeft 365 verschillende `network_id`’s, één per dag. Distributie (40–43 €/MWh) en transport (13,6–14,8 €/MWh) variëren dagelijks, terwijl gereguleerde tarieven jaarlijks vastliggen.
7. **Beperkte spreiding.** Er is één regio (NL_ZUID) en alleen huishoudens. De 5-jaarscontracten zijn klein: 26 stuks, waarvan 4 Single en 6 Senior.

## 4. Gap-analyse trede 1
### 4.1 Datavragen
|Nr.|Bron in dev.duckdb|Score|Gap|Aanname / oplossing|
|---|---|---|---|---|
|1|`stg_contracts`: tarief per contractvorm en commodity|🟡|Geen afrekeningen, geen tarieftijdreeks, beperkte historie. Alleen tarieven bij afsluiting (2024–2025).|Neem het gemiddelde contracttarief per vorm over 2024–2025 als basistarief. Onderbouw dat het representatief is, en zeg erbij dat indexatie niet te valideren is aan historische wijzigingen.|
|2|`monthly_service_fee_eur` (vast, circa 8–10 €/mnd) en tarief per kWh/m³ (variabel)|🟡|Het vaste deel staat apart. Het tarief is niet verder op te splitsen (inkoop, marge, certificaat).|Als L7 een opbouw van het tarief is, is er een aanname nodig. Vraag Fontasya naar de kostprijsopbouw.|
|3|`stg_electricity_consumption`, `stg_gas_consumption`, plus segment in `stg_customers`|🟢|Alleen 2026 en gegenereerd uit targets. Het jaarverbruik is kloppend en volledig.|Gemiddeld 2.873 kWh en 1.119 m³ per klant; per segment: Single circa 2.093 kWh, Family 3.753 kWh. Noem de beperking dat het geen metingen zijn.|
|4|Niet aanwezig voor O1 t/m O3 en CPI. N1 alleen als niet-bruikbare proxy.|⚪|Externe bronnen (ACM, Belastingdienst, CBS) heb ik niet getoetst.|Dit hoort extern opgehaald te worden. Pas scoren zodra je de bronnen hebt gecheckt.|

### 4.2 Aanvullende checks trede 1
| Onderwerp | Check | Score | Opmerking |
|---|---|---|---|
| CPI | Welke index en bron wordt gebruikt voor L7? | | |
| L3 | Zit groencertificaat in het tarief? | | |
| L8 | Terugleverkosten: aanname of in tarief? | | |
| Contractvormen | Zijn er tarieven per looptijd (1, 3, 5 jaar) en flexibel? | | |

### 4.3 Per datavraag (uitwerking)
#### Datavraag 1: ...
- Wat is er aangetroffen
- Beoordeling per criterium
- Gap en oplossing

## 5. Overzicht en haalbaarheid trede 1

### 5.1 Samenvatting
| Datavraag | Score | Blokkerend? | Actie | Eigenaar |
|---|---|---|---|---|

### 5.2 Overzicht per component (L1 t/m O3)
| Component | Methode 1 | Data beschikbaar? | Aanname |
|---|---|---|---|

### 5.3 Risico's en beperkingen
- Vlakke curve, weinig onderscheid tussen contractvormen
- Gevoeligheid voor referentieperiode
- **Beperking: de dataset is synthetisch en klein ten opzichte van het werkelijke klantbestand.**  
Deze gap-analyse is uitgevoerd op een synthetische dataset van 200 klanten (dev.duckdb). Het werkelijke klantbestand van Fontasya Electric telt naar verwachting circa 27.000 klanten [bron of “aanname, nog te bevestigen”], dus de dataset beslaat ongeveer 0,7% daarvan. Daarnaast is het verbruik gegenereerd op basis van jaardoelen per klant en is het geen meetdata. De scores in deze analyse zeggen daarom iets over de _structuur en beschikbaarheid_ van de data, niet over de kwaliteit van de werkelijke bronsystemen. Gemiddelde tarieven per contractvorm zijn bruikbaar voor een eerste uitwerking van trede 1, maar met een grotere onzekerheid, vooral bij kleine groepen (5-jarige contracten: 26). Of de verdeling over contractvormen en segmenten overeenkomt met het echte klantbestand is niet vastgesteld. De uitkomsten moeten daarom worden gevalideerd op echte Fontasya-data voordat ze voor prijsbesluiten worden gebruikt.

## Bijlage A: Bronnen
Anthropic. (2026). Claude (Claude Sonnet 5.5) [Groot taalmodel]. https://claude.ai

## Bijlage B: AI-verantwoording

**Gebruikte AI-tools.** Bij dit document is één generatieve AI-tool gebruikt: Claude
(Anthropic, 2026). Claude is ingezet als sparringpartner voor de opzet van dit document.
De inhoudelijke keuzes, de eindredactie en de verantwoordelijkheid voor dit document
liggen bij de auteur.

| Onderdeel | Tool | Aard van de ondersteuning | Rol van de auteur |
|---|---|---|---|
| Opzet gap-analyse (hoofdstuk-indeling, beoordelingscriteria, scoringsmodel, beslisregel) | Claude | Voorstel voor de structuur van het document op basis van de datachecklist uit het onderzoeksdocument (§5.2) | Beoordeling van het voorstel, bepalen van de focus op trede 1 en aanpassing van de hoofdvraag |

**Controle.** Alle door AI gegenereerde teksten zijn door de auteur beoordeeld en waar
nodig aangepast. Er zijn geen persoonsgegevens van klanten of vertrouwelijke bedrijfsdata
met de tool gedeeld.

*Wordt aangevuld naarmate er meer onderdelen met AI worden uitgewerkt.*