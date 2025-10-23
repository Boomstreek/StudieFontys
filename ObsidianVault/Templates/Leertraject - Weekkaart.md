<%*
/* ---------------------------
   Dynamische variabelen
----------------------------*/
const today = tp.date.now("YYYY-MM-DD");
const weekNumber = tp.date.now("WW");
const title = await tp.system.prompt("Titel of thema voor deze week?");
const niveau = await tp.system.prompt("Niveau (1–5)?");
const volgende = await tp.system.prompt("Wat wil je volgende week ontdekken?");
tR += `---\n`;
tR += `week: ${weekNumber}\n`;
tR += `thema: ${title}\n`;
tR += `niveau: ${niveau}\n`;
tR += `volgende_stap: "${volgende}"\n`;
tR += `tags: [leertraject, weekkaart]\n`;
tR += `date: ${today}\n`;
tR += `---\n`;
%>

# 🗓️ Week <%= weekNumber %> – <%= title %>

%% ✏️ Vul hieronder je reflectie in. Gebruik dezelfde kopjes elke week
   zodat Dataview en je docenten de voortgang goed kunnen volgen. %%

## 🧭 Waar stond ik aan het begin?
%% Wat wist je al? Waar twijfelde je over? Wat wilde je bereiken? %%

## ⚙️ Wat heb ik gedaan?
%% Beschrijf concreet je activiteiten, observaties of gesprekken. %%

- Voorbeeld: “Meegelopen met Joris bij BGT-dataverwerking.”
- Voorbeeld: “Test uitgevoerd met Greenpoint-koppeling.”

## 💡 Wat heb ik geleerd of ontdekt?
%% Wat werkte goed of minder goed? Welke inzichten of feedback kreeg je? %%

## 🔮 Waar wil ik volgende week naartoe?
%% Gebruik dit om vooruit te kijken. (Wordt ook opgeslagen als YAML-veld.) %%

## 📎 Bewijs & notities
%% Voeg hier links, bestanden of feedback toe als bewijs van leren. %%
- 📷 [[Excalidraw schets van proces]]
- 📄 [Documentatieproject.md](Documentatieproject.md)
- 💬 “Collega gaf aan dat ik duidelijker communiceerde.”

## 🔗 Navigatie
%% Handmatige koppelingen tussen weken (pas bestandsnamen aan) %%
[[Week <%= weekNumber - 1 %> |← Vorige week]]  
[[Week <%= weekNumber + 1 %> |Volgende week →]]


## 📈 Dataview voorbeeldquery (voor je Dashboard)
%% Dit stukje is alleen ter referentie, kopieer dit naar je Dashboard.md %%
```dataview
TABLE week, thema, niveau, volgende_stap
FROM "Leertraject"
WHERE contains(tags, "leertraject")
SORT week ASC\
```

[[Canvas/Leertraject-tijdlijn.canvas|📌 Bekijk Canvas-overzicht]]
[[Excalidraw/Week <%= weekNumber %>.excalidraw|✏️ Weektekening]]
