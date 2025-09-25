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

# Normalize rainfall for amplitude and color
rain_norm = (rainfall - rainfall.min()) / (rainfall.max() - rainfall.min())
colors = plt.cm.viridis(rain_norm)

x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('#222244')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.axis('off')

wave, = ax.plot([], [], lw=4)
title = ax.text(0.5, 1.05, '', ha='center', va='bottom', color='white', fontsize=18, transform=ax.transAxes)

# Animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('#222244')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    amplitude = 0.5 + rain_norm[i] * 1.5
    y = amplitude * np.sin(x)
    ax.plot(x, y, color=colors[i], lw=6)
    ax.fill_between(x, y, 0, color=colors[i], alpha=0.3)
    ax.text(0.5, 1.05, f"Rainfall: {rainfall[i]:.1f} mm\nDate: {dates[i]}", ha='center', va='bottom', color='white', fontsize=18, transform=ax.transAxes)
    return []

ani = FuncAnimation(fig, animate, frames=len(rainfall), interval=60, blit=False)
plt.show()
