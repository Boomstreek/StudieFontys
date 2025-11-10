```mermaid
stateDiagram-v2
    start --> handshake : verbinding maken

    %% Eerste if-statement
    state if_state1 <<choice>>
    handshake --> if_state1
    if_state1 --> wachten : if incomingByte == 0b00100100
    if_state1 --> handshake : else

    %% Tweede if-statement
    state if_state2 <<choice>>
    wachten --> if_state2
    if_state2 --> metenSturen : if incomingByte == 0b10100101
    if_state2 --> eind : if incomingByte == 0b00000000
    if_state2 --> wachten : else

    %% Meetfase met terugk[[2025-W44]][[Powerlifting PC Flow chart]]eerlogica
    metenSturen --> metenSturen : sensoren bewegen / meetgegevens doorsturen
    metenSturen --> wachten : sensoren ongeveer terug bij beginpositie én enige tijd stil

```
%%
# Wat heb ik ervan geleerd
Vergeleken met mijn eerdere state-diagrammen heb ik niet veel nieuws geleerd, behalve dat dit diagram is gemaakt met Mermaid. Daarnaast zijn er ruitjes toegevoegd op de plekken waar keuzes worden gemaakt. Ik weet nog niet zeker of dit correct is binnen de notatie, dit zal ik aan mijn docent vragen om te bevestigen.

%%