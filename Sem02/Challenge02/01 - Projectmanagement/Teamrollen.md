## Rollen & Teamstructuur

### Metadata
**Author: ** Bram Wieringa
**Date: ** 01-05-2026
**Version: ** 1.1
**Dependencies: ** 
- Projectscope versie 1.2
- Trancriptie: 2026-04-28 Projectoverleg rolverdeling en teamindeling.docx

### Inleiding

Dit document beschrijft de teamstructuur en rolverdeling voor het project. De groep bestaat uit acht studenten met verschillende specialisaties. Om effectief samen te werken wordt gekozen voor één overkoepelende projectgroep met twee Scrumteams daaronder. Vanuit de projectgroep worden een aantal centrale rollen belegd die zorgen voor samenhang, richting en technische aansluiting tussen de teams.

De reden voor deze structuur is dat de specialisaties van de studenten sterk van elkaar verschillen. Zonder duidelijke rolverdeling bestaat het risico dat iedereen zich verliest in zijn eigen onderdeel, terwijl het eindproduct alleen werkt als alle onderdelen goed op elkaar aansluiten.

### Stuurgroep

Deze rollen gelden voor het gehele project en staan boven de scrumteams. 

Het voorstel is om na het derde inlevermoment van dit semester de rollen opnieuw te verdelen, zodat andere teamleden de resterende periode de rol vervullen. Dit gebeurt alleen als zowel medestudenten als de betrokken docent(en) dit zinvol achten.

#### Product Owner

**Aantal:** 1

De Product Owner is verantwoordelijk voor de inhoudelijke richting van het project. Hij of zij bewaakt de scopedocumenten (MoSCoW), stelt prioriteiten en is het aanspreekpunt richting de opdrachtgever. De Product Owner beantwoordt continu de vraag: _bouwen we het juiste?_

**Taken:**

- Bijhouden en bewaken van de projectscope
- Opstellen en prioriteren van de backlog.
- Afstemming met de opdrachtgever (Carla Renders)
- Bewaken dat het team de "waarom" niet uit het oog verliest
- Definitief beslissen wanneer een onderdeel voldoet aan de Definition of Done

#### Technisch Lead

**Aantal:** 1

De Technisch Lead zorgt dat de technische onderdelen van de twee Scrumteams goed op elkaar aansluiten. Hij heeft overzicht over de volledige technische architectuur en signaleert tijdig wanneer keuzes van het ene team invloed hebben op het andere. De Technisch Lead bouwt zelf mee, maar heeft ook een coördinerende rol.

**Taken:**

- Bewaken van de technische architectuur als geheel
- Zorgen dat de AI-stack, backend en infrastructuur op elkaar aansluiten
- Afstemming tussen de scrum teams op technisch vlak
- Beoordelen van technische keuzes en deze documenteren
- Aanspreekpunt voor technische vragen vanuit beide teams

#### Scrum Master

**Aantal:** 1 (gedeeld over beide teams)

De Scrum Master zorgt dat het Scrumproces goed verloopt. Hij of zij organiseert de stand-ups, sprint planningen en retrospectives, en signaleert wanneer een team vastloopt of afdwaalt. De Scrum Master is geen inhoudelijk beslisser, maar een procesbewaker.

**Taken:**

- Organiseren van stand-ups, sprintplanningen en retrospectives
- Bijhouden van de voortgang in beide teams
- Signaleren van blokkades en deze bespreekbaar maken
- Bewaken dat het team op koers blijft met de planning
- Notulen of samenvattingen bijhouden van overlegmomenten

### Scrumteams
De scrumteams zijn ingedeeld op basis van topic, waarbij topic overeenkomt met de specialisatierichting van de opleiding. Dit zorgt ervoor dat elk teamlid werkt vanuit zijn of haar eigen vakgebied en dat de sprint planning en sturing zo dicht mogelijk aansluit bij de individuele leerdoelen van deze periode.

Er zijn vier scrumteams:

- **AI** - 3 studenten
- **Software** - 3 studenten
- **Infrastructuur** - 1 student
- **Business & Data** -1 student

De scrumteams zijn zelfsturend. Zij ontvangen user stories vanuit de stuurgroep, bestaande uit de Product Owner, de Technisch Lead en de Scrum Master, en zijn zelf verantwoordelijk voor backlog refinement en uitvoering binnen hun eigen team. De sprintplanning wordt globaal opgepakt door de stuurgroep.

Alle teams werken op hetzelfde gezamenlijke Jira scrumboard. De Scrum Master beheert dit board en is verantwoordelijk voor het overzicht. Elk team is zelf verantwoordelijk voor de documentatie die nodig is voor de overdracht aan een volgende groep. De Scrum Master bewaakt de voortgang hiervan en bespreekt dit periodiek met de stuurgroep.

#### Subrollen per scrumteam
Elk scrumteam benoemt een aantal subrollen. Deze rollen functioneren als verlengstuk van de stuurgroep, ze zorgen voor een duidelijk aanspreekpunt per team zonder dat de stuurgroep elk detail hoeft bij te houden. De subrollen mogen per sprint wisselen. 

Elk scrumteam benoemt de volgende rollen:

**Board Owner** - aanspreekpunt voor de Scrum Master. Houdt het Jira-board actueel voor het eigen team en signaleert wanneer taken vastlopen of onduidelijk zijn.

**Backlog-vertegenwoordiger** - aanspreekpunt voor de Product Owner. Zorgt dat user stories voor het team voldoende uitgewerkt zijn voordat een sprint begint.

**Documentatie-eigenaar** - aanspreekpunt voor de Technisch Lead. Bewaakt dat de documentatie van het team actueel en overdraagbaar is voor een volgende groep.

### Aandachtspunten

- De Product Owner is het enige aanspreekpunt richting de opdrachtgever, tenzij anders afgesproken. Dit voorkomt verwarring over wie wat heeft beloofd.
- De Technisch Lead heeft de definitieve stem over technische en inhoudelijke keuzes binnen het bouwwerk. De Product Owner heeft de definitieve stem over prioriteiten, scope en wat er opgeleverd wordt richting de opdrachtgever. Bij grote keuzes die beide raken, zoals de keuze van het gespreksmodel, beslissen zij samen. Komen zij er niet uit, dan heeft de Product Owner de doorslaggevende stem.
- Beide Scrumteams werken in dezelfde sprintcyclus en komen minimaal één keer per sprint samen met de volledige projectgroep om voortgang te bespreken en af te stemmen.
- De Scrum Master bewaakt actief dat het team niet alleen bezig is met bouwen, maar ook nadenkt over de "waarom" achter elke keuze. Dit is essentieel voor de documentatie en de overdracht.

### Bronnen

Anthropic. (2026). _Claude Sonnet 4.6_ [Large language model]. Gebruikt als AI-assistent bij het opstellen van dit document. [https://www.anthropic.com](https://www.anthropic.com)

Fontys Hogeschool ICT. (2026, 23 april). _AI-bot sessie_ [Vergaderingstranscriptie].

Fontys Hogeschool ICT. (2026, 28 april). _Projectoverleg rolverdeling en teamindeling_ [Vergaderingstranscriptie].