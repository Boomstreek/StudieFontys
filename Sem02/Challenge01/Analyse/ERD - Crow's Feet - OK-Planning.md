```mermaid
---
title: OK-Planning - ERD Crow's Feet Notatie
---
erDiagram
    PATIENT ||--o{ OPNAMEN : "is opgenomen"
    OPNAMEN }|--|| KAMER : "ligt op"
    KAMER }|--|| AFDELING : "hoort bij"
    
    PATIENT |o--o{ OPERATIE : ondergaat
    MEDEWERKER }|--|| KOPPEL_UITVOERING : "voert uit"
    OPERATIE }|--|| KOPPEL_UITVOERING : "wordt geholpen door"
    KOPPEL_UITVOERING ||--|| OKROOSTER : "heeft OK-slot"
    
    PATIENT |o--o{ TEVREDENHEID : "is tevreden"
    MEDEWERKER ||--o{ TEVREDENHEID : "heeft werkgeluk"
    
    MEDEWERKER ||--|{ ROOSTER : "heeft werkrooster"
    
    OPERATIE }|--|| OPERATIE_KAMER : "vindt plaats in"
    OPERATIE_KAMER ||--|{ OKROOSTER : "heeft beschikbaarheid"
    
    PATIENT {
    int patientId PK
    string naam
    string adres
    int telefoonnummer
    string email
    boolean toestemmingDigitaalPatientDossier
    }
    
    OPNAMEN {
    int opnamenId PK
    date startDatum
    date eindDatum
    }
    
    KAMER {
    int kamerId PK
    int aantalBedden
    decimal kamerNummer
    }
    
    AFDELING {
    int afdelingId PK
    string afdelingsnaam
    int aantalKamers
    }
    
    MEDEWERKER {
    int medewerkerId PK
    int roosterId FK
    string functie
    }
    
    ROOSTER {
    int roosterId PK
    int medewerkerId FK
    date datum
    time startTijd
    time eindTijd
    }
    
    TEVREDENHEID{
    int tevredenheidId PK
    int medewerkerId FK
    int patientId FK
    date datum
    string opmerking
    int tevredenheidsScore
    }
    
    OPERATIE {
    int operatieId PK
    int patientId FK
    int okRoosterId FK
    datetime geplandeStartTijd
    datetime geplandeEindTijd
    datetime werkelijkeStartTijd
    datetime werkelijkeEindTijd
    string typeOperatie
    string status
    date deadline
    boolean statusScreening
    date annuleringsDatum
    string annuleringsReden
    int aantalHerplanningen
    }
    
    OKROOSTER {
    int okRoosterId PK
    int operatieKamerId FK
    date datum
    time startTijd
    time eindTijd
    }
    
    OPERATIE_KAMER {
    int operatieKamerId PK
    string naam
    }
    
    KOPPEL_UITVOERING {
    int operatieId FK
    int medewerkerId FK
    decimal gespreksduurTotaal
    int aantalTelefonischeDatumVoorstellen
    int retourStroom48u
    decimal aantalMinutenBezigMetPlanning
    int aantalBelpogingen
    string opmerking
    }
    
    %% Eén-op-één relaties
    %% A ||--|| B : "Precies 1 op Precies 1"
    %% A ||--o| C : "Precies 1 op 0 of 1"
    %% Eén-op-veel relaties
    %% D ||--|{ E : "Precies 1 op 1 of meer"
    %% F ||--o{ G : "Precies 1 op 0 of meer"
    %% Veel-op-veel (of optionele) relaties
    %% H }|--|{ I : "1 of meer op 1 of meer"
    %% J }o--o{ K : "0 of meer op 0 of meer"
    %% L }o--o| M : "0 of meer op 0 of 1"
```