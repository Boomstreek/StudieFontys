import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import stats

# Data inladen
# Pad relatief aan dit script.
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, '../data_output/Feit_Gesprek.csv'))

# --- Kolommen om te plotten ---
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

colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52',
          '#8172B2', '#937860', '#DA8BC3', '#8C8C8C']

# --- Plot aanmaken ---
fig, axes = plt.subplots(2, 4, figsize=(18, 9))
fig.patch.set_facecolor('#F8F9FA')
axes = axes.flatten()

for i, col in enumerate(cols):
    ax = axes[i]
    ax.set_facecolor('#FFFFFF')
    data = df[col].dropna()

    mu, std = data.mean(), data.std()

    # Histogram (genormaliseerd naar dichtheid)
    ax.hist(data, bins=30, density=True,
            color=colors[i], alpha=0.6, edgecolor='white', linewidth=0.5)

    # Normale verdeling curve
    x = np.linspace(data.min(), data.max(), 300)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, color=colors[i], linewidth=2.2, label=f'µ={mu:.1f}, σ={std:.1f}')

    # Opmaak
    ax.set_title(labels[col], fontsize=11, fontweight='bold', pad=8)
    ax.set_xlabel('Waarde', fontsize=9, color='#444')
    ax.set_ylabel('Dichtheid', fontsize=9, color='#444')
    ax.legend(fontsize=8.5, framealpha=0.8)
    ax.tick_params(labelsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

fig.suptitle('Normale verdeling per variabele, op basis Feit_Gesprek',
             fontsize=15, fontweight='bold', y=1.01, color='#222')
plt.tight_layout(pad=2.5)
plt.savefig('normale_verdeling.png', dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print("Plot opgeslagen als normale_verdeling.png")