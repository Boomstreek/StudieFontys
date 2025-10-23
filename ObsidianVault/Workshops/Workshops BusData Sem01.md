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

# Les 5 - ER naar Database
Je hebt nog niet gekozen voor een DB of taal bij een ER-diagram. Die stap gaan we nu zetten

Recap

ER-diagram
basis voor:
- klasse diagram
- database

entiteiten rechthoek
attributen ovaal
relaties ruit

relaties naam en kardinaliteit. Geeft verhouding visueel wwer

tools:
virtual paradigm
smartdraw, canva, edraw

via chen notatie

Database

relaties kunnen ook attributen hebben

Stap 1
Alle rechthoeken worden een tabel
- elk veld heeft in ID <uniek>
	- Meestal worden integers gebruikt

Stap 2
Voeg de attributen toe aan de tabellen

stap 3 relaties
0, 1 of n
bijv. VerplID is gekoppeld aan ID table verpleegkundig

foreign key, identifier staat in een andere tabel

utizondering, bij veel op veel n - n

hier maak je een koppeltabel

als je dat heb dan maak je een apart tabel
Verzin zinvolle naam of voeg de twee namen samen
- voeg hier dan de attributen toe die op de relatie stonden

bijvoorbeld patient, medicijn wordt PatientMedicijn, PatientID, Medicijn ID, Aantal, Tijdstip

Patient en Docter is ook N - N. Samen wordt dat Behandelaar, met PatientID, DocterID
- dit heeft geen idee, en de cobinatie daarvan is uniek. Dus is al de ID

DIK gedrukt is de key van de tabel

Bij een foreign key als iets verwijdert word
drie dingen die je kan doen
- Mandatory, verboden is nog gekoppeld
- Cascade, waterfal, ook direkt de andere koppelingen verwijderen die daar op leunde.
- Foreign key -> null, alle patient id worden null.


kraaipoot notatie

-0 is 1 of 0
-1 is altijd min 1
meer even over uitzoeken
https://medium.com/@callista.m.azizah/crows-foot-erd-for-beginners-a-tutorial-1effc8a326c6R

Student square
self service portal, hier kan je een eigen database aanmaken op een fontys omgeving
azure data studio kan ook in sql server
hier de string invoeren van de studentsquar database die is aangemaatk

mockaroo.com kan je database laten invullen met random data

via R Studie is er een script om 
- verbinding te maken met sql server
- data te uploaden naar de database via excel
- script kan je vragen bij Kees

Wat heb ik geleerd:
- koppeltabel
- crow notatie (aanvulling)

ER-diagram voor applicatie
Dan database maken voor de applicatie