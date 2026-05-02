## Metadata
**Author:** Bram Wieringa
**Date:** 02-05-2026
**Version:** 1.0
**Dependencies:**
- Projectscope versie 1.3
- Teamrollen versie 1.1

## 1. Inleiding

Dit document legt de interne samenwerkingsafspraken vast voor het projectteam. Het doel
is dat iedereen weet wat er van hem of haar verwacht wordt, hoe beslissingen worden
genomen en hoe we omgaan met knelpunten. Het document is een levend document en kan gedurende het project worden bijgesteld.

Het team bestaat uit acht studenten verdeeld over vier scrumteams: AI (3), Software (3),
Infrastructuur (1) en Business & Data (1). Boven de scrumteams staat een stuurgroep
bestaande uit de Product Owner, de Technisch Lead en de Scrum Master
(Wieringa, 2026b).

Dit document is bedoeld als samenvatting en eventuele aanvulling op de Projectscope en
de Teamrollen (Wieringa, 2026a; Wieringa, 2026b). Die twee documenten staan altijd
boven dit document wanneer ze tegenstrijdig zijn.

## 2. Rolverdeling & verantwoordelijkheden

De rolverdeling is uitgebreid beschreven in de Teamrollen (Wieringa, 2026b). Hieronder
een beknopte weergave ter referentie.

### Stuurgroep

| Rol | Kernverantwoordelijkheid | Definitieve stem over |
|---|---|---|
| Product Owner | Bewaakt de scope (MoSCoW), prioriteert de backlog en is aanspreekpunt voor de opdrachtgever | Prioriteiten, scope en oplevering richting opdrachtgever |
| Technisch Lead | Bewaakt de technische architectuur als geheel en zorgt dat AI-stack, backend en infrastructuur aansluiten | Technische en inhoudelijke keuzes in het bouwwerk |
| Scrum Master | Bewaakt het Scrumproces, organiseert overlegmomenten en signaleert blokkades | Procesvoering |

Bij grote keuzes die zowel de scope als de techniek raken (zoals de keuze van het
gespreksmodel), beslissen de Product Owner en Technisch Lead samen. Komen zij er niet
uit, dan heeft de Product Owner de doorslaggevende stem.

De Product Owner is het enige aanspreekpunt richting de opdrachtgever, tenzij hier
uitdrukkelijk andere afspraken over worden gemaakt.

### Scrumteams

Elk scrumteam is zelfsturend en verantwoordelijk voor backlog refinement en uitvoering
binnen het eigen vakgebied. Elk team benoemt de volgende subrollen, die per sprint mogen wisselen:

| Subrol | Aanspreekpunt voor | Taak |
|---|---|---|
| Board Owner | Scrum Master | Houdt het Jira-board actueel en signaleert vastgelopen taken |
| Backlog-vertegenwoordiger | Product Owner | Zorgt dat user stories voldoende uitgewerkt zijn vóór sprintstart |
| Documentatie-eigenaar | Technisch Lead | Bewaakt dat documentatie actueel en overdraagbaar is |

> **Roulatie stuurgroep:** Na het derde inlevermoment wordt de rolverdeling opnieuw
> besproken. Andere teamleden kunnen de resterende periode de stuurgroeprol overnemen,
> mits medestudenten en betrokken docent(en) dit zinvol achten (Wieringa, 2026b).

## 3. Communicatieafspraken

### Kanalen

| Doel | Kanaal |
|---|---|
| Dagelijkse communicatie en korte vragen | Teams |
| Vergaderingen en overlegmomenten | Teams (videogesprek) |
| Projectdocumentatie en overdracht | Zie hoofdstuk 6 |
| Taakbeheer en voortgang | Jira |

**Verwachte reactietijd:** Berichten op Teams worden binnen drie dagen beantwoord als je
iemand via @ rechtstreeks een vraag stelt. Bij urgentie bellen we onderling;
contactgegevens staan in contactgegevens.xlsx. Iedereen vult dit bestand zelf in.

### Stand-ups

De wekelijkse stand-up vindt digitaal plaats via Teams op **donderdag om 20:00 uur**.
Heeft een teamlid op dat moment nog les, dan wordt het tijdstip uitgesteld tot na die les.

De Scrum Master notuleert of vat de stand-up samen en verwerkt blokkades in het
Jira-board.

### Volledige projectgroepoverleggen

Beide scrumteams komen minimaal één keer per sprint samen met de volledige
projectgroep. Dit overleg vindt plaats op **dinsdag op school** en is
bedoeld voor voortgangsafstemming en het bespreken van afhankelijkheden tussen teams.

## 4. Besluitvormingsproces

Besluiten worden zo laag mogelijk in de structuur genomen:

- **Binnen een scrumteam:** het team beslist zelf, mits het geen impact heeft op andere
  teams of de architectuur.
- **Technische keuzes met impact op meerdere teams:** de Technisch Lead beslist, in
  afstemming met de betrokken teams.
- **Scope- en prioriteitskeuzes:** de Product Owner beslist, in afstemming met de
  opdrachtgever indien nodig.
- **Keuzes die zowel scope als techniek raken:** Product Owner en Technisch Lead
  besluiten samen. Bij een impasse heeft de Product Owner de doorslaggevende stem.

Alle significante beslissingen worden gedocumenteerd met een korte onderbouwing. Dit is
de verantwoordelijkheid van de documentatie-eigenaar van het betreffende team, in
afstemming met de Technisch Lead.

## 5. Conflictresolutie

Bij een meningsverschil of conflict binnen het team gelden de volgende stappen:

1. **Direct gesprek** - De betrokken partijen bespreken het conflict onderling, zo snel
   mogelijk na het moment dat het ontstaat.
2. **Scrum Master als mediator** - Leidt het directe gesprek niet tot een oplossing, dan
   wordt de Scrum Master ingeschakeld om het gesprek te begeleiden.
3. **Stuurgroep beslist** - Blijft het conflict onopgelost, dan legt de Scrum Master het
   voor aan de volledige stuurgroep. De stuurgroep neemt een bindend besluit op basis van
   projectbelang.
4. **Escalatie naar begeleider** - Pas als de stuurgroep er gezamenlijk niet uitkomt,
   wordt een begeleidende docent ingeschakeld.

Alle stappen worden kort gedocumenteerd door de betrokken deelnemers en gedeeld met de Scrum Master.

## 6. Werken met Jira & sprintritme

### Jira-board

Alle teams werken op één gezamenlijk Jira-scrumboard. De Scrum Master beheert het board en bewaakt het overzicht. Elk team is verantwoordelijk voor het bijhouden van de eigen taken via de Board Owner.

Afspraken:
- Taken worden aangemaakt als user stories of subtaken met een duidelijke omschrijving
  en acceptatiecriteria.
- De status van taken wordt actueel gehouden: minimaal vóór elke stand-up.
- Vastgelopen taken worden gemarkeerd en besproken in de stand-up.

### Sprintritme

| Moment | Frequentie | Verantwoordelijke |
|---|---|---|
| Stand-up | Wekelijks (donderdag 20:00) | Scrum Master |
| Sprintplanning | Per sprint (globaal) | Stuurgroep |
| Backlog refinement | Per sprint, per team | Backlog-vertegenwoordiger |
| Retrospective | Per sprint | Scrum Master |
| Volledig projectgroepoverleg | Minimaal 1x per sprint (dinsdag op school) | Scrum Master |

## 7. Documentatie-afspraken

Goede documentatie is essentieel voor de overdracht aan een volgende projectgroep, zoals ook vastgelegd in de Definition of Done (Wieringa, 2026a). Dit is een gedeelde
verantwoordelijkheid, maar per team belegd bij de documentatie-eigenaar.

Afspraken:
- Elk team houdt eigen documentatie bij die aansluit op de technische en inhoudelijke
  keuzes die worden gemaakt.
- Significante keuzes worden onderbouwd: niet alleen _wat_ er is gekozen, maar ook
  _waarom_.
- De Technisch Lead controleert periodiek of documentatie overdraagbaar is.
- De Scrum Master bewaakt de voortgang van documentatie en bespreekt dit periodiek met
  de stuurgroep.
- Bij de Definition of Done hoort dat alle relevante documentatie is bijgewerkt. De
  Product Owner toetst hieraan.

## 8. Definition of Done (referentie)

De volledige Definition of Done is vastgelegd in de Projectscope (Wieringa, 2026a). Een
onderdeel is klaar wanneer:

- de functionaliteit werkt zoals omschreven in de user story
- de bijbehorende documentatie is bijgewerkt
- de keuzes zijn onderbouwd
- het resultaat overdraagbaar is aan een volgende projectgroep
- de Product Owner heeft bevestigd dat het voldoet

## Bronnen

Wieringa, B. (2026a). *Projectscope – AI-chatbot Sociaal Knooppunt* (Versie 1.3)
[Intern projectdocument]. Fontys Hogeschool ICT.

Wieringa, B. (2026b). *Rollen & teamstructuur – AI-chatbot Sociaal Knooppunt*
(Versie 1.1) [Intern projectdocument]. Fontys Hogeschool ICT.

Anthropic. (2026). *Claude Sonnet 4.6* [Large language model]. Gebruikt als AI-assistent bij het opstellen van dit document. https://www.anthropic.com