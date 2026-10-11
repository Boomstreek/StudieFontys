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
| Bron/bestand | Inhoud | Periode | Format | Eigenaar | Opmerking |
|---|---|---|---|---|---|

### 3.1 Datakwaliteit
- Per bron: volledigheid, consistentie, bijzonderheden

## 4. Gap-analyse trede 1
### 4.1 Datavragen
| Nr. | Datavraag | Component | Bron | Score | Gap | Aanname / oplossing |
|---|---|---|---|---|---|---|
| 1 | Historische afrekeningen en tarieven per contractvorm en commodity; welke periode is representatief? | L1 | | | | |
| 2 | L7 te splitsen in vast en variabel deel? | L7 | | | | |
| 3 | Jaarverbruik per klant of klantgroep | alle | | | | |
| 4 | Aannames N1 en O1 t/m O3 en bron | N1, O1 t/m O3 | | | | |

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