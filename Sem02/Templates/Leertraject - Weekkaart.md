<%*
/* ---------------------------
   Dynamische variabelen
----------------------------*/
const today = tp.date.now("YYYY-MM-DD");
const nextWeek = moment().add(1, 'weeks');
const nextMonday = nextWeek.startOf('isoWeek').format("YYYY-MM-DD");
const weekNumber = moment().week();
const nextWeekNumber = nextWeek.week();
const year = nextWeek.year();

/* ---------------------------
   Prompts
----------------------------*/
const title = await tp.system.prompt("Titel voor deze week?");
const doelen = await tp.system.prompt("Wat wil je deze week doen? (scheid met komma’s)(?Vragen?, Actiepunt)");
const focus = await tp.system.prompt("Wat krijgt je hoofdfocus deze week?");
const uitdaging = await tp.system.prompt("Wat verwacht je dat lastig wordt?");

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

const waaromMotivatie = await tp.system.prompt("Waarom heb je gekozen voor dit motivatiecijfer?");

let energieInt = 0;

do {
    const input = await tp.system.prompt(
        energieInt === 0 
        ? "Schaal van 1 t/m 5, wat is je energie op dit moment?" 
        : "Fout! Voer een getal in van 1 t/m 5 voor je energie op dit moment:"
    );
    energieInt = parseInt(input);
} while (isNaN(energieInt) || energieInt < 1 || energieInt > 5);

const waaromEnergie = await tp.system.prompt("Waarom heb je gekozen voor dit energiecijfer?");

let emotie = "";
const emoties = [
  "blij",
  "trots",
  "nieuwsgierig",
  "ontspannen",
  "kalm",
  "verbaasd",
  "boos",
  "gefrustreerd",
  "gestrest",
  "verdrietig",
  "teleurgesteld",
  "ongerust"
];

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
   Automatische bestandsnaam
----------------------------*/
await tp.file.rename(`${year}-W${nextWeekNumber}`);

/* ---------------------------
   YAML-header genereren
----------------------------*/
const doelenArray = doelen.split(",").map(d => d.trim()).filter(d => d.length > 0);

tR += `---\n`;
tR += `week: ${nextWeekNumber}\n`;
tR += `thema: "${title}"\n`;
tR += `motivatie: ${motivatieInt}\n`;
tR += `waarom dit motivatiecijfer?: "${waaromMotivatie}"\n`;
tR += `energie: ${energieInt}\n`;
tR += `waarom dit energiecijfer?: "${waaromEnergie}"\n`;
tR += `emotie: "${emotie}"\n`;
tR += `waarom deze emotie?: "${waaromEmotie}"\n`;
tR += `Actiepunten: [${doelenArray.map(d => `"${d}"`).join(", ")}]\n`;
tR += `focus: "${focus}"\n`;
tR += `verwachte_uitdagingen: "${uitdaging}"\n`;
tR += `tags: [leertraject, weekkaart]\n`;
tR += `Eerste_maandag_van_de_week: ${nextMonday}\n`;
tR += `Aangemaakt_op: ${today}\n`;
tR += `---\n\n`;

/* ---------------------------
   Inhoud weektemplate
----------------------------*/
tR += `# Week ${nextWeekNumber} – ${title}\n\n`;
tR += `%% Vul dit begin van de week in om richting te bepalen.
   Voeg aan het eind van de week reflectie toe onderaan. %%\n\n`;

tR += `## Actielijst voor deze week\n`;
tR += `${doelenArray.map(d => `- [ ] ${d}`).join("\n")}\n\n`;

tR += `## Focus\n`;
tR += `${focus}\n\n`;

tR += `## Verwachte uitdagingen\n`;
tR += `${uitdaging}\n\n`;

tR += `## Reflectie (einde van de week)\n`;
tR += `### Wat werkte goed?\n`;
tR += `- \n\n`;
tR += `### Wat kan beter?\n`;
tR += `- \n\n`;
tR += `### Wat was impactvol of opvallend?\n`;
tR += `- \n\n`;
tR += `### Hoe voelde de week?\n`;
tR += `%%- (druk, leerzaam, bevredigend, frustrerend, etc.) %%\n\n`;

tR += `### Belangrijkste inzicht\n`;
tR += `%% Beschrijf je belangrijkste Aha-moment en waarom dit belangrijk was. %%\n\n`;
tR += `- \n\n`;

tR += `## Inzichten, ideeën en geleerde lessen\n`;

tR += `## Feedback ontvangen\n`;

tR += `## Dataview overzicht\n`;
tR += "```dataview\n";
tR += "TABLE week, thema, focus, emotie, energie, motivatie\n";
tR += "FROM \"Weekkaarten\"\n";
tR += "WHERE contains(tags, \"leertraject\")\n";
tR += "SORT week DESC\n";
tR += "```\n\n";

tR += `Vorige: [[${year}-W${nextWeekNumber - 1}]]\n`;
tR += `Volgende: [[${year}-W${nextWeekNumber + 1}]]\n\n`;
%>