import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Load the CSV file
csv_path = r"c:\Users\user.V915-31\Downloads\daily_CCH_RF_ALL.csv"


# Read the CSV, skipping the first two header rows
data = pd.read_csv(csv_path, skiprows=2)
data = data.dropna()

# Extract date and rainfall value
years = data['年/Year']
months = data['月/Month']
days = data['日/Day']
rainfall = pd.to_numeric(data['數值/Value'], errors='coerce')

# Create a date string for each entry
dates = years.astype(str) + '-' + months.astype(str).str.zfill(2) + '-' + days.astype(str).str.zfill(2)

# Artistic Rainfall Drops Animation
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('#222244')
ax.axis('off')

# Normalize rainfall for size and color
rain_norm = (rainfall - rainfall.min()) / (rainfall.max() - rainfall.min())
sizes = 200 + rain_norm * 1800  # Circle size
colors = plt.cm.cool(rain_norm)

# Random horizontal positions for drops
np.random.seed(42)
x_pos = np.random.uniform(0.1, 0.9, len(rainfall))

def animate(i):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor('#222244')
    ax.axis('off')
    # Draw all previous drops faded, current drop bright
    ax.scatter(x_pos[:i], np.linspace(0.9, 0.1, i), s=sizes[:i], c=colors[:i], alpha=0.3, edgecolors='white', linewidths=1)
    ax.scatter(x_pos[i], 0.5, s=sizes[i], c=[colors[i]], alpha=0.9, edgecolors='white', linewidths=2)
    ax.text(0.5, 1.02, f"Rainfall: {rainfall[i]:.1f} mm\nDate: {dates[i]}", ha='center', va='bottom', color='white', fontsize=18, transform=ax.transAxes)
    return []

ani = FuncAnimation(fig, animate, frames=len(rainfall), interval=60, blit=False)
plt.show()
