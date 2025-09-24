import pandas as pd
from collections import defaultdict
import circlify
import matplotlib.pyplot as plt
import textwrap

# ============================
# 1. Data inlezen
# ============================
df = pd.read_excel("Applicaties.ods", engine="odf")
print("ODS ingelezen\n")
print(df.head())

# ============================
# 2. Hiërarchie bouwen
# ============================
def tree():
    return defaultdict(tree)

root = tree()

for _, row in df.iterrows():
    node = root
    for col in ["Organisatie", "Afdeling", "Team", "Applicatie"]:
        value = row[col]
        # Dubbele namen vermijden
        if row["Organisatie"] == "RID" and value == "GIS":
            value = "RID GIS"
        elif row["Organisatie"] == "RID" and value == "Kaartviewer":
            value = "Kaartviewer"
        elif row["Organisatie"] == "1Stroom" and value == "GIS":
            value = "Data"  # aanpassen zodat geen duplicate met QGIS/GeoServer
        node = node[value]

# ============================
# 3. Omzetten naar circlify-formaat
# ============================
def dict_to_circlify(d, name="root"):
    children = [dict_to_circlify(v, k) for k, v in d.items()]
    if children:
        return {"id": name, "children": children, "datum": 1}  # interne nodes krijgen datum
    else:
        return {"id": name, "datum": 1}  # leaf nodes

hierarchie = dict_to_circlify(root)

# ============================
# 4. Circlify berekenen
# ============================
circles = circlify.circlify(
    hierarchie["children"],   # root overslaan
    show_enclosure=True
)

# ============================
# 5. Plotten en labels
# ============================
fig, ax = plt.subplots(figsize=(12, 12))
ax.axis('off')

lim = max(
    max(abs(c.x) + c.r, abs(c.y) + c.r)
    for c in circles
)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

for c in circles:
    x, y, r = c.x, c.y, c.r
    ax.add_patch(
        plt.Circle((x, y), r, alpha=0.2,
                   linewidth=2, edgecolor="black",
                   facecolor="skyblue")
    )
    # Alleen labels tekenen als cirkel groot genoeg en ex bestaat
    if c.ex is not None and r > 0.5:
        label = c.ex["id"]
        # wrap lange namen
        label_wrapped = "\n".join(textwrap.wrap(label, width=12))
        fontsize = max(int(r*8), 4)  # lettergrootte dynamisch
        ax.text(x, y, label_wrapped, ha="center", va="center", fontsize=fontsize)

# ============================
# 6. Opslaan naar PNG
# ============================
plt.savefig("nested_circles.png", dpi=300, bbox_inches="tight")
print("Diagram opgeslagen als nested_circles.png")

