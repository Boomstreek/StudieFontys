## Rollen & Teamstructuur

### AI-chatbot Sociaal Knooppunt
**Author: ** Bram Wieringa
**Date: ** 26-04-2026
**Version: ** 1.0
**Dependencies: ** 
- Projectscope versie 1.1

### Inleiding

Dit document beschrijft de teamstructuur en rolverdeling voor het project. De groep bestaat uit acht studenten met verschillende specialisaties. Om effectief samen te werken wordt gekozen voor één overkoepelende projectgroep met twee Scrumteams daaronder. Vanuit de projectgroep worden een aantal centrale rollen belegd die zorgen voor samenhang, richting en technische aansluiting tussen de teams.

De reden voor deze structuur is dat de specialisaties van de studenten sterk van elkaar verschillen. Zonder duidelijke rolverdeling bestaat het risico dat iedereen zich verliest in zijn eigen onderdeel, terwijl het eindproduct alleen werkt als alle onderdelen goed op elkaar aansluiten.

### Overkoepelende projectrollen

Deze rollen gelden voor het gehele project en staan boven de twee Scrumteams.

#### Product Owner

**Aantal:** 1

De Product Owner is verantwoordelijk voor de inhoudelijke richting van het project. Hij of zij bewaakt de scopedocumenten (MoSCoW), stelt prioriteiten en is het aanspreekpunt richting de opdrachtgever. De Product Owner beantwoordt continu de vraag: _bouwen we het juiste?_

**Taken:**

- Bijhouden en bewaken van de projectscope
- Opstellen en prioriteren van de backlog
- Afstemming met de opdrachtgever (Carla Renders)
- Bewaken dat het team de "waarom" niet uit het oog verliest
- Definitief beslissen wanneer een onderdeel voldoet aan de Definition of Done

**Geschikt voor:** student met specialisatie Business & Data _kanttekening aanstaande ouderschap, dit goed bespreken en samen of een oplossing vinden mocht het misgaan en ik me voltijd moet foccussen op mijn gezin, bijvoorbeeld reserve instellen of b gezamlijk akkoord gaan _

---

#### Technisch Lead

**Aantal:** 1

De Technisch Lead zorgt dat de technische onderdelen van de twee Scrumteams goed op elkaar aansluiten. Hij of zij heeft overzicht over de volledige technische architectuur en signaleert tijdig wanneer keuzes van het ene team invloed hebben op het andere. De Technisch Lead bouwt zelf mee, maar heeft ook een coördinerende rol.

**Taken:**

- Bewaken van de technische architectuur als geheel
- Zorgen dat de AI-stack, backend en infrastructuur op elkaar aansluiten
- Afstemming tussen de twee Scrumteams op technisch vlak
- Beoordelen van technische keuzes en deze documenteren
- Aanspreekpunt voor technische vragen vanuit beide teams

**Geschikt voor:** student met specialisatie AI of Software

---

#### Scrum Master

**Aantal:** 1 (gedeeld over beide teams)

De Scrum Master zorgt dat het Scrumproces goed verloopt. Hij of zij organiseert de stand-ups, sprint planningen en retrospectives, en signaleert wanneer een team vastloopt of afdwaalt. De Scrum Master is geen inhoudelijk beslisser, maar een procesbewaker.

**Taken:**

- Organiseren van stand-ups, sprintplanningen en retrospectives
- Bijhouden van de voortgang in beide teams
- Signaleren van blokkades en deze bespreekbaar maken
- Bewaken dat het team op koers blijft met de planning
- Notulen of samenvattingen bijhouden van overlegmomenten

**Geschikt voor:** elke specialisatie, bij voorkeur iemand die overzicht houdt en communicatief sterk is

---

### Scrumteam 1 – AI & Gesprekslogica

Dit team is verantwoordelijk voor de kern van de chatbot: het gesprek zelf, de gesprekslogica op basis van het gekozen model en de matchinglogica.

**Samenstelling:** 3–4 studenten met specialisatie AI

**Verantwoordelijkheden:**

- Uitwerken van de systeemprompt op basis van het gekozen gespreksmodel (Positieve Gezondheid of Het Leefstijlroer)
- Opzetten van de AI-stack (LLM-keuze, RAG-architectuur)
- Ontwikkelen van de matchinglogica
- Opstellen van synthetische data (activiteiten, aanbieders, locaties)
- Opstellen van persona's en een voorbeeldgesprek (happy flow)
- Testen van de gesprekslogica en matchingkwaliteit

---

### Scrumteam 2 – Software, Infrastructuur & Data

Dit team is verantwoordelijk voor de technische omgeving waarin de chatbot draait, de koppeling met de frontend en het dashboard voor de opdrachtgever.

**Samenstelling:**

- 2 studenten met specialisatie Software
- 1 student met specialisatie Infrastructuur
- 1 student met specialisatie Business & Data

**Verantwoordelijkheden:**

- **Software (programmeurs):**
    - Bouwen van de web-based chatbot interface
    - Koppeling tussen frontend en AI-backend
    - Zorgen dat het prototype zelfstandig draait en bereikbaar is
- **Infrastructuur:**
    - Uitwerken van de hostingarchitectuur (theoretisch en praktisch voor het prototype)
    - Borgen van privacy by design in de technische opzet
    - Documenteren van de infrastructuurkeuzes voor overdracht
- **Business & Data:**
    - Ontwerpen en bouwen van een dashboard met inzichten voor de opdrachtgever, zoals:
        - aantal gesprekken gevoerd
        - meest voorgestelde activiteiten
        - type gebruikersvragen
    - Conceptuele uitwerking van het businessmodel
    - Ondersteunen van de Product Owner bij scopebewaking

---

### Overzicht

|Rol|Specialisatie|Scrumteam|
|---|---|---|
|Product Owner|Business & Data|Overkoepelend|
|Technisch Lead|AI of Software|Overkoepelend|
|Scrum Master|Vrij|Overkoepelend|
|AI-ontwikkelaar (3x)|AI|Team 1|
|Softwareontwikkelaar (2x)|Software|Team 2|
|Infrastructuur|Infrastructuur|Team 2|
|Business & Data|Business & Data|Team 2|

---

### Aandachtspunten

- De Product Owner is het enige aanspreekpunt richting de opdrachtgever, tenzij anders afgesproken. Dit voorkomt verwarring over wie wat heeft beloofd.
- De Technisch Lead heeft geen doorslaggevende stem over inhoudelijke keuzes — dat is de Product Owner. Wel heeft de Technisch Lead een veto op technische keuzes die de architectuur of overdraagbaarheid in gevaar brengen.
- Beide Scrumteams werken in dezelfde sprintcyclus en komen minimaal één keer per sprint samen met de volledige projectgroep om voortgang te bespreken en af te stemmen.
- De Scrum Master bewaakt actief dat het team niet alleen bezig is met bouwen, maar ook nadenkt over de "waarom" achter elke keuze. Dit is essentieel voor de documentatie en de overdracht.

---

### Bronnen

Anthropic. (2026). _Claude Sonnet 4.6_ [Large language model]. Gebruikt als AI-assistent bij het opstellen van dit document. [https://www.anthropic.com](https://www.anthropic.com)

Fontys Hogeschool ICT. (2026, 23 april). _AI-bot sessie_ [Vergaderingstranscriptie].