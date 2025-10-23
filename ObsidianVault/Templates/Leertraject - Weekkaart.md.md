<%*
/* ---------------------------
   Dynamische variabelen
----------------------------*/
const today = tp.date.now("YYYY-MM-DD");
const weekNumber = moment().week();
const title = await tp.system.prompt("Titel of thema voor deze week?");
const niveau = await tp.system.prompt("Niveau (1–5)?");
const volgende = await tp.system.prompt("Wat wil je volgende week ontdekken?");

/* ---------------------------
   YAML-header genereren
----------------------------*/
tR += `---\n`;
tR += `week: ${weekNumber}\n`;
tR += `thema: ${title}\n`;
tR += `niveau: ${niveau}\n`;
tR += `volgende_stap: "${volgende}"\n`;
tR += `tags: [leertraject, weekkaart]\n`;
tR += `date: ${today}\n`;
tR += `---\n\n`;

/* ---------------------------
   Inhoud van weektemplate
----------------------------*/
tR += `# 🗓️ Week ${weekNumber} – ${title}\n\n`;
tR += `%% ✏️ Vul hieronder je reflectie in. Gebruik dezelfde kopjes elke week
   zodat Dataview en je docenten de voortgang goed kunnen volgen. %%\n\n`;

tR += `## 🧭 Waar stond ik aan het begin?\n`;
tR += `%% Wat wist je al? Waar twijfelde je over? Wat wilde je bereiken? %%\n\n`;

tR += `## ⚙️ Wat heb ik gedaan?\n`;
tR += `%% Beschrijf concreet je activiteiten, observaties of gesprekken. %%\n\n`;
tR += `- Voorbeeld: “Meegelopen met Joris bij BGT-dataverwerking.”\n`;
tR += `- Voorbeeld: “Test uitgevoerd met Greenpoint-koppeling.”\n\n`;

tR += `## 💡 Wat heb ik geleerd of ontdekt?\n`;
tR += `%% Wat werkte goed of minder goed? Welke inzichten of feedback kreeg je? %%\n\n`;

tR += `## 🔮 Waar wil ik volgende week naartoe?\n`;
tR += `%% Gebruik dit om vooruit te kijken. (Wordt ook opgeslagen als YAML-veld.) %%\n\n`;

tR += `## 📎 Bewijs & notities\n`;
tR += `%% Voeg hier links, bestanden of feedback toe als bewijs van leren. %%\n`;
tR += `- 📷 [[Excalidraw schets van proces]]\n`;
tR += `- 📄 [Documentatieproject.md](Documentatieproject.md)\n`;
tR += `- 💬 “Collega gaf aan dat ik duidelijker communiceerde.”\n\n`;

tR += `## 🔗 Navigatie\n`;
tR += `[[Week ${weekNumber - 1} |← Vorige week]]  \n`;
tR += `[[Week ${weekNumber + 1} |Volgende week →]]\n\n`;

tR += `## 📈 Dataview voorbeeldquery (voor je Dashboard)\n`;
tR += `%% Dit stukje is alleen ter referentie, kopieer dit naar je Dashboard.md %%\n`;
tR += "```dataview\n";
tR += "TABLE week, thema, niveau, volgende_stap\n";
tR += "FROM \"Leertraject\"\n";
tR += "WHERE contains(tags, \"leertraject\")\n";
tR += "SORT week ASC\n";
tR += "```\n\n";

tR += `[[Canvas/Leertraject-tijdlijn.canvas|📌 Bekijk Canvas-overzicht]]\n`;
tR += `[[Excalidraw/Week ${weekNumber}.excalidraw|✏️ Weektekening]]\n`;
%>
