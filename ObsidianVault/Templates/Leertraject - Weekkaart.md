<%*
/* ---------------------------
   Dynamische variabelen
----------------------------*/
const today = tp.date.now("YYYY-MM-DD");
const weekNumber = moment().week();
const title = await tp.system.prompt("Hoofdthema voor deze week?");
const doelen = await tp.system.prompt("Wat wil je deze week bereiken? (scheid met komma’s)");
const focus = await tp.system.prompt("Wat krijgt je hoofd­focus deze week?");
const uitdaging = await tp.system.prompt("Wat verwacht je dat lastig wordt?");
const hulp = await tp.system.prompt("Waar wil je ondersteuning of afstemming over?");
const volgende = await tp.system.prompt("Wat lijkt de logische volgende stap na deze week?");

/* ---------------------------
   YAML-header genereren
----------------------------*/
tR += `---\n`;
tR += `week: ${weekNumber}\n`;
tR += `thema: "${title}"\n`;
tR += `doelen: [${doelen.split(",").map(d => `"${d.trim()}"`).join(", ")}]\n`;
tR += `focus: "${focus}"\n`;
tR += `verwachte_uitdaging: "${uitdaging}"\n`;
tR += `ondersteuning_nodig: "${hulp}"\n`;
tR += `volgende_stap: "${volgende}"\n`;
tR += `tags: [leertraject, weekkaart]\n`;
tR += `date: ${today}\n`;
tR += `---\n\n`;

/* ---------------------------
   Inhoud weektemplate
----------------------------*/
tR += `# 🗓️ Week ${weekNumber} – ${title}\n\n`;
tR += `%% ✏️ Vul dit begin van de week in om richting te bepalen.
   Je kunt later in de week reflectie toevoegen onderaan. %%\n\n`;

tR += `## 🎯 Doelen voor deze week\n`;
tR += `- ${doelen.split(",").map(d => d.trim()).join("\n- ")}\n\n`;

tR += `## 🎯 Focus\n`;
tR += `${focus}\n\n`;

tR += `## ⚠️ Verwachte uitdagingen\n`;
tR += `${uitdaging}\n\n`;

tR += `## 🤝 Ondersteuning of afstemming\n`;
tR += `${hulp}\n\n`;

tR += `## 🔄 Verwachte volgende stap\n`;
tR += `${volgende}\n\n`;

tR += `## 📅 Wat heb ik gedaan (aanvullen door de week)\n`;
tR += `- \n\n`;

tR += `## 💡 Reflectie (einde van de week, optioneel)\n`;
tR += `- Wat werkte goed?\n`;
tR += `- Wat kan beter?\n`;
tR += `- Belangrijkste inzicht:\n\n`;

tR += `## 🔗 Navigatie\n`;
tR += `[[Week ${weekNumber - 1} |← Vorige week]]  \n`;
tR += `[[Week ${weekNumber + 1} |Volgende week →]]\n\n`;

tR += `## 📈 Dataview voorbeeldquery\n`;
tR += `%% Gebruik deze op je dashboard om overzicht te krijgen over doelen en thema's %%\n`;
tR += "```dataview\n";
tR += "TABLE week, thema, focus, doelen, volgende_stap\n";
tR += "FROM \"Leertraject\"\n";
tR += "WHERE contains(tags, \"leertraject\")\n";
tR += "SORT week ASC\n";
tR += "```\n\n";

tR += `[[Canvas/Leertraject-tijdlijn.canvas|📌 Bekijk Canvas-overzicht]]\n`;
tR += `[[Excalidraw/Week ${weekNumber}.excalidraw|✏️ Weektekening]]\n`;
%>