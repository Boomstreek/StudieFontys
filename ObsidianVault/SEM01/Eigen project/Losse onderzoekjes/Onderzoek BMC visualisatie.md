# Inleiding
Tijdens de les is er uitleg gegeven over het Business Model Canvas (BMC) en hoe dit kan worden opgesteld. Voor het project wil ik dit concept ook uitwerken. Omdat het meenemen van een fysiek bord lastig is, wil ik het BMC digitaal visualiseren met behulp van syntax.  

## Mogelijkheden

### Mermaid

#### Flowchart
Onderstaande flowchart is een eerste poging, maar de visualisatie voldoet niet helemaal.  


```mermaid
flowchart TD
    A[Customer Segments] -->|Use| B[Value Proposition]
    B --> C[Channels]
    B --> D[Customer Relationships]
    C --> E[Revenue Streams]
    F[Key Resources] --> B
    G[Key Activities] --> B
    H[Key Partners] --> B
    I[Cost Structure] --> B
```

#### Graphvorm
Een andere poging met een graphvorm, maar deze voldoet eveneens niet.

```mermaid
graph TD
  subgraph Left [Customer Side]
    CS[Customer Segments]
    CR[Customer Relationships]
    CH[Channels]
  end

  subgraph Center [Value Proposition]
    VP[Value Proposition]
  end

  subgraph Right [Revenue & Costs]
    RS[Revenue Streams]
    CSt[Cost Structure]
  end

  subgraph Bottom [Resources & Partners]
    KR[Key Resources]
    KA[Key Activities]
    KP[Key Partners]
  end
```

### PlantUML
#### Grid-achtige opzet
Een eerste PlantUML-versie in grid-vorm, maar nog niet optimaal.

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor #f9f9f9
  BorderColor black
  RoundCorner 10
}

rectangle "Customer Segments" as CS #lightblue
rectangle "Value Proposition" as VP #yellow
rectangle "Channels" as CH #lightgreen
rectangle "Customer Relationships" as CR #lightpink
rectangle "Revenue Streams" as RS #orange
rectangle "Key Resources" as KR #lightgrey
rectangle "Key Activities" as KA #beige
rectangle "Key Partners" as KP #lavender
rectangle "Cost Structure" as CSt #salmon

CS -[hidden]-> VP
VP -[hidden]-> CH
CH -[hidden]-> CR
CR -[hidden]-> RS
KR -[hidden]-> KA
KA -[hidden]-> KP
KP -[hidden]-> CSt

' Arrange like a board
CS -[hidden]-> KR
VP -[hidden]-> KA
CH -[hidden]-> KP
CR -[hidden]-> CSt

@enduml
```

#### Verbeterde grid-opzet
Een tweede poging met een nettere grid-opzet, inclusief beschrijvingen.

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor White
  BorderColor Black
  RoundCorner 5
  Shadowing false
  FontSize 12
  FontName Arial
}

' ==== Top row ====
rectangle "Customer Segments\n\n(Who are your customers?)" as CS #lightblue
rectangle "Value Proposition\n\n(What value do you offer?)" as VP #yellow
rectangle "Channels\n\n(How do you reach them?)" as CH #lightgreen
rectangle "Customer Relationships\n\n(How do you interact?)" as CR #lightpink
rectangle "Revenue Streams\n\n(How do you earn?)" as RS #orange

' ==== Bottom row ====
rectangle "Key Resources\n\n(What assets do you need?)" as KR #lightgrey
rectangle "Key Activities\n\n(What do you do?)" as KA #beige
rectangle "Key Partners\n\n(Who helps you?)" as KP #lavender
rectangle "Cost Structure\n\n(What costs exist?)" as CSt #salmon

' ==== Arrange as board ====
CS -[hidden]-> VP
VP -[hidden]-> CH
CH -[hidden]-> CR
CR -[hidden]-> RS

KR -[hidden]-> KA
KA -[hidden]-> KP
KP -[hidden]-> CSt

' Align rows
CS -[hidden]-> KR
VP -[hidden]-> KA
CH -[hidden]-> KP
CR -[hidden]-> CSt
RS -[hidden]-> CSt

@enduml

```

### Experimenten met layout
Een poging om front-stage en back-stage componenten duidelijk te maken.

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor White
  BorderColor Black
  RoundCorner 4
  FontName Arial
  FontSize 12
}

' Front-stage sectie (klantgerichte onderdelen)
rectangle "Customer Segments\n\n(Who are your customers?)" as CS #ADD8E6
rectangle "Value Proposition\n\n(What value do you offer?)" as VP #FFFF99
rectangle "Channels\n\n(How do you reach them?)" as CH #90EE90
rectangle "Customer Relationships\n\n(How do you interact?)" as CR #FFB6C1
rectangle "Revenue Streams\n\n(How do you earn?)" as RS #FFD27F

' Back-stage sectie (infrastructuur)
rectangle "Key Resources\n\n(What assets do you need?)" as KR #D3D3D3
rectangle "Key Activities\n\n(What do you do?)" as KA #F5F5DC
rectangle "Key Partners\n\n(Who helps you?)" as KP #E6E6FA
rectangle "Cost Structure\n\n(What costs exist?)" as CSt #FFA07A

' Layout in 3x3 grid
CS -[hidden]-> VP
VP -[hidden]-> CH

KR -[hidden]-> KA
KA -[hidden]-> KP

CR -[hidden]-> RS
CSt -[hidden]-> RS

' Align front en back
CS -[hidden]-> KR
VP -[hidden]-> KA
CH -[hidden]-> KP
CR -[hidden]-> CSt

@enduml
```

```mermaid
graph TB
  subgraph Front‑stage
    CS["Customer Segments"]
    VP["Value Proposition"]
    CH["Channels"]
    CR["Customer Relationships"]
    RS["Revenue Streams"]
  end

  subgraph Back‑stage
    KR["Key Resources"]
    KA["Key Activities"]
    KP["Key Partners"]
    CSt["Cost Structure"]
  end

  CS --> VP
  VP --> CH
  CR --> RS
  KR --> KA
  KA --> KP
  CSt --> KP

  CS --> KR
  VP --> KA
  CH --> KP
  CR --> CSt
```

## Conclusie
Het blijkt lastig om een BMC via syntax visueel aantrekkelijk weer te geven. Hoewel er diverse opties zijn met Mermaid en PlantUML, blijft het moeilijk om een overzichtelijke en intuïtieve weergave te realiseren. Voor het doel van het project lijkt het werken met post-its op een fysiek bord nog steeds de meest praktische en overzichtelijke methode.

## Bronvermelding
Alle codevoorbeelden in dit document zijn gegenereerd door ChatGPT.