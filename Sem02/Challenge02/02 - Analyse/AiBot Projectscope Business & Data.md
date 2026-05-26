## Metadata
**Author: ** Bram Wieringa
**Date: ** 17-05-2026
**Version: ** 1.1
**Dependencies: **
- Projectscope
- HappyFlow
- Probleemanalyse

## Inleiding

Dit document beschrijft de scope van het Power BI dashboard dat meet of de AI-chatbot van Stichting Richter Education een succes is. Het dashboard is bedoeld voor de opdrachtgever (de stakeholder) en het projectteam.

Om te bepalen wat succes is, is eerst de kernvraag gesteld: wat doen we eigenlijk en waarom? We maken een chatbot om mensen die iets willen doen met leefstijlverbetering te koppelen aan een passende activiteit. De vraag is dan: werkt dat ook écht?

Om dat te beantwoorden meet het dashboard langs vijf dimensies:

1. **Gebruik** - wordt de chatbot daadwerkelijk gebruikt?
2. **Leefstijlscore** - wat is het profiel van de gebruikers die de chatbot bereikt?
3. **Matchkwaliteit** - klopt het advies dat de chatbot geeft?
4. **Gebruikerservaring** - vinden inwoners de chatbot prettig en begrijpelijk?
5. **Impact** - leidt de chatbot tot echte deelname aan activiteiten?

Dimensies 1 en 2 zijn essentieel en vormen de Must have. Dimensies 3 en 4 zijn belangrijk en vallen onder de Should have. Dimensie 5 is wenselijk en wordt alleen uitgewerkt als tijd het toelaat (Could have).

> **Databenadering:** Het dashboard wordt gebouwd en gedemonstreerd met synthetische (fictieve) data. Dit sluit aan op de keuze in de projectscope van de chatbot zelf. De koppeling met echte chatbot-data is een Could have en wordt alleen gerealiseerd als tijd het toelaat.

## Must have

_Essentieel – zonder deze onderdelen is het dashboard niet geslaagd._

- Een werkend Power BI dashboard met twee pagina's, met daarop twee dimensies
- Alle visualisaties draaien op synthetische data
- Het dashboard verwerkt geen persoonsgegevens

**Dimensie 1 – Gebruik:**

- Aantal gestarte gesprekken per week (lijndiagram)
- Voltooiingspercentage (KPI-card)
- Trechtervisualisatie: gestart → voltooid → match getoond
- Verdeling instroomtype (precies / beetje / helemaal niet weten wat je zoekt)

**Dimensie 2 – Leefstijlscore:**

- Verdeling van leefstijlscores onder gebruikers (histogram: hoeveel mensen scoren laag / gemiddeld / hoog)
- Gemiddelde leefstijlscore per gemeente (staafdiagram)
- Score uitgesplitst per Leefstijlroer-pijler (voeding, beweging, ontspanning, slaap, verbinding, middelen)

## Should have

_Belangrijk, maar niet strikt noodzakelijk om te slagen._

- Tijdfilter op weekniveau zodat trends zichtbaar zijn
- Opmaak conform huisstijl Stichting Richter Education
- Uitwerking van data dat de happy flow volgt

**Dimensie 3 – Matchkwaliteit:**

- Match-acceptatierate (KPI-card)
- Verdeling matches per Leefstijlroer-pijler (staafdiagram)
- Percentage "geen match gevonden" (KPI-card)
- Overzicht nieuwe activiteitsverzoeken (activiteiten die niet bestaan maar wel gewenst zijn)

**Dimensie 4 – Gebruikerservaring:**

- Gemiddelde gebruikersscore (gauge of KPI-card)
- Gemiddelde gesprekslengte in minuten (KPI-card)
- Percentage contactgegevens achtergelaten (KPI-card)

## Could have

_Wenselijk als tijd het toelaat._

**Dimensie 5 – Impact:**

- Percentage doorverwijzingen met opvolging (KPI-card)
- Percentage dat leidt tot deelname aan activiteit (KPI-card)
- Bereik kwetsbare doelgroep (gebruikers via professional, %)
- Vergelijking gemiddelde leefstijlscore vóór en ná deelname aan activiteit

**Technisch:**

- Live koppeling met chatbot-backend (REST API of geplande CSV-export) ter vervanging van synthetische data
- Gebruik per apparaattype (desktop vs. mobiel)
- Uitsplitsing afhaakpunt per gespreksstap
- Automatische dagelijkse refresh van de data
- Drillthrough per activiteit: welke activiteit wordt het vaakst gematcht en opgevolgd?

## Won't have

_Buiten scope voor deze versie._

- Individuele gebruikersprofielen of herleidbare persoonsgegevens
- Real-time livestream van gesprekken
- Meertalige weergave van het dashboard
- Integratie met andere externe systemen buiten chatbot-backend

## Vervolgstappen

1. Synthetische dataset aanmaken
2. Power BI dashboard bouwen per dimensie (Must have/Should Have)
3. Should have inbouwen waar tijd het toelaat
4. Could have: live koppeling zodra chatbot-backend sessie-logs wegschrijft

## Bronnen

Anthropic. (2026). *Claude* (claude-sonnet-4-6) [Large language model; gebruikt voor het opstellen van de opzet en controle van de KPI-structuur, MoSCoW-scope en datavelddefinities op basis van projectdocumenten]. https://www.anthropic.com

Wieringa, B. (2026, 26 april). *Probleemanalyse AI-chatbot "Het Sociaal Knooppunt"* (Versie 1.0). Stichting Richter Education.

Wieringa, B. (2026, 4 mei). *Projectscope AI-chatbot Sociaal Knooppunt* (Versie 1.4). Stichting Richter Education.

Wieringa, B. (2026). *Happy Flow AI-chatbot Sociaal Knooppunt* (Versie 1.1). Stichting Richter Education.