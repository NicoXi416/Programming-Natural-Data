# Rainfall Artistic Visualization Project

This project transforms daily rainfall data from Cheung Chau into both informative and artistic visualizations using Python and matplotlib.

## Features
- **Animated Rainfall Drops:** Circles represent daily rainfall, with size and color mapped to rainfall amount.
- **Rainfall Wave Animation:** Sine wave amplitude and color reflect rainfall, creating a vibrant, evolving pattern.
- **Rain Streaks & Drops:** Combination of vertical streaks and drops, with optimized performance and fullscreen display.
- **Standard Line Chart:** Simple, clear plot of daily rainfall for reference.

## Files
- `animated_rainfall.py`: Animated rainfall drops visualization.
- `normal_rainfall_diagram.py`: Standard line chart of daily rainfall.
- `rainfall_wave_animation.py`: Artistic sine wave animation.
- `rainfall_streaks_and_drops.py`: Combined streaks and drops animation.
- `rainfall_streaks_and_drops_optimized.py`: Optimized fullscreen streaks and drops animation.
- `daily_CCH_RF_ALL.csv`: Source rainfall data (Cheung Chau).

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib numpy
   ```
2. Run any script in your Python environment:
   ```bash
   python animated_rainfall.py
   # or
   python rainfall_streaks_and_drops_optimized.py
   ```

## Data Source
- The CSV file contains daily rainfall records for Cheung Chau, with columns for year, month, day, and rainfall value.

## Customization
- You can adjust colors, animation speed, and styles in each script to suit your artistic vision.


## Artistic Concept & Creative Choices
Rainfall is a natural phenomenon that varies daily, creating patterns that are both informative and visually compelling. By transforming rainfall data into animated drops, waves, and streaks, this project explores the boundary between scientific data visualization and generative art. The size, color, and movement of each visual element are directly influenced by the rainfall amount, allowing viewers to intuitively sense changes in weather over time.

The visualizations are designed to evoke the feeling of rain—sometimes gentle, sometimes intense—while maintaining a connection to the underlying data. This approach demonstrates how environmental metrics can inspire creative expression and help communicate natural processes in a more engaging way.

## License
This project is for educational and creative purposes.
