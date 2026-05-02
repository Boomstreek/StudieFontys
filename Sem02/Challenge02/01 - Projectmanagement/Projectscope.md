## Metadata
**Author: ** Bram Wieringa
**Date: ** 02-05-2026
**Version: ** 1.3
**Dependencies: ** 
- Probleemanalyse versie 1.0

## Projectscope - MoSCoW

### AI-chatbot Sociaal Knooppunt

**Projectnaam:** AI-chatbot Sociaal Knooppunt 
**Type:** Werkend ICT-product (Proof of Concept) 
**Werkwijze:** Scrum / iteratieve sprints 
**Doorlooptijd:** ± 9 weken 
**Beoordelingsfocus:** Functionele werking, afbakening en onderbouwing van keuzes

### Inleiding

Dit document beschrijft de scope van het project aan de hand van de MoSCoW-methode. De afbakening is tot stand gekomen op basis van gesprekken met de opdrachtgever en interne afstemming binnen het projectteam. Het doel is een werkend proof-of-concept op te leveren van een AI-chatbot die inwoners van gemeente Boxtel ondersteunt bij het vinden van passende leefstijl- en welzijnsactiviteiten.

### Must have

_Essentieel – zonder deze onderdelen is het project niet geslaagd._

- Een werkend web-based chatbot prototype waarbij:
    - een gebruiker minimaal één volledig gesprek kan doorlopen
    - het gesprek resulteert in een aantoonbare match-output
- Het gesprek is gestructureerd en gebaseerd op exact één erkend gespreksmodel:
    - Positieve Gezondheid (Instituut voor Positieve Gezondheid)
    - of Het Leefstijlroer (Vereniging Arts en Leefstijl)
- De chatbot:
    - toont na afronding maximaal drie meest passende activiteiten
    - is anoniem te gebruiken
    - vraagt uitsluitend contactgegevens wanneer de gebruiker daar zelf expliciet om verzoekt
- De matchinglogica werkt aantoonbaar op basis van:
    - wensen van de gebruiker
    - belemmeringen van de gebruiker
    - leefstijl- en welzijnsvariabelen
- Voor alle benodigde data wordt synthetische (fictieve) data gebruikt
- Primaire doelgroep: inwoners van gemeente Boxtel (15-99 jaar)
- Er worden minimaal twee persona's opgesteld:
    - inwoner (primair)
    - welzijnswerker (secundair)
- Het prototype draait lokaal
- Privacy by design is geborgd binnen de grenzen van een proof of concept:
    - de chatbot verwerkt geen medische gegevens
    - persoonsgegevens worden alleen gevraagd bij een expliciete contactaanvraag
- Projectdocumentatie wordt opgeleverd met:
    - onderbouwing van ontwerp- en technische keuzes
    - beschrijving van het matchingproces

### Should have

_Belangrijk, maar niet strikt noodzakelijk om te slagen._

De chatbot:
- communiceert in het Nederlands op taalniveau B1
- De gebruiker krijgt inzicht in waarom een specifieke activiteit als match is voorgesteld
- Mogelijkheid om contactgegevens achter te laten via:
    - naam en e-mailadres
    - of naam en telefoonnummer
- Visuele of tekstuele toelichting van het matchingproces
- De chatbot is geschikt voor ondersteunend gebruik door professionals zoals welzijnswerkers of zorgprofessionals

### Could have

_Wenselijk, maar alleen indien tijd en capaciteit dit toelaten._

- Geanonimiseerde weergave van aanbieders zonder actieve samenwerking
- Eerste aanzet voor de structuur van toekomstige automatisering van het aanbod
- Beperkte interne inzichten zoals:
    - type gestelde vragen
    - type gegenereerde matches
- UX-verbeteringen in gespreksflow en volgorde van vragen. 
- Voorbereidende ontwerpstap voor toekomstige meertaligheid

### Won't have

_Bewust buiten de scope van dit project gehouden._

- Samenvoeging van de twee gespreksmodellen tot één nieuw model of het uitwerken van het tweede gespreksmodel
- Conceptuele uitwerking van het businessmodel
- Automatisch ophalen of scrapen van actueel aanbod
- Gebruik van echte gemeentelijke, zorg- of medische data
- Opslag of verwerking van medische gegevens
- Validatie van matchkwaliteit met echte inwoners of aanbieders
- Infrastructuur geschikt voor productie- of grootschalig gebruik
- Volledige juridische AVG-uitwerking op productieniveau
- Meertaligheid anders dan Nederlands
- Native mobiele apps (iOS / Android)
- Actieve betalingsafhandeling met aanbieders
- Volledig actueel en dekkend activiteitenoverzicht van gemeente Boxtel
- Volledige inrichting, auditing en garantie van cybersecurity-maatregelen.


### Definition of Done

Het project is afgerond wanneer:

- een gebruiker zelfstandig een volledig gesprek kan voeren met de chatbot
- de chatbot maximaal drie activiteiten toont
- de herkomst van de match inzichtelijk is
- het prototype zelfstandig functioneert
- alle ontwerp-, technische en scopekeuzes zijn gedocumenteerd
- het resultaat overdraagbaar is aan een volgende projectgroep

### Bronnen

Anthropic. (2026). _Claude Sonnet 4.6_ [Large language model]. Gebruikt als AI-assistent bij het opstellen en herzien van dit document. [https://www.anthropic.com](https://www.anthropic.com)

Fontys Hogeschool ICT. (2026, 21 april). _Kennismakingsgesprek AI-groep S2_ [Vergaderingstranscriptie].

Fontys Hogeschool ICT. (2026, 23 april). _AI-bot sessie_ [Vergaderingstranscriptie].

Instituut voor Positieve Gezondheid. (z.d.). _Positieve Gezondheid_. Geraadpleegd op 26 april 2026, van [https://www.iph.nl](https://www.iph.nl)

Stichting Richter Education. (z.d.). _Leergebied® Gezond_. Geraadpleegd op 26 april 2026, van [https://www.richter.education](https://www.richter.education)

Vereniging Arts en Leefstijl. (z.d.). _Het Leefstijlroer_. Geraadpleegd op 26 april 2026, van [https://www.artsenleefstijl.nl/leefstijlroer](https://www.artsenleefstijl.nl/leefstijlroer)