import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Load the CSV file
csv_path = r"g:\Python\daily_CCH_RF_ALL.csv"
data = pd.read_csv(csv_path, skiprows=2)
data = data.dropna()

# Extract date and rainfall value
years = data['年/Year'].astype(int)
months = data['月/Month'].astype(int)
days = data['日/Day'].astype(int)
rainfall = pd.to_numeric(data['數值/Value'], errors='coerce')

dates = years.astype(str) + '-' + months.astype(str).str.zfill(2) + '-' + days.astype(str).str.zfill(2)

# Normalize rainfall for height and color
rain_norm = (rainfall - rainfall.min()) / (rainfall.max() - rainfall.min())
colors = plt.cm.Blues(rain_norm)

# Set up positions for rain streaks/drops
x_pos = np.linspace(0.1, 0.9, len(rainfall))
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_facecolor('#222244')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

def animate(i):
    ax.clear()
    ax.set_facecolor('#222244')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    # Draw faded previous streaks
    for j in range(i):
        ax.plot([x_pos[j], x_pos[j]], [0.95, 0.95 - rain_norm[j]*0.7], color=colors[j], alpha=0.2, linewidth=6)
        ax.scatter(x_pos[j], 0.95 - rain_norm[j]*0.7, s=100 + rain_norm[j]*800, c=[colors[j]], alpha=0.2, edgecolors='white', linewidths=1)
    # Draw current streak and drop
    ax.plot([x_pos[i], x_pos[i]], [0.95, 0.95 - rain_norm[i]*0.7], color=colors[i], alpha=0.8, linewidth=8)
    ax.scatter(x_pos[i], 0.95 - rain_norm[i]*0.7, s=200 + rain_norm[i]*1200, c=[colors[i]], alpha=0.9, edgecolors='white', linewidths=2)
    ax.text(0.5, 1.02, f"Rainfall: {rainfall[i]:.1f} mm\nDate: {dates[i]}", ha='center', va='bottom', color='white', fontsize=18, transform=ax.transAxes)
    return []

ani = FuncAnimation(fig, animate, frames=len(rainfall), interval=60, blit=False)
plt.show()
