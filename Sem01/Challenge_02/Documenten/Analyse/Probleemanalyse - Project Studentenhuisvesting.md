
## 1. Projectbeschrijving
**Projectnaam:** Studentenhuisvesting  
**Doel:** Ontwikkelen van een IT-oplossing die de belangrijkste operationele problemen van Student Housing B.V. oplost en schaalbaar is voor toekomstige uitbreidingen.  
**Hoofdvraag:** Hoe kan een nieuw IT-systeem het klachtenproces, onderhoudsbeheer en huishoudelijke organisatie binnen studentenhuisvesting efficiënter en inzichtelijker maken?

## 2. Contextanalyse

Student Housing B.V. beheert meerdere studentencomplexen met gedeelde voorzieningen. Het huidige systeem is verouderd en voldoet niet aan de operationele en administratieve eisen. Het nieuwe systeem moet:

- het klachten- en onderhoudsproces optimaliseren;
- opties bieden voor aanvullende diensten;
- inzicht geven in kosten, gebruik en leefomstandigheden;
- starten met een minimale, haalbare MVP;
- werken met beschikbare CSV-exports van het oude systeem.

### 2.1 Overzicht van uitdagingen

#### Operationele problemen
- Onvoldoende naleving van schoonmaak- en huishoudtaken  %%huishouden%%
- Vergeten of onbetaalde gezamenlijke boodschappen   %%huishouden%%
- Afval wordt niet tijdig afgevoerd   %%huishouden / klacht%%
- Ongemelde feestjes of verstoringen  %%klacht%%
- Klachten over verwarming/airco   %%klacht%%
- Storing of slecht onderhoud aan brandalarmen %%onderhoud%% 
- Geen goede traceerbaarheid van onderhoudsdiensten  %%onderhoud%%

#### Nieuwe mogelijkheden (toekomst)
- Delen van studiehulpmiddelen  
- Voorraadbeheer en boodschappenmodule  
- Monitoring van luchtkwaliteit  
- Smart-home integraties  
- Event- en communityfunctionaliteiten  

#### Kostenreductie en inzicht
- Inzicht in energieverbruik  
- Betere onderhoudsplanning
- Inzicht in leefomstandigheden  
- Betere studentplaatsing  
- Minder schadegevallen van studenten aan eigendommen Student Housing B.V.

## 3. Probleemanalyse 

### 3.1 Scope
#### Binnen scope 

- Ontwikkelen van een IT-systeem dat:
	- Via een website benaderbaar is
	- Ondersteuning biedt voor huishoudelijke organisatie
		- Huishoudrooster (schoonmaken, afval buiten zetten, boodschappen doen)
	- Klachtenproces van studenten automatiseert
		- melding, opvolging, feedback
	- Onderhoudsbeer automatiseert 
		- planning, uitvoering, registratie
- Starten met een MVP (Minimal viable product)
- Oude data (CSV-export) is verwerkt in het systeem
- Rollen en rechten
	- Student
	- Beheerder
	- Interne onderhoudsmedewerker
	- Extern onderhoudspartner
- Basisrapportage / Basis dashboard voor kosten, gebruik en leefomgeving

#### Buiten scope
- Geavenceeerde smart home integratie en sensortechnolgie
- Communityfunctionaliteit
	- Evenementen
	- Studiehulpmioddelen delen
	- voorraadbeheer
- Integratie met externe systemen
- Veranderingsproces bij Student Housing B.V.

### 3.2 Deelvragen
1. lorum
2. ipsum

### 3.2 Doelgroep / Gebruikers
#### Studenten
Studenten wonen in de studentenhuizen die Student Housing B.V. aanbiedt. Zij hebben behoefte aan een overzichtelijk systeem waarmee zij klachten kunnen melden, de status van meldingen kunnen volgen en inzicht hebben in de afhandeling. Daarnaast willen zij duidelijkheid over huishoudtaken: wie welke taak uitvoert, wanneer dit moet gebeuren en wat al is gedaan.

#### Beheerders 
Beheerders zijn verantwoordelijk voor het dagelijkse reilen en zeilen binnen de studentenhuizen. Zij moeten inzicht hebben in alle openstaande en afgeronde klachten, de planning en uitvoering van huishoudtaken, de onderhoudsstatus en operationele kosten. Het systeem moet hen ondersteunen bij coördinatie, besluitvorming en communicatie met studenten en onderhoudspartijen.

#### Onderhoudsmedewerker  
Onderhoudsmedewerkers, zowel intern als extern, voeren reparaties en onderhoudstaken uit binnen de studentenhuizen. Zij hebben behoefte aan een duidelijke en actuele takenlijst, met per taak de locatie, omschrijving, prioriteit, benodigde materialen en eventuele veiligheidsinstructies. Het systeem moet hen helpen om werkzaamheden efficiënt en traceerbaar uit te voeren.

#### Onderhoudsmanager
De onderhoudsmanager is verantwoordelijk voor de planning, prioritering en toewijzing van onderhoudstaken. Deze rol vereist inzicht in de totale onderhoudsbehoefte, beschikbare capaciteit, kostenramingen en materiaalgebruik. De onderhoudsmanager moet eenvoudig taken kunnen aanmaken, prioriteiten kunnen wijzigen, voortgang kunnen monitoren en rapportages kunnen genereren.

### 3.3 Beperkingen en voorkeuren
%%Aanvullen en controleren%%
- CSV-data van onbekende kwaliteit  
- Team heeft beperkte ervaring 
- Hardware (Arduino) alleen optioneel na MVP  


### 3.4 Functieanalyse (MoSCoW)
%% dit uitgebreid doornemen met zijn alle%% 
#### Must-have 
- **Webapplicatie (basisplatform)**  
  - Toegang voor studenten, beheerders, onderhoudsmedewerkers en Onderhoudsmanager  
  - Inloggen met rolgebaseerde rechten

- **Klachtenregistratie **  
  - Studenten kunnen een klacht melden  
  - Statusoverzicht per klacht (open, in behandeling, afgerond)  
  - Beheerders kunnen klachten toewijzen, prioriteren en afhandelen  
  - Basishistorie en feedbackmogelijkheid

- **Huishoudrooster**  
  - Aanmaken van huishoudtaken  
  - Automatische of handmatige taakverdeling  
  - Inzicht voor studenten: wie heeft welke taak en wanneer  
  - Taken als uitgevoerd markeren + logging

- **Onderhoudsbeheer**  
  - Takenlijst voor onderhoudsmedewerkers  
  - Toewijzing door beheerder of onderhoudsmanager  
  - Basisregistratie: locatie, omschrijving, status, datum

- **Data**  
  - Eenmalige import van CSV-data  
  - Minimale validatie op verplichte velden

- **Basisdashboard / rapportage**  
  - Overzicht aantal klachten  
  - Status onderhoud  
  - Huishoudtakenoverzicht

#### Should-have
- **Communicatiefunctionaliteit**  
  - Reacties op klachten en onderhoudstaken  
  - Notificaties bij wijzigingen

- **Uitgebreidere onderhoudsflows**  
  - Prioriteitsniveaus  
  - Meerdere medewerkers per taak

- **Verbeteren Data** 
  - Detectie ontbrekende velden  
  - Validatierapport

- **Gebruikersprofielen**  
  - Contactinformatie  
  - Voorkeuren

#### Could-have
- **Documentupload bij klachten**  
  - Foto's, video's, PDF's

- **Kalenderweergave**  
  - Week- en maandplanning

- **Uitgebreide dashboards**  
  - Energieverbruik  
  - SLA-tijden onderhoud

- **Tags en thema’s voor klachten**  
  - Geluid, verwarming, veiligheid, etc.

#### Won’t-have 
- Smart-home integraties (luchtkwaliteit, sensoren, Arduino)  
- Communityfunctionaliteiten (evenementen, hulpmiddelen delen, voorraadbeheer)  
- Integraties met externe systemen  
- Organisatorische veranderprocessen binnen Student Housing B.V.


### 3.5 Use Case (Pixar Pitch)
Er was eens een studentenhuis dat werd beheerd door Student Housing B.V.
Iedere dag worstelden de studenten met het melden van klachten en het bijhouden van huishoudtaken.
Op een dag kwam iemand van Student Housing B.V. met het idee om een webportal te ontwikkelen om deze problemen op te lossen.
En daardoor konden studenten eenvoudig klachten indienen en hadden ze duidelijk inzicht in wie welke taken in het huishouden moest uitvoeren.
Tot op een dag waren de problemen van vroeger opgelost en woonden de studenten een stuk gelukkiger in hun studentenhuis, omdat hun klachten werden gehoord en het huishouden goed geregistreerd en verdeeld was.

### 3.6 Openstaande vragen
%%welke vragen staan er nog open?%%

## 4. Planning
Sprint 0 - Probleemanalyse. website online krijgen

## 5. Technologische analyse
- C#, .NET  
- SQL Server  
- GitHub  
- CSV-import
- Tekst in markdown?
- Diagrammen in Mermaid indien mogelijk anders PlantUML?

## 6. Agile-setup en teamafspraken

### 6.1 Definition of Done
Wanneer is iets klaar? 

### 6.2 Definition of Ready
Wanneer is iets ready

### 6.3 Tools
Welke tools gaan we gebruiken?
- GitHub  
- Visual Studio Code  
- SQL Server  
- Trello
- Obsidian voor tekst en diagrammen?
	- Markdown voor tekst
		- Voordeel, we kunnen de tekst in GIT zetten
	-  Mermaid voor Diagrammen, voldoet mermaid niet dan PlantUML
		- Voordeel Mermaid wordt automatisch gegenereerd op basis van de syntax in Git
		- Syntax is makkelijker aanpasbaar dan graphic tekenen

### Samenwerkingsafspraken
%%Document Rik invoegen%%
GIT Hub als centrale bestanden hub?
	- documenten in markdown
	- code gewoon als code
	- Diagrammen als syntax 
- Rechten en rollen

## 7. Initiële product backlog (MVP)
De initiële product backlog bevat de eerste set van user stories en taken die nodig zijn om het minimale werkende product (MVP) op te leveren. De nadruk ligt op het realiseren van de basisfunctionaliteiten: Website als portaal, klachtenregistratie, huishoudrooster, onderhoudsbeheer en eenvoudige rapportage.

### 7.1 User stories (MVP)
**US-01 - Online portaal**
Als gebruiker van de applicatie wil ik naar een online omgeving gaan om daar alles met betrekking tot Studentenhuizen te regelen

**US-02 - Klachten melden**
Als student wil ik een klacht kunnen indienen. Bij voorkeur gaat dit volgens een formulier waarbij ik kan kiezen uit de meeste voorkomende problemen zodat ik met zo min mogelijk mentale effort de klacht zo duidelijk mgoelijk kan maken. Daarnaast wil ik transperantie van de klacht, kunnen zien wanneer die is ingevuld, wat de status is en wie het behandelt.

**US-3 - Klachten beheren**
Als beheerder wil ik de klachten, die de studenten indienen, kunnen inzien, status geven, toewijzen aan de Onderhoudsmanager en erop kunnen reageren naar de student

**US-4 - 

## 8. Risicoanalyse


## 9. Deliverables Sprint 0
Wat leveren we in sprint 0 op?

## 10. Conclusie
Het MVP bestaat uit:

%%Wat moet er in dit document nog besloten worden:
MoSCoW en wat is de MVP
Tools nalopen en bespreken
Scope en Deelvragen
Alle opmerking nalopen

%%
## Bronnenlijst
**APA-bronvermelding (inclusief AI-prompt):**
OpenAI. (2025, november 11). Prompt gebruikt voor het taalkundig te verbeter en tekst vloeiend te laten lopen [ChatGPT, GPT-5 mini]. Geraadpleegd via https://chat.openai.com

OpenAI. (2025, 9 november). Hoe ziet een sprintplanning eruit [Antwoord van ChatGPT]. ChatGPT. https://chat.openai.com/

