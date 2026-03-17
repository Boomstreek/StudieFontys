---
Title: Design OK-Planning
---

## Metadata
**Author: ** Bram Wieringa
**Date: ** 08-03-2026
**Version: ** 0.1
**Dependencies: ** 
	- Wireframe Dashboard versie 1.1
	- OK Planning - Analyse versie 1.4

# 1. Inleiding
Dit document beschrijft het functionele en visuele ontwerp van het OK-Planning Dashboard. Het ontwerp dient als de concrete uitwerking van het optimalisatieplan voor het OK-planningsproces. Waar de analyse zich richt op het identificeren van inefficiënties zoals handmatige data-opzoeking en late beddencontroles, vertaalt dit design deze problemen naar meetbare en stuurbare visuele elementen.

Het dashboard is ontworpen om te staten met de transformatie van de OK-planner naar een proactieve procesregisseur.

# 2. Doel
Het doel van het ontwerp is tweeledig:

1. **Managementsturing:** Het bieden van real-time inzicht in algemene KPI's zoals doorlooptijden en vullingsgraad om de procesgezondheid te bewaken.
2. **Verbeteringsmonitoring:** Het nauwgezet volgen van de doorgevoerde verbeteringen per specifiek knelpunt (zoals gedefinieerd in de nulmeting) om te bepalen of de interventies het gewenste effect hebben.

# 3. Functioneel Ontwerp & KPI-Mapping
Het dashboard is opgebouwd rondom de vier kritieke knelpunten uit de analyse. Elk element in de wireframe correspondeert met een specifieke indicator uit het optimalisatieplan.

## 3.1 Knelpuntmonitoring

|**Knelpunt in Analyse**|**Visualisatie in Dashboard**|**Doel & Indicator**|
|---|---|---|
|**4.1 Handmatige Data**|Linechart handmatige wijzigingen|Meet de data-frictie door het aantal mutaties op kritieke velden in HiX te monitoren.|
|**4.2 Onbeperkt Weigeren**|Planning patiënten met 2 weigeringen|Identificeert "deadlocks" voor directe escalatie naar een supervisor.|
|**4.3 Late Beddencontrole**|Linechart annuleringen wegens beddentekort|Meet de annuleringen vanwege het gebrek aan een bed na de operatie.|
|**4.4 Telefonische Afhankelijkheid**|Linechart met meerdere lagen, retourstroom, patienttevrdenheid, medewerkerstevredenheiud en gemiddel doorlooptijd planning|Meet de effectiviteit en gevolgen van de transitie naar digitale notificaties.|

## 3.2 Algemene Sturing & Filters
- **Algemene KPI's:** Het dashboard bevat een 'Multi-layered Chart' voor de gemiddelde doorlooptijd, patiënttevredenheid en medewerkerstevredenheid.
- **Tijdssturing:** Alle grafieken kunnen gefilterd worden per dag, week, maand of jaar om zowel kortstondige trends als lange termijn te weergeven.
- **Navigatie:** Een centraal dropdown-menu maakt snelle navigatie tussen de verschillende analysepagina's mogelijk.

# 4. Interface & Visuele Logica
Het design maakt gebruik van een intuïtief kleurensysteem  om de gebruiker direct te informeren over de status van het proces:

- **Groen:** Succes of ruime beschikbaarheid (bijv. >40% reductie in fouten of >5% vrije bedden).
- **Oranje:** We komen in de buurt van succes of de kritieke grens (bijv. 3% bedden vrij).
- **Rood/Zwart:** Kritieke fouten of totale stagnatie (bijv. te veel fouten of 0% bedbeschikbaarheid).

De achtergrondstijl is consistent doorgevoerd over alle pagina's om een rustige en professionele werkomgeving te creëren voor de planner.

# 5. Conclusie
Dit ontwerp vormt de brug tussen de technische achterkant en inzichten in de dagelijkse praktijk van de OK-planning. Door de focus te leggen op de visualisatie van de knelpunten en algemene sturingsinformatie, faciliteert het dashboard een verschuiving naar een datagedreven en efficiëntere manier van werken.

# 6. Bronnenlijst 
**Referentie naar Gemini:** Google. (2026). _Gemini (Gemini 3 Flash)_ [Large language model]. Geraadpleegd op 8 maart 2026, van [https://gemini.google.com](https://gemini.google.com/)

**Referentie naar het ontwerpdocument:**
Wieringa, B. (2026). _OK Planning - Analyse_ (Versie 1.4). 
Wieringa, B. (2026). _Wireframe Dashboard_ (Versie 1.1).

# 7. Bijlage
- Design Dashboard
- Bijlage 7.2: Verantwoording AI-gebruik

## 7.2 Verantwoording AI-gebruik
In overeenstemming met de APA-richtlijnen en de academische integriteit volgt hier een toelichting op het gebruik van kunstmatige intelligentie bij de totstandkoming van dit document:

- **Tool:** Gemini (Gemini 3 Flash), ontwikkeld door Google.
- **Datum van raadpleging:** 8 maart 2026.
- **Toepassing:** De AI is ingezet voor het tekstueel uitwerken en professioneel formuleren van het ontwerpdocument op basis van door de auteur aangeleverde kaders.
- **Inbreng auteur (Kerninhoud):** De volledige inhoudelijke basis is door de auteur aangeleverd. Dit omvat:
    - **Basisopzet:** Een door de auteur opgestelde basistekst en documentopmaak (inclusief titel, metadata en hoofdstukindeling).
    - **Inhoudelijke bronnen:** De volledige analyse van de vier knelpunten en de visuele vertaling hiervan in de wireframe (inclusief kleurlogica en grafiekkeuzes) .
    - **Strategie:** De visie op de rol van de OK-planner en de processturing.
- **Rol van de AI:** Gemini is uitsluitend gebruikt om de door de auteur aangeleverde ruwe teksten, de basisonderwerpen en de functionele mapping tussen de analyse en de wireframe samen te voegen tot een vloeiend en samenhangend geheel.
- **Verificatie:** De definitieve tekst is door de auteur gecontroleerd en waar nodig gecorrigeerd om te waarborgen dat de inhoud exact overeenkomt met de oorspronkelijke analyse en het ontwerp.