|Metadata|||
|---|---|
|Naam student|Bram Wieringa|
|Versienummer |1.3|
|Datum huidige versie|21-9-2026|
|Referenties|concept-leverovereenkomst met Fontasya Electric, 1.0|

## Must have

Expliciet vereist als kernresultaat of acceptatiecriterium in het werkplan (Bijlage 3), of als harde verplichting elders in de overeenkomst.

- **Data-inventarisatie en datalandschap** (§4.1): servers, databronnen, bestandsformaten, eigenaars en toegangsrollen identificeren; datastromen, kwaliteit, actualiteit, volledigheid en herleidbaarheid vaststellen; data classificeren naar gevoeligheid en aanwezigheid van persoonsgegevens; voorstel voor doelarchitectuur (catalogus, metadata, toegangsbeheer, logging) en voor veilige ETL-processen
- **Prijsadviesproces voor vier contractvormen** (§4.2): 1-jarig, 3-jarig, 5-jarig en flexibel, met de opgesomde kostprijs-, risico- en marge-elementen voor zover data beschikbaar is
- **Reproduceerbaarheid en uitlegbaarheid van het prijsmodel** (§9.1–9.3): versiebeheer, herleidbare invoer, gedocumenteerde aannames; per prijsadviesrun bronversies, datum, scenario, aannames en uitkomst vastleggen; onzekerheden en beperkingen rapporteren
- **Eerste versie van de dashboards** (§4.3): prijsbeslis-, inkoop/productie-, portfolio-, teruglever- en datakwaliteit/securitydashboard, met filters op periode/contractvorm/energieproduct/regio/scenario; persoonsgegevens geaggregeerd of gepseudonimiseerd waar passend
	- Dit splitsen naar 1 dashboard de prijsbeslishdsashbaod
- **Documentatie en kennisoverdracht** (§4.4): bronregister en datawoordenboek, datastroomoverzicht en technische architectuurbeschrijving, modeldocumentatie (aannames, versies, beperkingen, validatiemethode), gebruikershandleidingen, beheerinstructies, releaseproces, training
- **Privacyrolverdeling en verwerkersovereenkomst** (§6.1, Bijlage 1): Opdrachtgever als verwerkingsverantwoordelijke, Consultant als verwerker; verwerking uitsluitend op gedocumenteerde instructie en beperkt tot het noodzakelijke
- **Minimale beveiligingsmaatregelen** (§7.2): versleuteling, MFA, rolgebaseerde toegang, gescheiden dev/test/acceptatie/productie-omgevingen, gemaskeerde/synthetische testdata, centrale logging, kwetsbaarheidsbeheer, back-ups, beveiligde ontwikkeling, incidentresponsproces
- **Geen geautomatiseerde publicatie van prijsadviezen** zonder menselijke beoordeling, tenzij hierover aanvullende schriftelijke afspraken zijn gemaakt (§9.5)
- **Acceptatieproces per fase** (Bijlage 3): Initiatie -> Datafundament -> Prijsmodel -> Dashboards -> Pilot -> Overdracht, elk met een eigen acceptatiecriterium

## Should have

Wel onderdeel van de overeenkomst, maar voorwaardelijk, nader in te vullen, of niet kritiek voor de eerste oplevering.

- Aanvullende prijscomponenten "voor zover gegevens beschikbaar" (garanties, risico, onbalans, reserveringen) en energiebelasting/netkosten "voor zover Opdrachtgever dit wenst" (§4.2)
- Concrete invulling van de service level agreement: hersteldoelstellingen, back-upbewaartermijn, herstelfrequentie testen, rapportagefrequentie (Bijlage 2: status "in te vullen")
- Netwerk- en toegangsplan met alle gekoppelde systemen, protocollen en serviceaccounts (§7.3)
- Ondersteuning bij rechten van betrokkenen (inzage, correctie, verwijdering) (Bijlage 1, onderdeel D)
- Jaarlijkse audit-ondersteuning: certificeringen, assurance-rapportages, penetratietestsamenvattingen (§13)

## Could have

Alleen relevant als de opdrachtgever dit expliciet wenst of als de situatie erom vraagt; niet standaard onderdeel van de eerste oplevering.

- Uitbreiding van het dashboard-backlog buiten de vijf genoemde dashboards (§4.3: "definitieve set wordt vastgelegd in een afzonderlijk backlog of werkplan")
- Gebruik van machine learning of AI in het prijsmodel, mét bijbehorende documentatie van doel, data, prestaties en beperkingen (§9.4: alleen van toepassing "indien" dit gebeurt)
- Doorgifte van persoonsgegevens buiten de EER, met aanvullende waarborgen en schriftelijke toestemming (§6.4)
- Inzet van subverwerkers, na toestemming en met gelijkwaardige verplichtingen (§6.4)
- Aanvullende databronnen, licenties, cloudvoorzieningen of externe voorspeldiensten buiten de overeengekomen scope, na schriftelijke goedkeuring (§14.2)

## Won't have

Expliciet buiten scope of uitgesloten door de overeenkomst zelf.

- Zelfstandig een commercieel prijsbesluit nemen namens de opdrachtgever, dat blijft altijd bij Fontasya Electric (§2, §9.6)
- Klantdata gebruiken voor eigen doeleinden, profilering, marketing, training van algemene AI-modellen of doeleinden van derden (§5.2)
- Data, modellen of uitkomsten van de opdrachtgever gebruiken als referentie, publicatie of commerciële casus zonder voorafgaande schriftelijke toestemming (§11.4)
- Persoonsgegevens langer bewaren dan noodzakelijk, of niet verwijderen/retourneren na afloop van de overeenkomst (behoudens wettelijke bewaarplicht) (§6.5)