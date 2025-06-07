import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import re
import os

# Load and parse reducer output
data = []
with open('output/results_monthly_avg.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue

        city_month = parts[0]
        values = parts[1]

        # FIX: Safely extract city and month
        month = city_month[-7:]
        city = city_month[:-8].strip()

        # Extract numeric values
        matches = re.findall(r"[-+]?\d*\.\d+|\d+", values)
        if len(matches) == 4:
            temp, humidity, precip, wind = map(float, matches)
            data.append({
                "City": city,
                "Month": month,
                "Avg_Temp": temp,
                "Avg_Humidity": humidity,
                "Avg_Precip": precip,
                "Avg_Wind": wind
            })

# Convert to DataFrame
df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'], format="%Y-%m")
df.sort_values(by=["City", "Month"], inplace=True)

# Create output folder
os.makedirs("visualizations/month_avg", exist_ok=True)

# Plotting function
def plot_metric(df, column, title, ylabel, filename, color):
    plt.figure(figsize=(14, 7))
    ax = plt.gca()

    unique_months = sorted(df['Month'].unique())

    for city in df['City'].unique():
        city_data = df[df['City'] == city]
        ax.plot(city_data['Month'], city_data[column], marker='o', label=city)

    ax.set_title(title, fontsize=15, fontweight='bold')
    ax.set_xlabel("Month")
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend(title="City")

    ax.set_xticks(unique_months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b')) 
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(f"visualizations/month_avg/{filename}")
    print(f"✅ Saved: visualizations/month_avg/{filename}")
    plt.close()


# Generate 4 weather plots
plot_metric(df, "Avg_Temp", "Monthly Avg Temperature", "Temperature (°C)", "monthly_temp_trends.png", "tomato")
plot_metric(df, "Avg_Humidity", "Monthly Avg Humidity", "Humidity (%)", "monthly_humidity_trends.png", "skyblue")
plot_metric(df, "Avg_Precip", "Monthly Avg Precipitation", "Precipitation (mm)", "monthly_precip_trends.png", "seagreen")
plot_metric(df, "Avg_Wind", "Monthly Avg Wind Speed", "Wind Speed (km/h)", "monthly_wind_trends.png", "orange")
