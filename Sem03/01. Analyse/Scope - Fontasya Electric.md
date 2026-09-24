|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |1.5|
|Datum huidige versie|24-9-2026|
|Referenties|Studieplan semester 3 - Data Consultancy Fontasya Electric, 2.0 <br>concept-leverovereenkomst met Fontasya Electric, 1.0|

### Must have

- Data-inventarisatie en bronregister van de aangeleverde (synthetische) datasets: databronnen, datastromen, datakwaliteit, eigenaarschap
- Eerste werkende versie van het prijsadviesproces voor de vier contractvormen (1-jarig, 3-jarig, 5-jarig, flexibel)
- Reproduceerbaarheid en uitlegbaarheid van het prijsmodel: versiebeheer, herleidbare invoer, gedocumenteerde aannames; per prijsrun worden bronversies, datum, scenario en uitkomst vastgelegd
- Minimaal één werkend dashboard: het prijsbeslisdashboard (prijsadvies, kostprijs, marge, scenario's) - direct nodig om het prijsmodel bruikbaar en valideerbaar te maken. In de eerste versie zijn er twee dashboards gepland: waardecreatie, en inkoop/verkoop. Eén dashboard is voldoende, twee heeft de voorkeur.
- Modeldocumentatie: aannames, versies, beperkingen, validatiemethode
- Backend met voldoende beschikbaarheid en beheerbaarheid (geen streven naar een specifiek uptimepercentage), die na oplevering wordt overgedragen aan medewerkers van Fontasya Electric. Beheerbaarheid weegt zwaarder dan kosten; over de kosten kan nog gesproken worden.
- Basis signalering van datakwaliteitsproblemen richting opdrachtgever: bij een fout in de data (bijv. een prijzenfout) stopt het proces en toont het dashboard een duidelijke foutmelding
- Concept AI Chatbot voor klantvragen op basis van dataset die opdrachtgever aanlevert.

### Should have

- Overige dashboards: inkoop-/productiedashboard, portfoliodashboard, terugleverdashboard
- Data kwaliteit- en securitydashboard
- Pilotfase met gebruikers en verwerkte feedback (PoC valideren)
- Documentatie en kennisoverdracht: datastroomoverzicht en technische architectuurbeschrijving, gericht op beheerbaarheid en geschikt voor een lager kennisniveau
- Databeveiliging en privacy: toegangsrechten, voorkomen van datalekken, anonimiteit van data
- Backup van alles, zodat er niets verloren gaat bij incidenten zoals hacks of brand
- Netwerk- en toegangsplan met alle gekoppelde systemen, protocollen en serviceaccounts
- Advies over welke mensen in dienst moeten zijn om na oplevering met het project door te kunnen gaan
- Stakeholderanalyse
- Volledige signalering van datakwaliteitsproblemen, modelbeperkingen en onzekerheden richting opdrachtgever, verder uitgewerkt dan de basis versie bij Must have

### Could have

- Voorspellende/statistische componenten in het prijsmodel (bijv. prognose van toekomstige kosten) in plaats van een puur rekenkundig model
- Scenario-analyses en gevoeligheidsanalyses op het prijsmodel
- Uitbreiding van de dataset/scope zoals door Richard geopperd: nieuwe grote afnemers (tuinbouw) of leveranciers (stadsverwarming)
- Geautomatiseerde orchestration/scheduling van de dataketen
- Gebruik van machine learning of AI in het prijsmodel, mét bijbehorende documentatie van doel, data, prestaties en beperkingen
- Aanvullende databronnen, licenties, cloudvoorzieningen of externe voorspeldiensten buiten de overeengekomen scope, na schriftelijke goedkeuring
- Embedded device die ergens mee kan helpen om iets te ondersteunen
- Gebruikershandleiding
- Simulator voor data
- Productie klare AI Chatbot voor klantvragen op basis van dataset die opdrachtgever aanlevert.

### Won't have

- Volledige juridische/formele afhandeling van de overeenkomst zelf: verwerkersovereenkomst-ondertekening, aansprakelijkheidslimieten, auditrechten, subverwerkersbeheer
- Productie-grade beveiliging (bijv. formele pentest, SIEM-integratie), de beveiligingsprincipes neem ik wel mee in Design, maar niet als volwaardige implementatie
- Geautomatiseerde publicatie van prijsadviezen zonder menselijke controle
- Jaarlijkse audit-ondersteuning: certificeringen, assurance-rapportages, penetratietestsamenvattingen