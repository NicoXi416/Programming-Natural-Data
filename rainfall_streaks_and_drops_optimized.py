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

# Pre-create artists for blitting
streak, = ax.plot([], [], color='deepskyblue', alpha=0.8, linewidth=8)
drop = ax.scatter([], [], s=[], c=[], alpha=0.9, edgecolors='white', linewidths=2)
txt = ax.text(0.5, 1.02, '', ha='center', va='bottom', color='white', fontsize=18, transform=ax.transAxes)

# Animation function
# Only update current streak/drop for performance

def init():
    streak.set_data([], [])
    drop.set_offsets(np.empty((0, 2)))
    drop.set_sizes([])
    drop.set_color([])
    txt.set_text('')
    return streak, drop, txt

def animate(i):
    # Streak
    streak.set_data([x_pos[i], x_pos[i]], [0.95, 0.95 - rain_norm[i]*0.7])
    streak.set_color(colors[i])
    # Drop
    drop.set_offsets([[x_pos[i], 0.95 - rain_norm[i]*0.7]])
    drop.set_sizes([200 + rain_norm[i]*1200])
    drop.set_color([colors[i]])
    # Text
    txt.set_text(f"Rainfall: {rainfall[i]:.1f} mm\nDate: {dates[i]}")
    return streak, drop, txt

ani = FuncAnimation(fig, animate, frames=len(rainfall), init_func=init, interval=60, blit=True)
plt.show()
