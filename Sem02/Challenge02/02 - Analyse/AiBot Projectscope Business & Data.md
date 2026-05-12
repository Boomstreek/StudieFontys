## Metadata
**Author: ** Bram Wieringa
**Date: ** 12-05-2026
**Version: ** 1.0
**Dependencies: **
- Projectscope
- HappyFlow
- Probleemanalyse

## Inleiding

Dit document beschrijft de scope van het Power BI dashboard dat meet of de AI-chatbot van Stichting Richter Education een succes is. Het dashboard is bedoeld voor de opdrachtgever (de stakeholder) en het projectteam.

Om te bepalen wat succes is, is eerst de kernvraag gesteld: wat doen we eigenlijk en waarom? We maken een chatbot om mensen die iets willen doen met leefstijlverbetering te koppelen aan een passende activiteit. De vraag is dan: werkt dat ook écht?

Om dat te beantwoorden moet het dashboard langs vier dimensies meten:

1. **Gebruik** – wordt de chatbot daadwerkelijk gebruikt?
2. **Kwaliteit van de match** – klopt het advies dat de chatbot geeft?
3. **Gebruikerservaring** – vinden inwoners de chatbot prettig en begrijpelijk?
4. **Impact** – leidt de chatbot tot echte deelname aan activiteiten?

> **Databenadering:** Het dashboard wordt gebouwd en gedemonstreerd met synthetische (fictieve) data. Dit sluit aan op de keuze in de projectscope van de chatbot zelf. De koppeling met echte chatbot-data is een Could have en wordt alleen gerealiseerd als tijd het toelaat.

## Projectscope – MoSCoW

### Must have

_Essentieel – zonder deze onderdelen is het dashboard niet geslaagd._

- Een werkend Power BI dashboard met twee pagina's, met daarop twee veschillende dimensies.
- Alle visualisaties draaien op synthetische data
- **Dimensie 1 - Gebruik:**
    - Aantal gestarte gesprekken per week (lijndiagram)
    - Voltooiingspercentage (KPI-card)
    - Trechtervisualisatie: gestart → voltooid → match getoond
    - Verdeling instroomtype (precies / beetje / helemaal niet)
- **Dimensie 2 - Matchkwaliteit:**
    - Match-acceptatierate (KPI-card)
    - Verdeling matches per Leefstijlroer-pijler (staafdiagram)
    - Percentage "geen match gevonden" (KPI-card)
- **Dimensie 3 - Gebruikerservaring:**
    - Gemiddelde gebruikersscore (gauge of KPI-card)
    - Gemiddelde gesprekslengte in minuten (KPI-card)
    - Percentage contactgegevens achtergelaten (KPI-card)
- **Dimensie 4 - Impact:**
    - Percentage doorverwijzingen met opvolging (KPI-card)
    - Percentage dat leidt tot deelname aan activiteit (KPI-card)
    - Bereik kwetsbare doelgroep (gebruikers via professional, %)
- Het dashboard verwerkt geen persoonsgegevens

### Should have

_Belangrijk, maar niet strikt noodzakelijk om te slagen._

- De overige twee dimensies uitgewerkt
- Tijdfilter op weekniveau zodat trends zichtbaar zijn
- Uitsplitsing afhaakpunt per gespreksstap
- Gebruik per apparaattype (desktop vs. mobiel)
- Overzicht nieuwe activiteitsverzoeken (activiteiten die niet bestaan maar wel gewenst zijn)
- Opmaak conform huisstijl Stichting Richter Education

### Could have

_Wenselijk als tijd het toelaat – inclusief koppeling met echte data._

- Live koppeling met chatbot-backend (REST API of geplande CSV-export) ter vervanging van synthetische data
- Automatische dagelijkse refresh van de data
- Drillthrough per activiteit: welke activiteit wordt het vaakst gematcht en opgevolgd?

### Won't have

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