import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the CSV file
csv_path = r"c:\Users\user.V915-31\Downloads\daily_CCH_RF_ALL.csv"
data = pd.read_csv(csv_path)

# Preview columns and data
data = data.dropna()
print(data.head())

# Example: Use rainfall (RF) and date for animation
# Adjust column names if needed
dates = pd.to_datetime(data['Date']) if 'Date' in data.columns else range(len(data))
rf = data['RF'] if 'RF' in data.columns else data.iloc[:,1]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, len(rf))
ax.set_ylim(0, max(rf)*1.2)
ax.set_title('Animated Rainfall Visualization')
ax.set_xlabel('Day')
ax.set_ylabel('Rainfall (mm)')

bars = ax.bar(range(len(rf)), [0]*len(rf), color=plt.cm.Blues(rf/max(rf)))

def animate(i):
    for j, b in enumerate(bars):
        b.set_height(rf[j] if j <= i else 0)
        b.set_color(plt.cm.Blues(rf[j]/max(rf)))
    return bars

ani = FuncAnimation(fig, animate, frames=len(rf), interval=50, blit=False)
plt.show()
