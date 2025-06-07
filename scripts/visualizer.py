import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# Read the reducer output
results = []
with open('output/results.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        city = parts[0]
        values = parts[1]

        # Extract max and min values using regex
        matches = re.findall(r"Max=([-\d.]+).*?Min=([-\d.]+)", values)
        data = {'City': city}
        if len(matches) == 4:
            data['Temp_Max'], data['Temp_Min'] = map(float, matches[0])
            data['Humidity_Max'], data['Humidity_Min'] = map(float, matches[1])
            data['Precip_Max'], data['Precip_Min'] = map(float, matches[2])
            data['Wind_Max'], data['Wind_Min'] = map(float, matches[3])
            results.append(data)

# Convert to DataFrame
df = pd.DataFrame(results)

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Plot function
def plot_weather_metric(df, max_col, min_col, title, ylabel, filename, color_max, color_min):
    plt.figure(figsize=(14, 7))
    x = range(len(df['City']))
    bar_width = 0.4

    # Plot bars with offset
    bar1 = plt.bar([i - bar_width/2 for i in x], df[max_col], width=bar_width, color=color_max, label=f'Max {ylabel}')
    bar2 = plt.bar([i + bar_width/2 for i in x], df[min_col], width=bar_width, color=color_min, label=f'Min {ylabel}')

    # Annotate Max bars (slightly left)
    for i, bar in enumerate(bar1):
        height = bar.get_height()
        plt.annotate(f'{height:.9f}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-10, 5),
                     textcoords="offset points",
                     ha='right', va='bottom', fontsize=7)

    # Annotate Min bars (slightly right)
    for i, bar in enumerate(bar2):
        height = bar.get_height()
        plt.annotate(f'{height:.9f}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(10, 5),
                     textcoords="offset points",
                     ha='left', va='bottom', fontsize=7)

    plt.title(title, fontsize=15, fontweight='bold')
    plt.xlabel('City')
    plt.ylabel(ylabel)
    plt.xticks(ticks=x, labels=df['City'], rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'output/{filename}')
    print(f"✅ Saved: output/{filename}")
    plt.close()

# Generate all plots
plot_weather_metric(df, 'Temp_Max', 'Temp_Min', 'Temperature by City', 'Temperature (°C)', 'temperature_plot.png', 'tomato', 'skyblue')
plot_weather_metric(df, 'Humidity_Max', 'Humidity_Min', 'Humidity by City', 'Humidity (%)', 'humidity_plot.png', 'gold', 'deepskyblue')
plot_weather_metric(df, 'Precip_Max', 'Precip_Min', 'Precipitation by City', 'Precipitation (mm)', 'precip_plot.png', 'lightgreen', 'mediumseagreen')
plot_weather_metric(df, 'Wind_Max', 'Wind_Min', 'Wind Speed by City', 'Wind Speed (km/h)', 'wind_plot.png', 'orange', 'turquoise')
