<%*
/* ---------------------------
   Dynamische variabelen
----------------------------*/
const today = tp.date.now("YYYY-MM-DD");
const weekNumber = moment().week();
const title = await tp.system.prompt("Title voor deze week?");
const doelen = await tp.system.prompt("Wat wil je deze week bereiken? (scheid met komma’s)");
const focus = await tp.system.prompt("Wat krijgt je hoofdfocus deze week?");
const uitdaging = await tp.system.prompt("Wat verwacht je dat lastig wordt?");
const hulp = await tp.system.prompt("Waar wil je ondersteuning of afstemming over?");
const volgende = await tp.system.prompt("Zijn er al actiepunten voor volgende week?");

/* ---------------------------
   Valideerbare motivatie / energie / emoties prompts
----------------------------*/
let motivatieInt = 0;

do {
    const input = await tp.system.prompt(
        motivatieInt === 0 
        ? "Schaal van 1 t/m 5, wat is je motivatie op dit moment?" 
        : "Fout! Voer een getal in van 1 t/m 5 voor je motivatie op dit moment:"
    );
    motivatieInt = parseInt(input);
} while (isNaN(motivatieInt) || motivatieInt < 1 || motivatieInt > 5);

const waaromMotivatie = await tp.system.prompt("Waarom heb je gekozen voor dit motivatie cijfer?");

let energieInt = 0;

do {
    const input = await tp.system.prompt(
        energieInt === 0 
        ? "Schaal van 1 t/m 5, wat is je energie op dit moment?" 
        : "Fout! Voer een getal in van 1 t/m 5 voor je energie op dit moment:"
    );
    energieInt = parseInt(input);
} while (isNaN(energieInt) || energieInt < 1 || energieInt > 5);

const waaromEnergie = await tp.system.prompt("Waarom heb je gekozen voor dit energie cijfer?");

let emotie = "";
const emoties = ["blij", "boos", "gefrustreerd", "ontspannen", "gestrest", "verbaasd"];

do {
    const input = await tp.system.prompt(
        emotie === "" 
        ? `Welke emotie voel je op dit moment? Kies uit: ${emoties.join(", ")}`
        : `Fout! Kies één van de volgende emoties: ${emoties.join(", ")}`
    );
    if (emoties.includes(input.toLowerCase().trim())) {
        emotie = input.toLowerCase().trim();
    } else {
        emotie = "";
    }
} while (emotie === "");

const waaromEmotie = await tp.system.prompt("Waarom heb je gekozen voor deze emotie?");

/* ---------------------------
   YAML-header genereren
----------------------------*/
tR += `---\n`;
tR += `week: ${weekNumber}\n`;
tR += `thema: "${title}"\n`;
tR += `motivatie: ${motivatieInt}\n`;
tR += `waarom dit motivatiecijfer?: ${waaromMotivatie}\n`;
tR += `energie: ${energieInt}\n`;
tR += `waarom dit energiecijfer?: ${waaromEnergie}\n`;
tR += `emotie: ${emotie}\n`;
tR += `waarom deze emotie?: ${waaromEmotie}\n`;
tR += `doelen: [${doelen.split(",").map(d => `"${d.trim()}"`).join(", ")}]\n`;
tR += `focus: "${focus}"\n`;
tR += `verwachte_uitdagingen: "${uitdaging}"\n`;
tR += `ondersteuning_nodig: "${hulp}"\n`;
tR += `volgende_stap: "${volgende}"\n`;
tR += `tags: [leertraject, weekkaart]\n`;
tR += `date: ${today}\n`;
tR += `---\n\n`;

/* ---------------------------
   Inhoud weektemplate
----------------------------*/
tR += `# Week ${weekNumber} – ${title}\n\n`;
tR += `%% Vul dit begin van de week in om richting te bepalen.
   Voeg aan het eind van de week reflectie toe onderaan. %%\n\n`;

tR += `## Doelen voor deze week\n`;
tR += `${doelen.split(",").map(d => `- [ ] ${d.trim()}`).join("\n")}\n\n`;

tR += `## Focus\n`;
tR += `${focus}\n\n`;

tR += `## Verwachte uitdagingen\n`;
tR += `${uitdaging}\n\n`;

tR += `## Ondersteuning of afstemming\n`;
tR += `${hulp}\n\n`;

tR += `## Actiepunten volgende week\n`;
tR += `${volgende}\n\n`;

tR += `## Wat heb ik gedaan\n`;
tR += `%%- (Welke projecten of taken heb ik uitgevoerd?) %%\n`;
tR += `%%- (Wat waren concrete resultaten of stappen?) %%\n`;
tR += `%%- (Waar heb ik de meeste tijd aan besteed — was dat effectief?) %%\n\n`;

tR += `## Wat heb ik geleerd\n`;
tR += `%%- (Welke kennis of vaardigheid heb ik ontwikkeld?) %%\n`;
tR += `%%- (Wat heb ik geleerd over samenwerking of proces?) %%\n`;
tR += `%%- (Wat zou ik verder willen ontwikkelen?) %%\n\n`;

tR += `## Reflectie (einde van de week)\n`;
tR += `### Wat werkte goed?\n`;
tR += `- \n\n`;
tR += `### Wat kan beter?\n`;
tR += `- \n\n`;
tR += `### Wat was impact vol of opvallend?\n`;
tR += `- \n\n`;
tR += `### Hoe voelde de week?\n`;
tR += `%%- (druk, leerzaam, bevredigend, frustrerend, etc.) %%\n\n`;
tR += `%% {Motivatie / Energie} %%\n\n`;
tR += `### Belangrijkste inzicht\n`;
tR += `%% Beschrijf je belangrijkste Aha moment en waarom dit je een belangrijke Aha moment was. %%\n\n`;
tR += `- \n\n`;

tR += `## Inzichten of ideeën\n`;
tR += `%%- (Nieuwe ideeën, observaties, verbeterpunten voor volgende week) %%\n\n`;

tR += `## Vragen voor docenten\n`;
tR += `%%- (Welke vragen heb ik voor de algemene les?) %%\n\n`;

tR += `## Feedback ontvangen\n`;
tR += `%% {Naam / opmerking} %%\n\n`;

tR += `## Dataview overzicht\n`;
tR += `%% Gebruik deze query op je dashboard om overzicht te krijgen over doelen en thema's %%\n`;
tR += "```dataview\n";
tR += "TABLE week, thema, focus, doelen, volgende_stap\n";
tR += "FROM \"Leertraject\"\n";
tR += "WHERE contains(tags, \"leertraject\")\n";
tR += "SORT week DESC\n";
tR += "```\n\n";

tR += `[[Canvas/Leertraject-tijdlijn.canvas|📌 Bekijk Canvas-overzicht]]\n`;
tR += `[[Excalidraw/Week ${weekNumber}.excalidraw|✏️ Weektekening]]\n`;
%>
