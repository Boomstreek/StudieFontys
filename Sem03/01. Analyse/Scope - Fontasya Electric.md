|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |1.4|
|Datum huidige versie|22-9-2026|
|Referenties|Studieplan semester 3 - Data Consultancy Fontasya Electric, 2.0 <br>concept-leverovereenkomst met Fontasya Electric, 1.0|

## Must have

Zonder dit geen geldig prijsadvies en geen bewijs voor mijn hoofdprofiel.

- Data-inventarisatie en bronregister van de aangeleverde (synthetische) datasets: databronnen, datastromen, datakwaliteit, eigenaarschap _(leverovereenkomst §4.1, Fase 2 Datafundament)_
- Eerste werkende versie van het prijsadviesproces voor de vier contractvormen (1-jarig, 3-jarig, 5-jarig, flexibel) _(§4.2, Fase 3 - expliciet acceptatiecriterium: "reproduceerbare berekeningen en modeldocumentatie")_
- Reproduceerbaarheid en uitlegbaarheid van het prijsmodel: versiebeheer, herleidbare invoer, gedocumenteerde aannames; per prijsrun bronversies, datum, scenario en uitkomst vastgelegd _(§9.1–9.2)_
- Minimaal één werkend dashboard: het prijsbeslisdashboard (prijsadvies, kostprijs, marge, scenario's) - direct nodig om het prijsmodel bruikbaar en valideerbaar te maken _(§4.3)_
	- twee dashbaord in eerste versie, waardecreatie, inkoop en verkoop. 1 tevreden 2 liever
- Modeldocumentatie: aannames, versies, beperkingen, validatiemethode _(§4.4)_
- Backend met uptime van 99,5%,
	- niet streven naar percentage, er is beschikbaarheid en beheerbaarheid, daarna overdargen aan mensen die in dienst zijn bij Fotnyasia electric
	- Beheerbaarheid belangrijker, kosten kunnen we over praten
		- Advies welke mensen in dienst moeten zijn om ermee te kunnen doorgaan.. Should have
		- stakeholderanalyse

## Should have

Belangrijk voor een compleet en geloofwaardig eindproduct, maar niet het eerste waar ik op vastloop als de tijd krap wordt.

- Overige dashboards uit §4.3: inkoop-/productiedashboard, portfoliodashboard, terugleverdashboard
- Data kwaliteit- en securitydashboard
- Pilotfase met gebruikers en verwerkte feedback  (PoC valideren)
- Signaleren van datakwaliteitsproblemen, modelbeperkingen en onzekerheden richting opdrachtgever (§5.2, §9.3) 
	- in lichte vorm wel bij must have, als het fout gaat wat dan, luchtig houden (prijzenfout in data, stoppen plus grote error in dashbaord)
- Documentatie en kennisoverdracht: datastroomoverzicht, technische architectuurbeschrijving,  (§4.4)
	- beheerbaarheid
	- niveau lager
- Databeveiliging en privacy
	- rechten
	- data niet lekken
	- anonimiteit
- Backup van alles, niks verliezen bij hacks brand etc
- Netwerk- en toegangsplan met alle gekoppelde systemen, protocollen en serviceaccounts (§7.3)

## Could have

Waardevolle verdieping als er tijd over is; niet nodig om mijn leeruitkomsten aan te tonen.

- Voorspellende/statistische componenten in het prijsmodel (bijv. prognose van toekomstige kosten) in plaats van een puur rekenkundig model
- Scenario-analyses en gevoeligheidsanalyses op het prijsmodel (§4.2, §9.3)
- Uitbreiding van de dataset/scope zoals door Richard geopperd: nieuwe grote afnemers (tuinbouw) of leveranciers (stadsverwarming)
- Geautomatiseerde orchestration/scheduling van de dataketen
- Gebruik van machine learning of AI in het prijsmodel, mét bijbehorende documentatie van doel, data, prestaties en beperkingen (§9.4: alleen van toepassing "indien" dit gebeurt)
- Aanvullende databronnen, licenties, cloudvoorzieningen of externe voorspeldiensten buiten de overeengekomen scope, na schriftelijke goedkeuring (§14.2)
- Embedded device die ergens mee kan helpen om iets te ondersteunen
- gebruikershandleiding
- simulator voor data

## Won't have

Bewust buiten scope, ook als het interessant is.

- Volledige juridische/formele afhandeling van de overeenkomst zelf: verwerkersovereenkomst-ondertekening, aansprakelijkheidslimieten, audit­rechten, subverwerkersbeheer (§6, §11–13) 
- Productie-grade beveiliging (bijv. formele pentest, SIEM-integratie) - de beveiligingsprincipes (§7) neem ik wel mee in Design, maar niet als volwaardige implementatie
- Geautomatiseerde publicatie van prijsadviezen zonder menselijke controle - expliciet uitgesloten in de overeenkomst (§9.5)
- Jaarlijkse audit-ondersteuning: certificeringen, assurance-rapportages, penetratietestsamenvattingen (§13)