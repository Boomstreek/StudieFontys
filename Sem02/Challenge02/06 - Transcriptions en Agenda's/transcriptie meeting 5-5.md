Gemaakt door: Robert

### 📋 Samenvatting Meeting 5 mei 2026

**Aanwezig:** Bram (PO/stuurgroep), Robert, Jurgen, Irsad, Tutai (vanuit de trein)

---

### Wat hebben we besproken?

**Stuurgroep & projectscope**De projectscope is na overleg met Carlo voor 99,9% akkoord. Na het eerste inlevermoment roteert de stuurgroep zodat anderen de PO-rol kunnen oppakken. Bram gaf aan graag iets eerder over te dragen vanwege persoonlijke omstandigheden.

**Software-team (Irsad & Jurgen)**Irsad heeft gewerkt aan een analysedocument met als basis een gelaagde architectuur (API-laag, service-laag, datalayer). De backend wordt hoogstwaarschijnlijk ASP.NET Core Web API, maar dit wordt nog afgestemd met Nick. Voor de database zijn SQLite, MySQL Workbench en PostgreSQL opties — SQLite lijkt voorlopig het meest praktisch (licht en lokaal). De keuze wordt bepaald na verdere analyse. Nick heeft ook al een technisch plan van aanpak gemaakt dat nog gedeeld moet worden met de hele groep.

**Cloud/AWS (Robert)**De database wordt eerst lokaal opgezet en daarna eventueel naar AWS gemigreerd. Robert gaat uitzoeken hoe hij de database kan importeren in AWS. De AI-integratie loopt via API-endpoints (bijv. `POST /api/chat/start` en `POST /api/chat/message`). Voor de frontend scrapet Robert de homepage van de gemeentewebsite en plaatst de chatbot-UI als avatar/mascot rechtsonder.

**BI/Dashboard (Bram)**Bram is bezig met de happy flow-analyse voor de chatbot om te meten hoe succesvol deze is (aantal gebruikers, vragen, etc.). Hij bouwt een PowerBI-dashboard en wil dat de "gewone" database los draait van de AI-database.

**MVP login**Er werd gesproken over 3 mock-gebruikers met unieke identifiers, zodat elke gebruiker zijn eigen chatgeschiedenis ziet vanuit de database.

**Personas**Er moeten 2 persona's gemaakt worden: één eindgebruiker (inwoner) en één professional/medewerker. Bram was hier al mee bezig en misschien dat Robert kan helpen.

---

### ✅ Actielijst

|Actie|Wie|
|---|---|
|Beslissen wie de volgende PO wordt|Iedereen (volgende meeting)|
|Analysedocument afmaken en delen met Jurgen|Irsad|
|Tech stack afstemmen met Nick (database, backend, FastAPI vs .NET)|Irsad + Jurgen|
|Nick's technisch plan van aanpak delen met de hele groep|Jurgen (of Nick vragen)|
|Analysedocument aanpassen op basis van Nick's document voor donderdag|Irsad|
|Database-import uitzoeken voor AWS|Robert|
|Personas uitwerken (1 eindgebruiker + 1 professional)|Bram (en Robert)|
|Happy flow uitwerken + PowerBI dashboard opzetten|Bram|
|Wireframes chatbot-UI maken|Sahel + Robert afstemmen|

---

### 📅 Volgende afspraken

- **Donderdag:** Eigen standup om **08:00**, daarna meeting met docent Robin om **18:30**
- **Dinsdag volgende week:** Fysiek bij elkaar in **Eindhoven**