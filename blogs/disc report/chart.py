# Correction: Since there are 4 axes, we need 5 points (to close the chart), but had a mismatch in angles and scores.
# Correcting the number of angles and closing points.
import matplotlib.pyplot as plt
import numpy as np

# Core scores and stretch zones
core_scores = np.array([0.37, 0.20, 0.10, 0.33])
labels = ["Dominance", "Influence", "Steadiness", "Conscientiousness"]

# Radar needs to "close the loop" by repeating the first value at the end
core_scores_closed = np.concatenate([core_scores, [core_scores[0]]])
stretch_scores = np.array([0.45, 0.33, 0.25, 0.42])
stretch_scores_closed = np.concatenate([stretch_scores, [stretch_scores[0]]])

# Angles for each axis
angles = np.linspace(0, 2 * np.pi, len(core_scores) + 1)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_rmax(0.6)
ax.set_rticks([0.2, 0.4, 0.6])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=13)

# Core profile area
core_area = ax.fill(angles, core_scores_closed, alpha=0.5, label="Your Core DISC Profile", zorder=2)

# Stretch profile area
stretch_area = ax.fill(angles, stretch_scores_closed, alpha=0.25, label="Stretch Zone (Intentional Effort)", zorder=1)

# Annotation for stretch
ax.annotate(
    "Stretch zones: Greater influence & steadiness, sharper drive, deeper analysis.\nAccessed when you slow down, seek broad input, flex style.",
    xy=(np.deg2rad(65), 0.44), fontsize=11, ha='center', va='center', color='black',
    bbox=dict(boxstyle="round,pad=0.6", fc="white", ec="gray", alpha=0.85)
)

ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.10))
ax.set_title("Kundan Sen — DISC Quadrant Profile & Stretch Zones", fontsize=16, weight='bold', pad=25)

plt.tight_layout()
plt.savefig("/mnt/data/kundan_disc_quadrant_chart.png", dpi=150)
plt.close()

"/mnt/data/kundan_disc_quadrant_chart.png"
