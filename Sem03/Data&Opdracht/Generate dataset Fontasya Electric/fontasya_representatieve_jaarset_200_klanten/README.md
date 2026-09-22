# Fontasya Electric — representatieve jaarset

## Inhoud
- 200 synthetische huishoudens.
- Kalenderjaar 2026 met dagelijkse facttabellen, per maand gepartitioneerd.
- 86 PV-klanten (43.0%); dit valt binnen de vereiste bandbreedte van 35% tot 55%.
- Eigen elektriciteitsproductie is jaarlijks gekalibreerd op 60% van de vraag.
- Eigen productie bestaat uit 65% wind en 35% zon.
- Gas wordt volledig ingekocht.

## Grote maandpartities
- `electricity_consumption_daily/`: 200 klant-dagrecords per dag.
- `gas_consumption_daily/`: 200 klant-dagrecords per dag.
- `pv_feedin_daily/`: alleen PV-klanten, met productie, zelfverbruik en teruglevering.

De grote tabellen zijn gecomprimeerde CSV-bestanden. Voor productiegebruik is Parquet aanbevolen, maar CSV.GZ werkt zonder extra Python-dependencies.

## Sleutels
- `customer_id` koppelt klanten, contracten, PV-assets, elektriciteitsverbruik, gasverbruik en PV-teruglevering.
- `installation_id` koppelt productielocaties en productiedata.
- `date` koppelt alle dagreeksen.
- EAN-codes en coördinaten zijn synthetisch en consistent binnen gekoppelde entiteiten.

## Privacy
De dataset is volledig synthetisch. In een werkelijke omgeving moeten PII, meterdata en pricingdata via toegangscontrole, pseudonimisering, logging en dataminimalisatie worden gescheiden.
