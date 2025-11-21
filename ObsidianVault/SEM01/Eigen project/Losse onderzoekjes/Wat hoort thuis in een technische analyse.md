# Prompt:
Horen GitHub, Word en Trello thuis in een technische analyse? 

# Antwoord

Kort antwoord: **Nee, GitHub, Word en Trello horen meestal _niet_ thuis in de technische analyse van een IT-project.**

## Waarom niet?

Een **technische analyse** beschrijft normaal gesproken de technische aspecten die direct bijdragen aan het ontwerp, de werking en de architectuur van de oplossing. Denk hierbij aan:

- de **technische architectuur** (frontend, backend, API’s, databases, hosting, integraties)
- gebruikte **frameworks en libraries**
- **data-stromen**, **interfaces**, **protocollen**
- **security-, performance- en schaalbaarheidsvereisten**
- keuzes in **systemen** die functioneel onderdeel zijn van de software

Het gaat dus om alles wat daadwerkelijk het te bouwen of te implementeren systeem vormt.

## Waarom tools als GitHub, Word en Trello er niet in horen

Platforms zoals **GitHub**, **Microsoft Word** en **Trello** horen hier niet in thuis, omdat:

- ze **geen onderdeel** zijn van de uiteindelijke softwareoplossing
- ze de **architectuur of werking** van het systeem niet beïnvloeden
- ze puur **ondersteunend** zijn voor samenwerking, documentatie of projectmanagement

Deze tools horen eerder thuis in:

- **projectmanagementdocumentatie**, of
- een **kwaliteitsplan**, bijvoorbeeld onder gebruikte hulpmiddelen of werkmethoden

## Wat hoort wél in een technische analyse?

Voorbeelden van zaken die wél thuishoren:

- Programmeertalen (bijv. Python, Java, JavaScript)
- Frameworks (React, Vue, Spring Boot, Django)
- Cloudplatformen (Azure, AWS, GCP, on-premise setups)
- Databases (PostgreSQL, MySQL, MongoDB)
- Deployment-methoden (Docker, Kubernetes, CI/CD pipelines)
- Externe API’s en integraties
- Securitycomponenten (IAM, OAuth2, encryptie)
- Monitoring- en loggingoplossingen

## Wanneer hoort een tool wél in een technische analyse?

Alleen wanneer een tool functioneel onderdeel is van de oplossing of daadwerkelijk technische risico’s of afhankelijkheden introduceert. Bijvoorbeeld:

- **GitHub Actions** als de CI/CD-pipeline onderdeel is van de technische architectuur.
- Een **monitoringtool** (zoals Prometheus) als die geïntegreerd wordt in de oplossing.
- Een **securityscanner** die automatisch deel uitmaakt van de build chain.

In alle andere gevallen hoort het thuis in het projectplan, niet in de technische analyse.

## Bronnen (APA-stijl)
OpenAI. (2025). _Uitleg over technische analyses in IT-projecten_ [Large language model output]. ChatGPT. [https://chat.openai.com/](https://chat.openai.com/)

Chatgpt gaf aan als onderstaande aan als bron, maar daar kan ik niet bij.
Bass, L., Clements, P., & Kazman, R. (2021). _Software architecture in practice_ (4th ed.). Addison-Wesley.