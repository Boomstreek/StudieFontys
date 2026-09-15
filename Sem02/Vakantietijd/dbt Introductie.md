## Metadata
**Author: ** Bram Wieringa
**Date: ** 22-07-2026
**Version: ** 1.0
**Dependencies: ** -

## Inleiding

## Waarom
Op mijn werk gebruiken we Azure Datafactory en DBT om data op te halen, te verwrken en klaar te zetten voor de bi mannen. Echter vind ik de architectuur niet fijn, dus wil ik me verdiepen in DBT om te kijken of wat we gemaakt ehbben gewoon zo gedaan is omdat het snel werkt of omdat er andere gedachtes liggen. collega die dat heeft gemaatk is met vakantie.

## Introduction to dbt
Wat heb i kgeleerd:?

Spreekt verschillende SQL dialecten

dbt dfine realtiopnship between data models

kan data qualiteit testen

dbt-core is open source, dbt cloud is proprietary

dbt is ontworpen voor mensen die data moeten transformeren,.

### DBT project
- project configutration
- data source en destionations
- sql quiries
- templates
- documentation

_Hoe breed maak je een project?_  _Binnen mijn werkomgeving doen we alles binnen 1 project_ _Gemini stelt dat dit niet handig is en dat je dan beter kan werken met een centraal project (Hub), genierieke dattbronnen, BRP, BAG, centrale koppeltabellen, public modellen en daarnaast domeinproject (de spokes) bijvoorbeeld sociuaal domein of finacnien of vbth importeert publieke modellen uit de hub en bouwen daarop hun eigen rapportage_

_Ik twijfel of dit handig is. ij weren nu met staging, mart en nog een die per dashboard werkt. Echter stelt gemini dat dit niet handig is omdat die git problemen kan geven of meer implementatie problemen_

_Wat ga ik ermee doen. Dit flaggetje staat nu aan, ik ga erover nadenken en het bespreken met colleggas. Denk dat ik het meeneem als een punt in een bredere discussie over proffesionaliseren van onze infratstructuur_

### DBT Profiles
a profile represents a given deployment scenario
- development
- staging / test
- production

je kna meerdere profiles hebben, stan in profiles.yml

- Vectorisatie voor een database betekent het optimaliseren van de data die wordt aangeleverd aan de CPU, zodat deze meer data tegelijk kan verwerken. Wordt daardoor sneller

