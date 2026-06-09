import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- Paden ---
BASE = os.path.dirname(os.path.abspath(__file__))
df      = pd.read_csv(os.path.join(BASE, '../data_output/Feit_Gesprek.csv'))
df_gem  = pd.read_csv(os.path.join(BASE, '../data_output/Dim_Gemeente.csv'))

# --- Samenvoegen ---
merged = df.merge(df_gem, on='gemeente_id')

# --- Kolommen en labels ---
cols = [
    'leefstijlscore_totaal',
    'score_voeding',
    'score_beweging',
    'score_ontspanning',
    'score_slaap',
    'score_verbinding',
    'score_middelen',
    'duur_minuten',
]

labels = {
    'leefstijlscore_totaal': 'Leefstijlscore Totaal',
    'score_voeding':         'Score Voeding',
    'score_beweging':        'Score Beweging',
    'score_ontspanning':     'Score Ontspanning',
    'score_slaap':           'Score Slaap',
    'score_verbinding':      'Score Verbinding',
    'score_middelen':        'Score Middelen',
    'duur_minuten':          'Duur (minuten)',
}

gemeentes   = sorted(merged['gemeente_naam'].unique())
colors      = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2']
gem_colors  = dict(zip(gemeentes, colors))

# --- Plot ---
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.patch.set_facecolor('#F8F9FA')
axes = axes.flatten()

for i, col in enumerate(cols):
    ax = axes[i]
    ax.set_facecolor('#FFFFFF')

    # Data per gemeente groeperen
    data_per_gem = [merged[merged['gemeente_naam'] == g][col].dropna() for g in gemeentes]

    bp = ax.boxplot(
        data_per_gem,
        patch_artist=True,
        notch=False,
        widths=0.5,
        medianprops=dict(color='white', linewidth=2),
        whiskerprops=dict(linewidth=1.2),
        capprops=dict(linewidth=1.2),
        flierprops=dict(marker='o', markersize=3, alpha=0.4),
    )

    # Kleuren per gemeente
    for patch, gem in zip(bp['boxes'], gemeentes):
        patch.set_facecolor(gem_colors[gem])
        patch.set_alpha(0.75)

    ax.set_title(labels[col], fontsize=11, fontweight='bold', pad=8)
    ax.set_ylabel('Waarde', fontsize=9, color='#444')
    ax.set_xticks(range(1, len(gemeentes) + 1))
    ax.set_xticklabels(gemeentes, rotation=20, ha='right', fontsize=8)
    ax.tick_params(labelsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# --- Legenda ---
legend_patches = [mpatches.Patch(color=gem_colors[g], label=g) for g in gemeentes]
fig.legend(handles=legend_patches, title='Gemeente', loc='lower center',
           ncol=len(gemeentes), fontsize=9, title_fontsize=10,
           bbox_to_anchor=(0.5, -0.02), framealpha=0.9)

fig.suptitle('Boxplots per gemeente — Feit_Gesprek',
             fontsize=15, fontweight='bold', y=1.01, color='#222')
plt.tight_layout(pad=2.5)
plt.savefig(os.path.join(BASE, 'boxplot_gemeente.png'),
            dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()
print("Plot opgeslagen als boxplot_gemeente.png")