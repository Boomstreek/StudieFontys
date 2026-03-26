## Projectplanning: Digitalisering OK-Planning (4 Weken)
### Week 1: Business Analysis & Data Design
_Focus: Het fundament leggen en de nulmeting concretiseren._

- **Activiteiten:**
    - **BPMN-verfijning:** Het bestaande proces uit 1a uitbreiden en versimpelen met de financiële meetpunten (waar ontstaat de NVAT?).
    - **Data-inventarisatie:** Definiëren van de exacte datastructuur (ERD Chen-notatie) die nodig is voor de CPB-berekening.
    - **Stakeholder check:** Kort fictief overleg met de 'Manager OK-planners' om de KPI's (CPB, NVAT) te valideren. 'Manager OK-planners' worden gedaan door AI
- **Deliverable:** Definitief Business Analysis Document (Aanvulling op versie 1.1).
    

### Week 2: Data & IT-Integration (The Proof of Concept)
_Focus: Van theorie naar cijfers._

- **Activiteiten:**
    - **Dataverzameling/Simulatie:** ERD-Crowsfeetnotatie maken op basis van de ERD Chen notatie, vervolgens daarvoor data generen met mockdata python script
    - **Power BI Ontwikkeling (Backend):** Laden van data, opschonen in Power Query en het leggen van relaties.
    - **Dashboarding:** Opzet van de 'Must Haves' uit de MoSCoW-analyse (Nulmeting en NVAT-monitor).
- **Deliverable:** Eerste versie Power BI Dashboard (POC).
    

### Week 3: Digital Optimization & Implementation
_Focus: De oplossing bouwen en testen._

- **Activiteiten:**
    - **Prototype bouwen:** Ontwikkelen van een eenvoudige "Besparingscalculator" (bijv. in Excel met macro's of een Power App laag) die de impact van de _Digital Adoption Rate_ simuleert.
    - **Integratie:** De calculator koppelen aan het Power BI dashboard (de 'Should Haves').
    - **Testen:** Controleren of de berekeningen achter de CPB en FTE-besparing logisch kloppen bij verschillende scenario's.
- **Deliverable:** Werkend prototype van de optimalisatie-tool.
    

### Week 4: Business Impact & Rapportage
_Focus: Resultaten interpreteren en presenteren._

- **Activiteiten:**
    - **Impactanalyse:** De resultaten van de simulatie vertalen naar een concreet advies (bijv. "Bij 60% adoptie besparen we 1.2 FTE").
    - **Adviesrapport:** Het documenteren van de bevindingen, de gebruikte IT-componenten en de aanbevelingen voor fase 2.
    - **Peerreview:** Presenteren aan medestudenten en feedback verwerken.
        
- **Deliverable:** Integraal Adviesrapport & Eindpresentatie.
```mermaid
gantt
    title Projectplanning: Digitalisering OK-Planning (4 Weken)
    dateFormat  YYYY-MM-DD
    axisFormat  %d-%m
    
    section Week 1: Business Analysis
    BPMN-verfijning & Financieel Kader    :active, w1a, 2026-03-24, 3d
    Data-inventarisatie & Structuur       :w1b, after w1a, 2d
    Stakeholder Validatie KPI's           :milestone, m1, 2026-03-30, 0d

    section Week 2: Data & IT-Integration
    Dataset Simulatie (Excel/Data Gen)    :w2a, 2026-03-31, 3d
    Power BI Dashboard: Nulmeting & NVAT   :w2b, after w2a, 4d
    Proof of Concept Oplevering           :milestone, m2, 2026-04-06, 0d

    section Week 3: Digital Optimization
    Prototype Besparingscalculator        :w3a, 2026-04-07, 4d
    Integratie Dashboard & Scenario-test  :w3b, after w3a, 3d
    Werkende Tool & Testrapport           :milestone, m3, 2026-04-13, 0d

    section Week 4: Impact & Advies
    Impactanalyse & Conclusies            :w4a, 2026-04-14, 3d
    Adviesrapport & Presentatie           :w4b, after w4a, 3d
    Peerreview & Finale Oplevering        :milestone, m4, 2026-04-20, 0d
```