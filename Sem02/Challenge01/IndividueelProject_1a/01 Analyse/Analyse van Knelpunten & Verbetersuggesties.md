## Metadata
**Author: ** Bram Wieringa
**Date: ** 26-02-2026
**Version: ** 2.0
**Dependencies: ** OR Planning 003

## Knelpunten & Verbetersuggesties

- **Handmatige data opzoeken**
    - _Knelpunt:_ Een aantal controletaken in HIX en MEDSPACE zijn nu handmatig (User Tasks).
    - _Verbetering:_ Automatiseer dit via Service Tasks (API-koppelingen) voor directe data-uitwisseling, wat de kans op menselijke fouten verkleint.
        
- **Patient mag oneindig weigeren**
    - _Knelpunt:_ Er zit geen limiet op de herhaal-loop als een patiënt een datum weigert.
    - _Verbetering:_ Voeg een regel toe die na twee mislukte pogingen het proces escaleert naar een supervisor om een "deadlock" te voorkomen.
        
- **Late beddencontrole**
    - _Knelpunt:_ De bedden-check vindt pas 2 dagen voor de OK plaats, waardoor bij een tekort de OK-tijd vaak verloren gaat.
    - _Verbetering:_ Gebruik een Parallel Gateway om de bedden-allocatie direct na de screening te starten, zodat er meer tijd is voor alternatieve oplossingen.
        
- **Communicatie via mensen**
    - _Knelpunt:_ Het proces is extreem afhankelijk van telefonisch contact, wat arbeidsintensief en foutgevoelig is (voicemail-loops).
    - _Verbetering:_ Implementeer een geautomatiseerde notificatie-service (SMS, E-mail, Patiëntportaal) om de status direct door de patiënt te laten bevestigen.
        
