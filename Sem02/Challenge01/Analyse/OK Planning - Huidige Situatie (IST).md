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
De scope van dit proces start bij de beoordeling van de chirurgische noodzaak door de medisch specialist en eindigt op de dag van de operatie. Het proces richt zich uitsluitend op de geplande) zorg.

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

## 4.1 Operationele efficiency en uitval
- **Percentage en absolute aantal annuleringen door beddentekort op moment van geplande operatie**
	- _Data:_ Hoeveel procent van de geplande operaties wordt 48 uur voor aanvang geannuleerd vanwege een gebrek aan bedecapaciteit?
	- _Waarom:_ Dit toont aan of het verplaatsen van de beddencontrole naar voren in het proces (Parallel Gateway) daadwerkelijk capaciteitsverlies op de OK voorkomt.
- **Gemiddelde doorlooptijd per planning**
	- _Data:_ Hoeveel minuten besteedt een OK-planner gemiddeld aan één succesvolle planning (inclusief mislukte belpogingen en handmatige data-check)?
	- _Waarom:_ Dit dient als basis voor de berekening van de tijdsbesparing door automatisering (API-koppelingen en digitale / fysieke notificaties).
- **Foutgevoeligheid en herstelwerk (Data-intregriteit)**
	- _Data:_Hoe vaak per week moet een planning worden aangepast vanwege typefouten of synchronisatieverschillen tussen HIX en MEDSPACE?
	- _Waarom:_Dit kwantificeert de waarde van het automatiseren van handmatige User Tasks naar Service Tasks (API).

## 4.2 Patient- en procesdynamiek
- **Weigerings- en annuleringsfrequentie?**
	- _Data:_ Hoe vaak wijst een patiënt een voorgesteld moment af tijdens een telefonisch contact?
	- _Data:_ Hoe vaak wordt een reeds geplande operatie door de patiënt afgezegd als de patient via de post of digitaal is geïnformeerd over het operatiemoment.?
	- _Waarom:_ Data geeft extra onderbouwing voor het inzetten van een patiëntenportaal voor contact met de patient.
- **Afzeggingsfrequentie en Escalatie (Deadlocks)**
	- _Data:_ Hoe vaak belt een patiënt een operatie af? Dit moet gemeten worden per patient per operatie, om te zien of mensen vaker dezelfde operatie afbellen.
	- _Waarom:_ Deze data dient als onderbouwing voor het instellen van een escalatieprotocol naar een supervisor om processtagnatie te voorkomen.
- **Klantcontact tijd**
	- _Data:_ Na hoeveel belpogingen wordt een patiënt gemiddeld daadwerkelijk gesproken? En voor hoe lang?
	- _Waarom:_ Dit kan ondersteunde werken om ovetegaan naar asynchroon contact via digitale of fysieke post of SMS of andere middel.
	- _Data:_ Hoevaak beld een patient nadat deze digitaal of via de post is benaderd op om een operatie af te zeggen. (hier een tijdlimiet op zetten? Om te voorkomen dat je de reden van afzegging aan het verkeerde gaat tevoegen)
	- _Waarom:_ 

## 4.3 Kwalitatieve Indicatoren

- **Patiënttevredenheid**
    - _Data:_ Patienttevredenheid
    - _Waarom:_ Het management moet kunnen afwegen of de 'persoonlijke touch' van de telefoon opweegt tegen de snelheid en duidelijkheid van digitale post/portaal.    
- **OK-planners Medewerkerstevredenheid:**
    - _Data:_ In hoeverre ervaren planners de huidige handmatige administratie en het "jagen" op patiënten als een belasting voor hun werkplezier?
    - _Waarom:_ Hoe is deze verandering voor de OK-planners
- **Screening "In-Control" ratio**
	-  _Data:_ Percentage patiënten waarbij de medische screening nog niet volledig is op het moment dat de planner de taak oppakt.
	- _Waarom:_ Dit meet eventuele problemen in de screening proces, dat weer effect heeft op de OK-planning

# 5. Moscow parameters
In hoofdstuk 4 werd besproken welke parameters er allemaal handig zouden kunnen zijn om te bepalen wat de ROI is.

# 5. Conclusie

# 6. Bronnen

# 7. Bijlage


### Over nadenken?
Tijdspad inzetten? Of adviseren het kanban te doen?
