## Metadata
**Author: ** Bram Wieringa
**Date: ** 26-02-2026
**Version: ** 1.1
**Dependencies: ** OR Planning 003 en Analyse van Knelpunten & Verbetersuggesties versie 2

# 1. Inleiding
Dit document beschrijft de huidige werkwijze (IST) van het OK-planningsproces. Het doel is om een feitelijk fundament te leggen voor procesverbetering. In de huidige situatie wordt de planning gekenmerkt door een hoge mate van handmatige gegevensverwerking en afhankelijkheid van telefonische bereikbaarheid, wat leidt tot een verhoogde kans op fouten en inefficiëntie.

## 1.1 Doelstelling
Het vastleggen van de huidige processtappen als nulmeting voor de voorgestelde automatisering en procesoptimalisatie.

## 1.2 Scope
De scope van dit proces start bij de beoordeling van de chirurgische noodzaak door de medisch specialist en eindigt op de dag van de operatie. Het proces richt zich uitsluitend op de geplande zorg en hoofdzakelijk op de rol van OK-planner.

Acute spoedgevallen vallen buiten de directe procesgang van deze planning. De impact van acute zorg is echter wel aanwezig: spoedoperaties kunnen leiden tot het ad-hoc annuleren van reeds ingeplande patiënten. In de huidige werkwijze dwingt dit de OK-planner om het volledige planningsproces voor de uitgevallen patiënt handmatig opnieuw te doorlopen.

## 1.3 Betrokken Rollen & Systemen
**Rollen**
- Chirurg
- OK Planner
- Screening
- Medical Manager (Dit kunnen verschillende personen zijn maar wordt nu enkele gebruikt om aan te geven dat er geescaleert moet worden, het proces loopt vast)

**Systemen**
- HiX (Elektronisch Patiëntendossier)
- Medspace (Roosterpakket)

# 2. Procesbeschrijving 
Afbeelding proces toevoegen

1. **Aanvraag:** De chirurg start het proces door een Werkorder aan te maken in HiX.
2. **Handmatige Validatie:** De OK-planner voert handmatig controles uit in zowel HiX als indien nodig Medspace om de medische data en de beschikbaarheid van de specialist te verifiëren.
3. **Patiëntcontact:** De patiënt wordt telefonisch benaderd voor het afstemmen van een datum. Dit verloopt via een repetitief proces zonder harde limiet op het aantal weigeringen door de patiënt.
4. **Screening:** Na de initiële planning volgt het screeningstraject. Waar men patient alleen telefonisch bellen als ze binnen 5 werkdagen moet op komen dagen voor de screening.
5. **Beddencontrole:** De cruciale controle op bedbeschikbaarheid vindt pas 2 dagen voor de operatie plaats.

# 3. Knelpunten
Uit de analyse zijn de volgende knelpunten naar voren gekomen:

- **Handmatige Data-afhandeling:** Het opzoeken van informatie in HiX en Medspace gebeurt handmatig. Dit verhoogt de kans op menselijke fouten en vertraagt de start van de planning.
- **Deadlock in Patiëntkeuze:** Er is geen beperking aan hoe vaak een patiënt een voorgestelde datum kan weigeren. Dit leidt tot een oneindige loop in het proces.
- **Inefficiënte Communicatie:** De sterke afhankelijkheid van telefonisch contact in de OK-planning maakt het proces arbeidsintensief. Screening communiceert idealiter via digitale of fysieke post. Het is onduidelijk waarom men dat  niet doet bij de OK-planning.
- **Capaciteitsverlies:** Door de beddencontrole pas 2 dagen van te voren uit te voeren, kan bij een tekort de gereserveerde OK-tijd niet altijd meer effectief worden ingezet voor een andere patiënt.

# 4. Nulmeting: Benodigde data voor onderbouwing
Om de impact van de voorgestelde procesverbeteringen objectief te kunnen meten, is een nulmeting op basis van harde data noodzakelijk. Onderstaande gegevens zijn vereist om de huidige inefficiëntie aan te tonen en de 'Return on Investment' (ROI) van de nieuwe werkwijze te berekenen.

Voor een betrouwbare nulmeting geniet het de voorkeur om deze data direct te extraheren uit de logbestanden van HiX, telefonie-centrale en eventuele andere systemen, om subjectiviteit te voorkomen en een zuiver beeld van de proces-doorlooptijden te verkrijgen.

## 4.1 Operationele Efficiency en Procesintegriteit
- **Annuleringen door beddentekort**
	- **Indicator:** Percentage en absoluut aantal annuleringen vanwege beddentekort twee werkdagen voor aanvang van operatie.
	- **Relevantie:** Deze KPI meet het effect van de voorgestelde Parallel Gateway op vroegtijdige beddencontrole. Het doel is om onnodig capaciteitsverlies op de OK te minimaliseren door logistieke knelpunten eerder in het proces te signaleren.
- **Gemiddelde doorlooptijd per planning**
	- **Indicator:** Het aantal minuten dat een OK-planner gemiddeld besteedt aan het voltooien van één planning (inclusief mislukte belpogingen en handmatige datacorrecties).
	- **Relevantie:** Dit vormt de nulmeting voor de berekening van de tijdswinst na automatisering (API-koppelingen en digitale notificaties).
- **Data-integriteit en herstelwerk**
	- **Indicator:** Het wekelijkse aantal handmatige correcties in de planning door synchronisatieverschillen of typefouten tussen HiX en MEDSPACE.
	- **Relevantie:** Dit kwantificeert de noodzaak om handmatige _User Tasks_ te vervangen door geautomatiseerde _Service Tasks_ (API), wat de foutgevoeligheid verlaagt.

## 4.2 Patiënt- en Procesdynamiek
- **Responsiviteit en kanaalkeuze**
	- **Indicator A:** Frequentie van directe afwijzingen tijdens telefonisch contact versus annuleringen na digitale/postale berichtgeving.
	- **Indicator B:** Het aantal belpogingen voordat een patiënt daadwerkelijk wordt bereikt en de gemiddelde gespreksduur.
	- **Relevantie:** Deze data onderbouwen de transitie naar asynchroon contact (patiëntenportaal/SMS). Het geeft inzicht in of de huidige telefonische benadering efficiënt is of dat digitale zelfservice tot minder procesverstoring leidt.
- **Escalatie en processtagnatie (Deadlocks)**
	- **Indicator:** Het aantal herhaaldelijke afzeggingen per patiënt per operatie. 
	- **Relevantie:** Hiermee wordt de noodzaak voor een escalatieprotocol naar een supervisor aangetoond, om te voorkomen dat specifieke dossiers het planningsproces langdurig blokkeren.
- **Retourstroom na digitale benadering**
	- **Indicator:** Het aantal patiënten dat binnen een vastgesteld tijdsbestek (bijv. 48 uur) na een digitale of fysieke notificatie alsnog telefonisch contact opneemt om de afspraak te wijzigen. (_Hier heb ik veel over zitten denken, en weet het nog steeds niet zeker, maar of die 48 uur relevant is of niet. Ik wil voorkomen dat alle afzeggeing aan het asynchrome worden gekoppeld.)
	- **Relevantie:** Dit meet de effectiviteit van de digitale en fysieke informatievoorziening en voorkomt dat de reden van afzegging onjuist wordt gealloceerd.
- **Klantcontacttijd**
	- **Indicator A (Bereikbaarheid):** Het gemiddeld aantal belpogingen (outbound) dat een OK-planner moet ondernemen voordat er daadwerkelijk een patiënt wordt gesproken.
	- **Indicator B (Gespreksduur):** De gemiddelde duur van het effectieve telefoongesprek (in minuten) waarin de operatie wordt bevestigd of verzet.
	- **Relevantie:** Deze data zijn essentieel voor de business case van een asynchroon systeem (zoals een portaal, SMS, chat).
	    - _Tijdwinst:_ Door de "wachttijd" en de herhaalde belpogingen (synchronisatie-verlies) te elimineren, kan worden berekend hoeveel tijd vrijkomt wanneer de patiënt op een eigen gekozen moment reageert.
	    - _Procesversnelling:_ Het toont aan hoeveel 'dode tijd' er in het proces zit door het proberen te bereiken van niet-beschikbare patiënten.

## 4.3 Kwalitatieve Indicatoren
- **Patiënt- en medewerkerstevredenheid**
	- **Patiënt:** In hoeverre weegt de 'persoonlijke touch' van een telefoongesprek op tegen het gemak van digitale snelheid en duidelijkheid?
	- **Medewerker OK-planners:** De mate waarin OK-planners de huidige administratieve last en het "jagen" op patiënten ervaren als een belasting van hun werkplezier.
	- **Relevantie:** Cruciaal voor het management om de balans te vinden tussen menselijke zorg en procesmatige efficiëntie.
	  
- **Screening "In-Control" ratio**
	-  **Indicator:** Percentage patiënten waarbij de medische screening nog niet volledig is op het moment dat de planner de taak weer oppakt.
	- **Relevantie:** Deze indicator identificeert knelpunten in het voorafgaande screeningsproces die een directe negatieve impact hebben op de workflow van de OK-planning.

# 5. MoSCoW Analyse: Optimalisatie OK-Planning
Hiervoor moet ik eerst mok data generen/

## 5.1 Must Havess

## 5.2 Should Haves

## 5.3 Could Haves

## 5.4 Won´t Have s(voor nu)

# 6. Conclusie

# 7. Bronnen
- Google. (2026). **Gemini (Gemini 3 Flash)** [Large language model]. Geraadpleegd op 28 februari 2026, van [https://gemini.google.com](https://gemini.google.com)
- **Gebruikte prompt:** _"Verbeter deze tekst zodat het vloeiender, leesbaarder en professioneler wordt maar behoud de kern van de tekst."_
- 
# 8. Bijlage


### Over nadenken?
Tijdspad inzetten? Of adviseren het kanban te doen?
