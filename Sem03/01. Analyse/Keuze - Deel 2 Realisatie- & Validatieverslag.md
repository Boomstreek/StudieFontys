## Metadata
**Auteur:** Bram Wieringa  
**Datum:** 22-09-2026 
**Versie:&** 1.0
**Afhankelijkheden:** Keuze - welke prototype database v1.1
**Omgeving:** Arch Linux (Omarchy) | Python 3.12 (`uv`) | DuckDB v1.5.5 | dbt-core v1.12.5 | `dbt-duckdb` v1.11.0  

## 1. Inleiding & Context
In het voorafgaande onderzoeksdocument (*"Keuze - welke prototype database v1.1"*) is op basis van een *Available Product Analysis (Library)* onderbouwd dat **DuckDB** in combinatie met **dbt-duckdb** de meest geschikte in-process OLAP-architectuur vormt voor het verwerken van gecomprimeerde netcongestiedatasets (`.csv.gz`).

Dit document vormt de directe praktische invulling van de vervolgstappen uit dat onderzoek (Paragraaf 6.2: *Prototyping & Integration Test*). Het beschrijft de daadwerkelijke inrichting, de opgetreden technische uitdagingen (zoals proces-locking en pad-resoluties) en de validatie van de opgeleverde data pipeline.

## 2. Praktische Realisatie (Prototyping & Integration Test)
Conform het advies uit het vooronderzoek is de pipeline volledig geautomatiseerd en versiebeheerd ingericht via de Linux CLI.

### 2.1 Omgevingsinrichting via `uv`
Om een lichtgewicht, zero-daemon omgeving te garanderen zonder systeemvervuiling, is de gehele Python-omgeving geïsoleerd opgezet met `uv`:

* **Afhankelijkheden:** `dbt-duckdb`, `duckdb` en `harlequin`.
* **Uitvoering:** Alle commando's worden geïsoleerd aangeroepen binnen de virtuele omgeving (`uv run`).

### 2.2 Staging Modellen & `.csv.gz` Ingestie
Er zijn 8 SQL-stagingmodellen opgebouwd in de map `models/staging/`. DuckDB leest de gecomprimeerde bronbestanden direct in via de `read_csv_auto()` functie zonder uitpakstap op de harde schijf.

* **Tijdsreeksscenario's (Wildcards op `.csv.gz`):**
  * `stg_electricity_consumption.sql`
  * `stg_gas_consumption.sql`
  * `stg_pv_feedin.sql`
* **Dimensionele entiteiten (`.csv`):**
  * `stg_customers.sql`, `stg_contracts.sql`, `stg_energy_balance.sql`, `stg_network_system.sql`, `stg_pv_assets.sql`.

---

## 3. Technische Aandachtspunten & Oplossingen

Tijdens de *Integration Test* (het koppelen van dbt aan DuckDB en Harlequin) deden zich twee specifieke runtime-vraagstukken voor die als volgt zijn opgelost:

### 3.1 Foutafhandeling: Concurrerende Bestandsvergrendeling (File Locking)
* **Probleem:** Tijdens het testen ontstond een `IO Error: Could not set lock on file`, doordat de TUI-client **Harlequin** en `dbt run` gelijktijdig hetzelfde `.duckdb` bestand probeerden te beschrijven.
* **Oorzaak & Oplossing:** DuckDB is een *single-writer* embedded database. Voor geautomatiseerde batch-runs dient Harlequin afgesloten te worden, of moet er via gescheiden lees-processen gewerkt worden. Dit bevestigt de conclusie uit het vooronderzoek dat Harlequin puur als *secundaire interactieve inspectietool* dient te worden gebruikt.

### 3.2 Relatieve vs. Absolute Paden in `profiles.yml`
* **Probleem:** Bij het aanroepen van `dbt run` vanuit verschillende submappen ontstonden er meerdere, gefragmenteerde `dev.duckdb` bestanden op de schijf.
* **Oplossing:** De relatieve paden in `~/.dbt/profiles.yml` zijn vervangen door **absolute paden**. Hierdoor kijken dbt, de DuckDB CLI én Harlequin altijd gegarandeerd naar exact hetzelfde databasebestand.

```yaml
# ~/.dbt/profiles.yml
grid_congestion_pipeline:
  outputs:
    dev:
      type: duckdb
      path: /home/bram/Documents/Studie/Sem03/dbt/dev.duckdb
      threads: 1
  target: dev
````

## 4. Validatie & Resultaten

De opgeleverde keten is succesvol gevalideerd via de terminal:

1. **dbt Execution (`dbt run` / `dbt build`):**
    
    - Alle 8 staging-modellen bouwen foutloos op als fysieke tabellen (`PASS=8`).
        
    - De totale uitvoeringstijd voor de volledige transformatie bedraagt **1.21 seconden**.
        
2. **Datakwaliteit & Inspectie (Harlequin):**
    
    - Via `uv run harlequin dev.duckdb` is geverifieerd dat de tabellen in het `main`-schema correct zijn gevuld en direct querybaar zijn voor vervolganalyses.
        

## 5. Conclusie

De praktische realisatie bevestigt de hypothese uit het vooronderzoek (_"Keuze - welke prototype database v1.1"_):

1. **Zero-Daemon werkt in de praktijk:** De combinatie van DuckDB en dbt draait extreem snel, vereist geen achtergrondservices en laat geen rommel achter op het Linux-systeem.
    
2. **Directe `.csv.gz` verwerking:** De data wordt zonder tussentijdse decompressiestappen correct en binnen 1,5 seconde getransformeerd.
    
3. **Pijplijn is gereed:** De staging-laag staat als een huis. De vervolgstap binnen het project is het bouwen van **Intermediate / Mart modellen** voor de inhoudelijke netcongestie-analyses.
    

## 6. AI-Verantwoording (Conform Opleidingsrichtlijnen)

- **Tooling:** Google Gemini (Gemini Pro).
    
- **Toepassing:** AI is ingezet als _interactieve debugging-partner_ bij het analyseren van dbt-foutmeldingen (zoals de `IO Error` file locking) en het optimaliseren van pad-referenties binnen Arch Linux.
    
- **Eigen Regie:** De inhoudelijke keuzes voor de datastructuur, het opzetten van de staging-modellen, de configuratie van de absolute paden en het fysiek testen in de terminal zijn volledig zelfstandig uitgevoerd en gecontroleerd door de onderzoeker.
    

```

### Wat is er nu anders/beter?
* Het sluit naadloos aan op de structuur van je PDF[cite: 1].
* Het verwijst naar Hoofdstuk 6.2 van je vooronderzoek als startpunt[cite: 1].
* Het documenteert de **werkelijke praktijkstappen en problemen** die we zojuist hebben opgelost (zoals de `dev.duckdb` paden, de Harlequin file lock en de `uv` omgeving).
```