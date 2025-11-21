Wat heb ik geleerd

# Les 1
## SQL, R & Python belangrijk voor data-visualisatie
### [[Werkboek R]] en [[datacamp.com]]
## Test dashboards altijd met testdata! Klopt de pi chart wel met 50/50 of laat die bij 50/50 20/80 zien.
## Pas op met open tekstvelden, dan moet je eerst alles categoriseren voordat je het kan visualiseren. 

# Les 2
## Data is storytelling
### Het verhaal kunnen vertellen over: het proces, de wens en de opdrachtgever
## Vragen:
### Uni-variate vs histogram, wat is het verschil

# Les 3
## [[ER Diagram]] basis
## [[Chen notatie]]
## Visual paradigm
## Vragen
### Wat is het verschil tussen [[ER Diagram]] en [[EER Diagram]]
#### Verschil is: 
### Welke notaties zijn er nog meer?
#### [[Chen notatie]]
#### [[Crow's foot notatie]]
#### meer?
##### Waarom kies je de een en niet de ander?
### Waarom N:M en niet N:N, verschil daartussen
####  N is 0, 1 of meer en M is 1, 2, of meer, maar dit staat niet vast

# Les 4 – Van ER-diagram naar Database

## Recap ER-diagram
- Basis voor: klasse diagram en database  
- **Entiteiten:** rechthoek  
- **Attributen:** ovaal  
- **Relaties:** ruit (met naam en kardinaliteit)  
- **Tools:** Virtual Paradigm, SmartDraw, Canva, Edraw  
- **Notatie:** Chen-notatie  

## Database
- Relaties kunnen ook attributen hebben  

### Stap 1 – Tabellen maken
- Elke entiteit (rechthoek) wordt een tabel  
- Elk veld heeft een unieke ID (meestal integer)  

### Stap 2 – Attributen toevoegen
- Voeg alle attributen van de entiteit toe aan de tabel  

### Stap 3 – Relaties omzetten
- Kardinaliteit: 0, 1 of n  
- **Foreign key:** verwijst naar ID in een andere tabel  
- **Bij n–n relaties:** maak een **koppeltabel**  
  - Naam: combineer de twee entiteiten of verzin een zinvolle naam  
  - Voeg attributen van de relatie toe  

**Voorbeelden:**  
- `Patient – Medicijn` → `PatientMedicijn(PatientID, MedicijnID, Aantal, Tijdstip)`  
- `Patient – Docter` → `Behandelaar(PatientID, DocterID)` (combinatie is uniek, geen aparte ID nodig)  

### Foreign key gedrag bij verwijderen
1. **Mandatory:** verwijderen verboden als er nog koppelingen zijn  
2. **Cascade:** verwijdert automatisch alle gekoppelde records  
3. **Set to null:** verwijst naar null bij verwijdering  

## Extra notities
- **Crow’s foot notatie:**  
  - `0` = 0 of 1  
  - `1` = altijd minstens 1  
  - Meer info: [Crow's Foot ERD Tutorial](https://medium.com/@callista.m.azizah/crows-foot-erd-for-beginners-a-tutorial-1effc8a326c6R)  

- **Praktisch:**  
  - Student Square portal: eigen database maken  
  - Azure Data Studio kan ook (SQL Server)  
  - Mockaroo.com: random data genereren  
  - R Studio script beschikbaar om verbinding te maken met SQL Server en data uit Excel te uploaden (script bij Kees)  

## Wat je hebt geleerd
- Koppeltabellen maken bij n–n relaties  
- Crow’s foot notatie begrijpen  
- ER-diagram vertalen naar een database voor je applicatie

# Les 5 Basis procesmodelener
waarde toe brengen aan de organisatie

Karakteristiek van een proces
- Doel gericht, wanneer endigt het proces of wanneer is het doel bereikt
- Stap-voor-stap, duidelijke stsappen
- Herhaalbaar, kan je telkens opnieuw op de zelfde manier doen
- gedfineert door input en output, beignpunt en eindepunt
- meetbaar, hoeveel tyijd kost elke stap, kwaliteit van de output, vorm, formaat, kwaliteit, waarde
- Triggerd, trigger is de gene die het proces start kicks off

levels of controle
- prodcutie process
- busniss porcies
- work porcess
- task
- act

ovalen zijn start en stop
rechthoek is activiteit
ruit/diamond is keuze
pijlen geven de flow aan

alles heeft een voorganger en een opvolger behable de de ovalen start en stop

![procesDiagramSymbolen](procesDiagramSymbolen.png)

BV management notatie? BPMN Business process model notation

op school gebruiken ze visual pardaigm

```plantuml
@startbpmn
start

partition "L'Unspecifice" {
  :Lege schaaljes aanvullen;
  :Mis-en-place maken;
  if (Zijn er lege schaaljes?) then (ja)
  else (nee)
    :Lege schaaljes aanvullen;
  endif
}

partition "Runners" {
  :Voorraadtekort bij pakker;
  :Haal schaaltje op;
  :Was schaaltje af;
  :Breng naar pakkers;
}

partition "Pakker" {
  :Brootbox Pakker;
  :Klamtopdracht;
  :Box op de lijn;
  :Produceren eindproducten;
}

partition "Chef" {
  :Iwenties controle;
  :Box controleren;
}

stop
@endbpmn
```
```mermaid
bpmnGraph
    %% Processen
    subgraph Srijder [L'Unspecifice]
        task1[Lege schaaljes aanvullen]
        task2[Mis-en-place maken]
        gateway1{Zijn er lege schaaljes?}
    end

    subgraph Runners
        task3[Voorraadtekort bij pakker]
        task4[Haal schaaltje op]
        task5[Was schaaltje af]
        task6[Breng naar pakkers]
    end

    subgraph Pakker
        task7[Brootbox Pakker]
        task8[Klamtopdracht]
        task9[Box op de lijn]
        task10[Produceren eindproducten]
    end

    subgraph Chef
        task11[Iwenties controle]
        task12[Box controleren]
    end

    %% Verbindingen
    gateway1 -->|Nee| task1
    gateway1 -->|Ja| task3
    task3 --> task4 --> task5 --> task6
    task6 --> task7 --> task8 --> task9 --> task10
    task10 --> task11 --> task12
    task12 --> gateway1
```
```mermaid
bpmnGraph
    start
    gateway1{Zijn er lege schaaljes?}
    
    task1[Lege schaaljes aanvullen]
    task2[Mis-en-place maken]
    task3[Voorraadtekort bij pakker]
    task4[Haal schaaltje op]
    task5[Was schaaltje af]
    task6[Breng naar pakkers]
    task7[Brootbox Pakker]
    task8[Klamtopdracht]
    task9[Box op de lijn]
    task10[Produceren eindproducten]
    task11[Iwenties controle]
    task12[Box controleren]
    end

    start --> gateway1
    gateway1 -->|Nee| task1 --> task2 --> gateway1
    gateway1 -->|Ja| task3 --> task4 --> task5 --> task6
    task6 --> task7 --> task8 --> task9 --> task10
    task10 --> task11 --> task12 --> gateway1
```


Les 6 Strategie en performance
Wat is een missie?
Slechte missiom statement zijn bucket list items, gebaseerd op marktpositie winst of omzet
Missiestatement
waar staan we voor 
waarde

Visie
Waar gaan we voor

Belangrijk om dit uit elkaar teh ouden Missie en Visie, Misssie wie ben ik en Visie wat wil ik doen

missie statement moet je een idee geven welk bedrijf het is, raadbaar in elk geval de juiste richting

missie vissie dat hoort bij dit merk

Strategie is voor 3-5 jaar
huidige positie ga je vanuit
	- 5 krachten van porter
	- 6w model van farreell
	- swot analyse

bijvoorbeeld met
	 - value strategy tract wiersema (focus bedrijf)
	 - competition strategy porter

volgens tracy en wiesema
strategie 
- product leaderschip
focus op
beste product

customer intemcy -> beste opllosing voor de klatn

operational excellence -> beste opbrengst

waardestrategien, belanse van de strategie

Hoe kies je tussen de verschillende doelen als ze met elkaar bijten?
- de cijfers worden anders, je kiest ze neit alle 3 het is een trade off
- je kiezt meer

als je hebt gekozen, wat ga ik dan meten? Critice performence
klant teveredenheid -> klantentrouw
gemotiveerde mederwerkers -> medewerkerbetrokkkenheid
innovatie -> activie vernieuwing

daarna
key performance
klantentrouw -> aantal terugekerende klnaten per jaar
medewerkesbetrokkenheid -> score medewerkers
actieve verniwueing -> aantal nnieuwe producten per jaar

KPI's moeten zijn smart, speciefiek meetbaar acceptable, realistisch, tijdsgebonden
je meet kpis in een eenheid

wat is voldoende, wat is goed, wat is onvoldoende ofdaar willen we uitkomen

je meet kpis op data binnen je bedrijfsproces, dus omslagpunt in je bedrijfsproces, dus van bakker naar verkoper is bijvoorbeeld een opslagpunt

missie
bestaansrecht van ondernemening
visie
waar gaan we voor
strategie
palan 3-5 jaar
csfs welek factoren zijn belangirjk
cscs wat gaan we dan meten
kpis wat meten we het en wanner is het goed

kpi bewijzen dat het werkt of niet in de echte wereld, die succes bewijzen in de relle werdel en zo een indicatie zijn voor de missie.vissie/strategie

systeem wereld - reele wereld -> doel 
hoe kunnen we vanuit de systeem wereld de intentie het doel vertifieren 

hierdoor zorgt dat de proffesional zicht mikt op de klant

door kpis worden het doel niet de reele wereld maar dan wordt het doel de systeem wereld

hier hebben wij bij mijn werk last van, reele wereld en de systeem werredl
(verdraaide organisaties) wouter hart
rens van der vorst Dont mention the VAR

blijf alert bij kpis waarom wouden we dit meten en blijft dit het doel halen

uiteindelijk wint de systeemwereld altijd
- toeslagenschandaal
- identisiteitsfraude

volgende keer, hoe je de meting kan vertalen naar dashboard. Pakken we stukje proces met applicatie 

Dashboarding, fontys data github website nakijken

%% raw
# uitleg business model canvas

bestaat uit 9 dingen

hij heeft net iets gedeelte ergens, de buisness model canvas

filmpje:
je orgineerst het per functie

maarn u doen we het anders

stap 2 value proposition:
wat doe je en voor wie
(solving a problem or a need, not a idea or product) (verschil tussen problem en need)

Meer kunnen genieten van het  leven door sociaal te bewegen: is een voorbeeld

stap 2 the customer 
who arethey and why would they buy? you exist for them

customer archtype, customer persona maken
- geographic
- social
- demographic

mensen met een kleinere sociale netwerk, t

ouderen 60-80 die fitter willen worden maar een drempel overheen moeten om het te gaan doen.

er zijn er nog veel meer, ze moeten allemaal naar voren komen

Stap 3: Channels
hoe bereikt je value proposition je customer, door distrubution channel

fysiek of digitaal?

doorverwijzing via fysiotherapeut , zo dicht mogelijk bij de persoon komen

stap 4: customer relationship
how do i get customers, how do i keep them, how do i grow them?

>get>-keep->grow> en weer terug naar get

Hoe hou je de mensen vast? Gerzellig

stap 5: Revenua stream
what value is de customer paying for . Ditrect sale, freemium model, lincens en subscription model is anders dan de pricing tactics?

financiele opbrengesten en social opbrengsten of andere opbrengsten. Zoals awerness van cyberveiligheid

Dit staat in de course? waar staat de course dan? 

stap 6: resources
what are the key resources? welke assets zijn belagnrijk? Veel geld, veel leen geld, fabricatiemachines, autos, intuelectual, pattants, custromers, humans that work or something else?

social coach, ruimte, muziek, 

stap 7: Partners
who are your key partners? what are we aquirering for us, what activiteits are tehy doing for you and when?

joint ventures

huisartsenpraktijk, zorginstelling, zwenbadeb,

iets met zorgverzekering betaalt het? customer segment?

PRaktische tip: doe dit op post its, zodat je kan switchen makkelijk

stap 8: activities

what is the most important thing you need to do to make the busniss work?

key activitiets you need to become expert at? 

Stap 9: Cost ??
cost what are fixed cost

opdracht is om dit toe te passen in je project

namen bij customer segment en keypartners, dat is raar. Keypartnet helpt met waardere creeeren dus die stuur je geen rekenen.

Maandag kijken customer segment die we nog meer een plek kunnen geven. Template is ontvangen ga hiermee aan de slag

expert tafel rond 19:30
exper
%%

# Business Model Canvas – Verbeterde Les-Samenvatting

Het **Business Model Canvas (BMC)** bestaat uit **9 bouwstenen**. In de les werd eerst de klassieke uitleg gedeeld, maar vervolgens werkten we het **per functie/onderdeel** verder uit.  

## 1. Value Proposition (Stap 2 in de les)  
**Wat doe je en voor wie?**  
Een value proposition lost **een probleem of een behoefte (need)** op. Het gaat dus **niet** om het verkopen van een idee of product, maar om het oplossen van iets dat de klant ervaart.

**Voorbeeld:**  
*“Meer kunnen genieten van het leven door sociaal te bewegen.”*

## 2. Customer Segments (Stap 2 – The Customer)  
**Voor wie besta je?**  
Wie zijn je klanten en **waarom zouden zij kopen/gebruiken**? Je moet precies weten **wie ze zijn**, want zonder klant besta je niet als organisatie.

### Customer archetype / persona opbouwen:
- **Geografisch**
- **Sociaal**
- **Demografisch**

**Voorbeeldsegment uit de les:**  
- *Ouderen van 60–80 jaar met een kleiner sociaal netwerk, die graag fitter willen worden maar een drempel ervaren om te beginnen.*

Er zijn mogelijk **veel meer segmenten**—die moeten allemaal zichtbaar worden in je Canvas.

## 3. Channels (Stap 3)  
**Hoe bereikt jouw value proposition de klant?**  
Kan zowel **fysiek** als **digitaal**.

**Voorbeelden:**  
- Doorverwijzingen via fysiotherapeuten  
- Zo dicht mogelijk aansluiten bij waar de persoon al komt

## 4. Customer Relationships (Stap 4)  
**Hoe krijg, behoud en laat je klanten groeien?**

- **Get → Keep → Grow → (terug naar Get)**  
Het is een continu proces.

**Voorbeeld:**  
- *Klanten vasthouden door gezelligheid en sociale verbinding.*

## 5. Revenue Streams (Stap 5)  
**Welke waarde levert de klant geld op?**  
Let op:  
- **Verdienmodellen** (direct sales, freemium, licenties, subscriptions) zijn iets anders dan **pricing tactics**.  
- Opbrengsten kunnen **financieel** en/of **sociaal** zijn (bijv. awareness creëren over cyberveiligheid).

(*Vraag uit de les: “Dit staat in de course? Waar staat de course dan?”*)

## 6. Key Resources (Stap 6)  
**Welke middelen zijn essentieel om het bedrijf te laten werken?**  
Dit kunnen zijn:  
- Financiële middelen (geld, leningen)  
- Fysieke middelen (machines, voertuigen, ruimtes)  
- Intellectuele middelen (patenten, know-how)  
- Human resources (mensen met expertise)

**Voorbeelden uit de les:**  
- Social coach  
- Fysieke ruimte  
- Muziek

## 7. Key Partners (Stap 7)  
**Met wie werk je samen en waarom?**  
Partners leveren waarde, middelen of activiteiten die jij zelf niet doet.

### Vragen:  
- Wat leveren ze aan jou?  
- Welke activiteiten verrichten zij voor jou?  
- Wanneer en waarom?

**Voorbeelden:**  
- Huisartsenpraktijken  
- Zorginstellingen  
- Zwembaden  
- Mogelijk zorgverzekeringen (afhankelijk van je customer segment)

> Opmerking uit de les: Namen horen **niet** bij Customer Segments maar bij Partners. Partners helpen bij waardecreatie, maar je **stuurt ze geen rekening**.

## 8. Key Activities (Stap 8)  
**Wat moet je vooral goed doen zodat je bedrijf werkt?**  
Wat moet je kunnen? Waar moet je expert in worden?


## 9. Cost Structure (Stap 9)  
**Welke kosten maak je?**  
Bijv.:  
- Vaste kosten  
- Variabele kosten  
- Kosten van partners  
- Kosten van resources en activiteiten


## Opdracht  
Pas dit Business Model Canvas toe op je **eigen project**.  
Maandag wordt samen gekeken naar **extra customer segments** die je nog kunt toevoegen. Je hebt de template ontvangen—ga daarmee aan de slag.


## Praktische tip uit de les  
Werk met **post-its** zodat je makkelijk kunt schuiven en onderdelen kunt hergroeperen.

## Organisatorisch  
- Expert-tafel rond **19:30**.
