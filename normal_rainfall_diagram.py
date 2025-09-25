import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_path = r"g:\Python\daily_CCH_RF_ALL.csv"
data = pd.read_csv(csv_path, skiprows=2)
data = data.dropna()

# Extract date and rainfall value
years = data['年/Year'].astype(int)
months = data['月/Month'].astype(int)
days = data['日/Day'].astype(int)
rainfall = pd.to_numeric(data['數值/Value'], errors='coerce')

dates = pd.to_datetime(years.astype(str) + '-' + months.astype(str).str.zfill(2) + '-' + days.astype(str).str.zfill(2), format='%Y-%m-%d')
plt.figure(figsize=(14, 6))
plt.plot(dates, rainfall, color='royalblue', linewidth=2)
plt.title('Daily Rainfall (Cheung Chau)')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
