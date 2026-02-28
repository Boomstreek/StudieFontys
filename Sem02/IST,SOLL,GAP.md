## Gemini zei

Het opstellen van een **IST** (de huidige situatie) en een **SOLL** (de gewenste situatie) is essentieel om de kloof tussen nu en de toekomst te overbruggen. Zie het als een routebeschrijving: je kunt pas navigeren als je weet waar je staat en waar je naartoe wilt.

Hieronder staan de kwaliteitseisen voor beide onderdelen.

---

## De IST: De Huidige Situatie

Een goede IST-beschrijving is een eerlijke, feitelijke weergave van de werkelijkheid. Geen mooipraterij, maar de harde realiteit.

- **Feitelijk en Objectief:** Beschrijf wat er _is_, niet wat er zou moeten zijn. Gebruik data, logs en interviews.
    
- **Volledige Architectuur:** Dek alle lagen van de ICT-stack af:
    
    - **Infrastructuur:** Servers, netwerken, cloud-omgevingen.
        
    - **Applicaties:** Welke software draait er en hoe praten ze met elkaar (koppelingen)?
        
    - **Data:** Waar staat de data en wie is de eigenaar?
        
- **Processen en Organisatie:** Hoe wordt de ICT beheerd? Wie doet wat? Denk aan ITIL-processen of de huidige governance.
    
- **Pijnpunten (Bottlenecks):** Benoem expliciet waar het nu schuurt. Hoge kosten, trage systemen, of gebrek aan support?
    
- **Validatie:** Laat de IST controleren door de mensen die er dagelijks mee werken. Zij weten vaak meer dan de documentatie vertelt.
    

---

## De SOLL: De Gewenste Situatie

De SOLL is je stip op de horizon. Deze moet ambitieus zijn, maar wel passen binnen de kaders van de organisatie.

- **Business Alignment:** De techniek moet de bedrijfsdoelen dienen. Als het bedrijf wil groeien, moet de SOLL schaalbaar zijn.
    
- **Functionele Eisen:** Wat moet het systeem straks _kunnen_? Focus op de behoeften van de eindgebruiker.
    
- **Non-Functionele Eisen:** Denk aan de 'harde' kwaliteitseisen zoals:
    
    - **Security:** Voldoet het aan ISO27001 of de AVG?
        
    - **Performance:** Hoe snel moet het reageren?
        
    - **Beschikbaarheid:** Wat is de maximaal toegestane downtime (SLA)?
        
- **Toekomstbestendigheid:** Houd rekening met trends zoals AI, cloud-native werken of hybride werken.
    
- **Realiteitszin:** Een SOLL die technisch perfect is maar onbetaalbaar, is geen goed document. Blijf binnen het budgettaire kader.
    

---

## De Gap-Analyse

Het belangrijkste van deze twee documenten is wat er gebeurt als je ze naast elkaar legt. De **Gap-analyse** bepaalt je projectplan:

|Onderdeel|IST (Nu)|SOLL (Straks)|De 'Gap' (Actie)|
|---|---|---|---|
|**Hosting**|On-premise server|Azure Cloud|Migratie naar cloud|
|**Security**|Wachtwoord|Multi-Factor (MFA)|Implementatie MFA|
|**Data**|Verspreid in Excel|Centraal ERP|Data-opschoning & import|

> **Tip van Gemini:** Wees in de IST vooral niet bang om "schaduw-IT" te benoemen (die ene Excel-sheet waar de hele afdeling op draait). Als je het niet documenteert, kun je het in de SOLL ook niet oplossen!