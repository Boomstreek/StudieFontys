## Metadata
**Author: ** Bram Wieringa
**Date: ** 27-03-2026
**Version: ** 1.2
**Dependencies: ** 
- OK-Planning - Analyse versie 1.5

## 1. Inleiding
Dit document vormt de transitie van de zorglogistieke analyse (opdracht 1a) naar een financieel managementperspectief (opdracht 1b). De focus verschuift van het optimaliseren van de workflow naar het kwantificeren van de besparingen en de business case achter de digitalisering van het patiëntcontact.

### 1.1 Doelstelling
Het definiëren van de functionele en financiële vereisten voor een Power BI Dashboard. Dit dashboard moet inzichtelijk maken welke kostenbesparing en efficiëntiewinst gerealiseerd worden door de overstap van telefonische acquisitie naar geautomatiseerde asynchrone communicatie.

### 1.2 Scope
De scope van dit project is beperkt tot de **financiële kwantificering** van de transitie binnen het planningsproces. We richten ons specifiek op de vervanging van handmatig, synchroon patiëntcontact (bellen) door geautomatiseerde, asynchrone notificaties (SMS, e-mail, portaal).

- **In scope:**
	- Het berekenen van de huidige operationele kosten (nulmeting) van het belproces.
	- Het definiëren van financiële stuurgetallen (KPI's) voor het Power BI Dashboard.
	- De potentiële besparing op personele capaciteit (FTE) door reductie van _Non-Value Added Time_.
	
- **Out of scope:**
    - De technische implementatie van de notificatie-software.
    - Medische inhoudelijke optimalisatie van de OK-planning zelf.
    - Kosten met betrekking tot de nazorg of facturatieprocessen.

### 1.3 Stakeholders
**Primaire stakeholder:** Manager OK-planners (Focus: Werkdrukverlaging, bezettingsgraad en kostenefficiëntie).

## 2. Probleembeschrijving
Het huidige proces leunt op synchroon contact (bellen). Dit leidt tot "synchronisatieverlies": planners besteden een groot deel van hun tijd aan niet-effectieve handelingen zoals voicemail-loops en herhaalpogingen.

- **Financieel knelpunt:** De hoge 'Kosten per Contact'. Elke succesvolle planning draagt een zware last van indirecte loonkosten door mislukte belpogingen.
- **Kans:** Doorlooptijdverkorting en reductie van administratieve lasten, waardoor de kostbare capaciteit van OK-planners elders of effectiever ingezet kan worden.

## 3. Benodigde data
Om het dashboard te voeden en de business case te onderbouwen, is de volgende data essentieel:

- **Personeelskosten:** Gemiddeld uurtarief (incl. werkgeverslasten) van een OK-planner.
- **Beldata:** Aantal belpogingen per succesvolle afspraak en de gemiddelde gespreksduur.
- **Systeemkosten:** Kosten per SMS/notificatie versus de licentiekosten van het huidige telefoonsysteem.
- **Uitvaldata:** Percentage patiënten dat niet komt opdagen (No-shows) na telefonisch contact versus digitaal contact.


## 4. Benodigde KPI's 
Om de manager te overtuigen van de verbetering, moet het dashboard de volgende kritieke prestatie-indicatoren tonen:

|**KPI**|**Definitie**|**Financiële Invalshoek**|
|---|---|---|
|**Cost per Booking (CPB)**|Totale loonkosten planners / aantal succesvolle planningen.|Maakt de directe besparing per patiënt inzichtelijk door minder handmatige handelingen.|
|**Non-Value Added Time (NVAT)**|Percentage van de werktijd besteed aan mislukte belpogingen en voicemails.|Toont de "verborgen kosten" van inefficiëntie (loonbetaling zonder resultaat).|
|**Digital Adoption Rate**|% van de patiënten dat de afspraak bevestigt via de digitale notificatie.|Bepaalt de ROI van de software; hoe hoger de rate, hoe lager de operationele kosten.|

## 5. MoSCoW Analyse
Voor de ontwikkeling van het Power BI Dashboard hanteren we de volgende prioriteiten, gebaseerd op de KPI’s uit hoofdstuk 4:

### Must Have
- **Financieel nulmeting-overzicht:** Visuele weergave van de huidige **Cost per Booking (CPB)** op basis van handmatig bellen.
- **NVAT-Monitor:** Grafiek die het aandeel 'Non-Value Added Time' (verspilde beltijd) afzet tegen effectieve planningstijd.
- **Adoptie-tracker:** Real-time weergave van de **Digital Adoption Rate** versus handmatige interventies.
    

### Should Have
- **FTE-Besparingscalculator:** Een interactieve slider waarbij de manager ziet hoeveel FTE er vrijkomt wanneer de _Digital Adoption Rate_ stijgt met X%.
- **Efficiency-trend:** Verloop van de CPB over de tijd om de daling van operationele kosten zichtbaar te maken.
- **Respons-analyse:** Inzicht in de tijd tussen verzending notificatie en digitale bevestiging (Latency).

### Could Have
- **Patiënttevredenheid (NPS):** Integratie van feedback om te monitoren of de digitale overstap de patiëntervaring niet schaadt.
- **Screener-Benchmark:** Vergelijking van de proceskosten met de 'screeners' die al asynchroon werken.

### Won't Have
- **Gedetailleerde OK-benutting:** Dit dashboard focust op het _planningsproces_, niet op de medische uitvoering.
- **Facturatiegegevens:** Integratie met declaratiesystemen valt buiten de huidige scope.

## 6. Conclusie
De overstap van een primair telefonisch planningsproces naar een asynchrone, digitale werkwijze is niet enkel een logistieke optimalisatie, maar een noodzakelijke financiële stap. Uit de eerdere analyse (OK-Planning - Analyse) en de bijbehorende BPMN-modellen blijkt dat het huidige "synchronisatieverlies" leidt tot een hoge mate van **Non-Value Added Time (NVAT)**. Dit vormt een significante verborgen kostenpost binnen de OK-planning.

Door de **Cost per Booking (CPB)** te verlagen via een hogere **Digital Adoption Rate**, kan de organisatie de administratieve druk op OK-planners effectief verminderen zonder in te boeten op de kwaliteit van de planning. Het beoogde Power BI Dashboard zal deze transitie kwantificeren door de nulmeting af te zetten tegen de resultaten van de digitale service. Hiermee krijgt de manager een krachtig sturingsinstrument in handen om de business case voor digitalisering financieel te verantwoorden en de personele capaciteit optimaal te benutten.

## 7. Bronvermelding
**Interne Documentatie**
Wieringa, J.C.L. (2026). _OK-Planning - Analyse (versie 1.5 - Opdracht 1a)_. Ongepubliceerd document, Fontys ICT.

**AI-Assistentie**
Gemini (2026). _Ondersteuning bij financiële KPI-formulering, documentstructurering en optimalisatie van spelling en taalbeheersing_. Google AI. Geraadpleegd op 22 maart 2026.