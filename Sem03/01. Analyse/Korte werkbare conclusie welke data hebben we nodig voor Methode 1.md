# Conclusie: welke data hebben we nodig voor het eerste prijsadvies?

We hebben al data van Fontasya Electric, maar geen tijd om die eerst op te schonen. Daarom genereren we voor het ontwerp zelf een dataset. Later vervangen we dit door de echte data.

## Zelf genereren 

- **Inkoopprijs van stroom en gas** per maand, per contractvorm (flexibel, 1, 3, 5 jaar), in €/kWh en €/m³. Hierin zitten de risico-opslagen al verwerkt.
- **Marge van Fontasya**, uitgesplitst in:
    - **Operationele kosten, vast:** € per aansluiting per maand (facturatie, klantenservice, ICT, personeel, marketing).
    - **Operationele kosten, variabel:** € per kWh of m³.
    - **Rendement (winst):** € per kWh of m³.
    - **Debiteurenrisico (wanbetalers):** € per kWh of m³.
- **Jaarverbruik** in kWh en m³ per klantgroep.

## Snel online opzoeken 

- **Netbeheerkosten** per maand: aansluittarief, capaciteitstarief en meettarief (ACM).
- **Energiebelasting** per kWh stroom en per m³ gas (Belastingdienst).
- **Vermindering energiebelasting:** vast bedrag per jaar per aansluiting (Belastingdienst).
- **Btw:** 21%, berekend over alles samen.
- **Inflatie (CPI)** per jaar (CBS).

## Rekenregel

```
tarief per kWh of m³ = (inkoopprijs + operationele kosten + rendement + debiteurenrisico + energiebelasting) × 1,21
```

De vaste kosten (operationele kosten vast en netbeheer) komen per maand bovenop het tarief, minus de vermindering energiebelasting per jaar.

