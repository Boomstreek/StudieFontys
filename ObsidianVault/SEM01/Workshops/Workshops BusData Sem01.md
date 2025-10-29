Wat heb ik geleerd

# Les 1
## SQL, R & Python belangrijk voor data-visualisatie
### [[Werkboek R]] en [[datacamp.com]]
## Test dashboards altijd met testdata! Klopt de pi chart wel met 50/50 of laat die bij 50/50 20/80 zien.
## Pas op met open tekstvelden, dan moet je eerst alles categoriseren voordat je het kan visualiseren. 

# Les 2
## Data is storytelling
### Het verhaal kunnen vertellen over: het proces, de wens en de opdrachtgever
## Vragen:
### Uni-variate vs histogram, wat is het verschil

# Les 3
## [[ER Diagram]] basis
## [[Chen notatie]]
## Visual paradigm
## Vragen
### Wat is het verschil tussen [[ER Diagram]] en [[EER Diagram]]
#### Verschil is: 
### Welke notaties zijn er nog meer?
#### [[Chen notatie]]
#### [[Crow's foot notatie]]
#### meer?
##### Waarom kies je de een en niet de ander?
### Waarom N:M en niet N:N, verschil daartussen
####  N is 0, 1 of meer en M is 1, 2, of meer, maar dit staat niet vast

# Les 4 – Van ER-diagram naar Database

## Recap ER-diagram
- Basis voor: klasse diagram en database  
- **Entiteiten:** rechthoek  
- **Attributen:** ovaal  
- **Relaties:** ruit (met naam en kardinaliteit)  
- **Tools:** Virtual Paradigm, SmartDraw, Canva, Edraw  
- **Notatie:** Chen-notatie  

## Database
- Relaties kunnen ook attributen hebben  

### Stap 1 – Tabellen maken
- Elke entiteit (rechthoek) wordt een tabel  
- Elk veld heeft een unieke ID (meestal integer)  

### Stap 2 – Attributen toevoegen
- Voeg alle attributen van de entiteit toe aan de tabel  

### Stap 3 – Relaties omzetten
- Kardinaliteit: 0, 1 of n  
- **Foreign key:** verwijst naar ID in een andere tabel  
- **Bij n–n relaties:** maak een **koppeltabel**  
  - Naam: combineer de twee entiteiten of verzin een zinvolle naam  
  - Voeg attributen van de relatie toe  

**Voorbeelden:**  
- `Patient – Medicijn` → `PatientMedicijn(PatientID, MedicijnID, Aantal, Tijdstip)`  
- `Patient – Docter` → `Behandelaar(PatientID, DocterID)` (combinatie is uniek, geen aparte ID nodig)  

### Foreign key gedrag bij verwijderen
1. **Mandatory:** verwijderen verboden als er nog koppelingen zijn  
2. **Cascade:** verwijdert automatisch alle gekoppelde records  
3. **Set to null:** verwijst naar null bij verwijdering  

## Extra notities
- **Crow’s foot notatie:**  
  - `0` = 0 of 1  
  - `1` = altijd minstens 1  
  - Meer info: [Crow's Foot ERD Tutorial](https://medium.com/@callista.m.azizah/crows-foot-erd-for-beginners-a-tutorial-1effc8a326c6R)  

- **Praktisch:**  
  - Student Square portal: eigen database maken  
  - Azure Data Studio kan ook (SQL Server)  
  - Mockaroo.com: random data genereren  
  - R Studio script beschikbaar om verbinding te maken met SQL Server en data uit Excel te uploaden (script bij Kees)  

## Wat je hebt geleerd
- Koppeltabellen maken bij n–n relaties  
- Crow’s foot notatie begrijpen  
- ER-diagram vertalen naar een database voor je applicatie
