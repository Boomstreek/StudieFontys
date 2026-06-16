## Metadata
**Author: ** Bram Wieringa
**Date: ** 16-06-2026
**Version: ** 1.0
**Dependencies: **
- versie1_2_Gebruik.jpg 
- versie1_2_Leefstijl.jpg

## Inleiding
Dit document bevat een toelichting op het Power BI-dashboard dat is ontwikkeld ter ondersteuning van de monitoring van een AI-gedreven leefstijlcoach-chatbot. Het dashboard bestaat uit twee pagina's: **Gebruik** en **Leefstijl**. Samen geven zij inzicht in zowel het operationele gebruik van de tool als de inhoudelijke leefstijlresultaten van de gebruikers.

## Voor wie is het dashboard?

Het dashboard is primair bedoeld voor één typen gebruikers:

- **Bestuur van de stichting:** Voor het aantonen van maatschappelijke impact richting gemeenteraden en financiers en te beoordelen of het AI bot werkt een succes is en verder investering rechtvaardigt

## Dashboard 'Gebruik'

Dit dashboard toetst de prestaties en het gebruik van de AI-chatbot. Er worden drie kernvragen beantwoord:

- **Volume:** Wanneer en hoeveel gesprekken starten er?
- **Retentie:** Worden de sessies succesvol voltooid?
- **Klantbehoefte:** Willen gebruikers na afloop de matches zien?

### Gesprekken door de tijd

De bovenste grafiek toont het aantal gesprekken per dag over de periode april 2023 t/m november 2024. Het verloop is volatiel, met regelmatige pieken en dalen, wat duidt op variabele instroom of het gebruik van mockdata. Via de tijdsslider kan de weergave worden verfijnd.

### Kerncijfers

Rechts op de pagina worden drie kerncijfers getoond:

- **Voltooiingspercentage: 82%** een sterk resultaat dat aangeeft dat de overgrote meerderheid van gestarte gesprekken ook wordt afgerond.
- **Gesprekken gestart: 3K** het totaal aantal gestarte sessies in de geselecteerde periode.
- **Matches getoond: 1.444K** het aantal keren dat aan de gebruiker daadwerkelijk de  matches is getoond.

### Instroom per bron

De donutgrafiek toont via welk kanaal gebruikers zijn binnengekomen:

- **Huisarts verwijzing**
- **Werkgever doorverwijzing**
- **Zelfaanmelding**
- **Zorgverzekeraar initiatie**
- **GGD doorverwijzing**

### Conversietrechter

Het staafdiagram toont de voortgang van gesprekken door het proces:

|Stap|Aantal|betekenis|
|---|---|---|
|Gestarte gesprekken|2.500|aantal gesprekken dat door de gebruiker is gestart|
|Voltooide gesprekken|2.053|aantal gesprekken die tot net na de laatste vraag minimaal zijn gekomen|
|Match resultaten opgevraagd|1.444|hoeveel gebruikers vragen daarna de matches op|

## Dashboard 'Leefstijl'

Dit dashboard toont de leefstijlresultaten van gebruikers, uitgesplitst per gemeente (dorpskern). De pagina is speciaal ontworpen voor de stichting om richting de gemeenteraad de maatschappelijke impact aan te tonen.

### Gemiddeld rapportcijfer per pijler

De staafgrafiek linksboven toont de gemiddelde scores op zes leefstijlpijlers. De scores liggen dicht bij elkaar, allemaal rond de 6, wat een uniform beeld geeft van de leefstijlkwaliteit en aantoont dat er gebruik gemaakt is van mockdata:

|Pijler|Indicatie|
|---|---|
|Gem. Beweging|~6|
|Gem. Middelen|~6|
|Gem. Slaap|~6|
|Gem. Verbinding|~6|
|Gem. Voeding|~6|
|Gem. Ontspanning|~6|

### Gemiddelde score per gemeente

De horizontale staafgrafiek toont de gemiddelde totaalscore per gemeente. Liempde en Lennisheuvel scoren het hoogst, terwijl Esch en Boxtel iets lager uitkomen. Dit geeft inzicht in geografische verschillen in leefstijlgezondheid binnen het werkgebied.

### Boxplot – spreiding per gemeente

De boxplot geeft een gedetailleerder beeld van de spreiding van de geselecteerde pijler per gemeente. De mediaan ligt voor de meeste gemeenten rond 6, maar de spreiding varieert: sommige gemeenten kennen een bandbreedte van score 3 tot 9. Dit wijst op grote individuele verschillen binnen gemeenten.

### Samenvattende Kerncijfers

|Kerncijfer|Waarde|Betekenis|
|---|---|---|
|Gem. Score|4,95|Gemiddelde totaalscore over geselecteerde filters|
|% Score ≤4|32,40%|Aandeel gebruikers met lage score (risicogroep)|
|% Score ≥7|4,08%|Aandeel gebruikers met hoge score (best presterende groep)|

## Conclusie & aandachtspunten

De twee dashboardpagina's bieden samen een volledig beeld van zowel het operationele gebruik als de inhoudelijke impact van de AI-chatbot:

- Het hoge voltooiingspercentage (82%) en de brede instroom via meerdere kanalen wijzen op een goed functionerende en goed bereikbare tool.
- De leefstijlscores laten zien dat er gemeentelijke verschillen zijn en dat een significante groep (32,4%) een lage gemiddelde score heeft, wat het belang van de interventie onderbouwt.

**Aandachtspunten voor doorontwikkeling:**

- Verdere verdieping op de lage-score-groep (32,4% scoort ≤4)
- Analyse van seizoenspatronen in het gebruik
- Uitbreiding van de monitoring op instroombronnen

## Bronnen

Anthropic. (2026). _Claude_ (Sonnet 4.6) [Grote taalmodel]. Gebruikt voor het opstellen van begeleidende tekst op basis van visuele dashboard-invoer. Prompt: _"schrijf een begeleidende tekst met uitleg over mijn dashboard op basis van mijn concept"_ en vervolgvragen over opmaak, bronvermelding en APA-stijl. [https://www.anthropic.com](https://www.anthropic.com)

Wieringa, B. (2026). _Gebruik_ [Power BI-schermafbeelding]. versie1_2_Gebruik.jpg

Wieringa, B. (2026). _Leefstijl_ [Power BI-schermafbeelding]. versie1_2_Leefstijl.jpg