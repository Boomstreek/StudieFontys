## Metadata
**Author: ** Bram Wieringa
**Date: ** 01-05-2026
**Version: ** 1.0
**Dependencies: ** 
- Projectscope versie 1.2
- Teamrollen versie 1.1

Dit document komt te vervangen. Ik heb het gemaakt omdat ik een aantal problemen / uitdagingen zie aankomen maar na dit besproken te hebben met Nick en Jurgen ben ik het eens met hun feedback dat we er gewoon tegen aan moeten lopen. We kunnen / we zijn nog niet goed gegneog om alles vooraf af te vangen.

## Inleiding

Dit document beschrijft hoe de scrumteams samenwerken op technische onderdelen die niet onder één enkel team vallen. Per onderdeel is vastgelegd welk team verantwoordelijk is per fase. De Technisch Lead heeft eindverantwoordelijkheid over het geheel en is het eerste escalatiepunt bij onduidelijkheid over eigenaarschap.

## Database

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|Conceptueel model & ERD|Ontwerp van de datastructuur op basis van de projectvereisten|Business & Data|
|Synthetische data bedenken|Verzinnen van realistische mockdata passend bij de projectcontext|AI + Business & Data|
|Seed-bestand maken|Mockdata omzetten naar een bestand waarmee de database in één keer gevuld kan worden|Software|
|Database inrichten & seeden|Centrale database opzetten en vullen met de seed-data|Infrastructuur + Software|
|Beheer tijdens het project|Schemawijzigingen doorvoeren via afstemming met de Technisch Lead|_nader te bepalen_|


## Koppeling frontend–backend–AI

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|API-ontwerp|Definiëren van de interface tussen frontend en AI-backend|Software + AI|
|Implementatie frontend-kant|Bouwen van de koppeling vanuit de interface|Software|
|Implementatie backend-kant|Bouwen van de koppeling vanuit de AI-logica|AI|
|Integratie & testen|Controleren dat de volledige keten werkt|Software + AI|

## Systeemprompt en gespreksmodel

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|Inhoudelijke keuze gespreksmodel|Bepalen welk model gehanteerd wordt en waarom|AI + Product Owner|
|Uitwerken systeemprompt|Vertalen van het gespreksmodel naar concrete promptinstructies|AI|
|Review & accordering|Beoordelen of de prompt aansluit bij de projectdoelen en de opdrachtgever|Product Owner|
|Beheer tijdens het project|Aanpassingen doorvoeren op basis van testresultaten|AI|

## Privacy by design

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|Inventarisatie gegevensstromen|Bepalen welke gebruikersdata waar binnenkomt en opgeslagen wordt|Software + AI + Infrastructuur|
|Technische maatregelen hosting|Borgen van privacy op infrastructuurniveau|Infrastructuur|
|Maatregelen in de applicatie|Zorgen dat de interface geen onnodige data verwerkt of opslaat|Software|
|Maatregelen in de AI-logica|Zorgen dat het gesprek geen gevoelige data onnodig verwerkt|AI|
|Documentatie & overdracht|Vastleggen van alle privacykeuzes voor de volgende groep|Infrastructuur + Technisch Lead|

## Testverantwoordelijkheid

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|Testen gesprekslogica|Kwaliteit en correctheid van de AI-output|AI|
|Testen interface|Werking en bruikbaarheid van de chatbot interface|Software|
|End-to-end test|Testen van het prototype als geheel|Software + AI + Scrum Master|
|Bevindingen rapporteren|Vastleggen van testresultaten en openstaande punten|Scrum Master|

## Dashboard datakoppeling

|Fase|Verantwoordelijkheid|Team|
|---|---|---|
|Bepalen benodigde data|Welke inzichten wil de opdrachtgever zien?|Business & Data + Product Owner|
|Beschikbaar stellen van data|Zorgen dat de juiste data uit de chatbot opvraagbaar is|Software + AI|
|Bouwen van het dashboard|Visualiseren van de data voor de opdrachtgever|Business & Data|
|Koppeling & integratie|Aansluiten van het dashboard op de databron|Business & Data + Software|

## Bronnen

Anthropic. (2026). _Claude Sonnet 4.6_ [Large language model]. Gebruikt als AI-assistent bij het opstellen van dit document. [https://www.anthropic.com](https://www.anthropic.com)

Wieringa, B. (2026). _Projectscope versie 1.2_ [Intern projectdocument]. Fontys Hogeschool ICT.

Wieringa, B. (2026). _Rollen & Teamstructuur versie 1.1_ [Intern projectdocument]. Fontys Hogeschool ICT.