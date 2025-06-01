import pandas as pd
import matplotlib.pyplot as plt
import re

# Read the reducer output
results = []
with open('output/results.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        city = parts[0]
        values = parts[1]

        # Extract numbers using regex
        matches = re.findall(r"Max=([-\d.]+).*?Min=([-\d.]+)", values)
        data = {'City': city}
        if len(matches) == 4:
            data['Temp_Max'], data['Temp_Min'] = map(float, matches[0])
            data['Humidity_Max'], data['Humidity_Min'] = map(float, matches[1])
            data['Precip_Max'], data['Precip_Min'] = map(float, matches[2])
            data['Wind_Max'], data['Wind_Min'] = map(float, matches[3])
            results.append(data)

df = pd.DataFrame(results)

# Plot max/min temperature
plt.figure(figsize=(10,5))
plt.bar(df['City'], df['Temp_Max'], color='red', label='Max Temp')
plt.bar(df['City'], df['Temp_Min'], color='blue', label='Min Temp')
plt.title('Max and Min Temperature by City')
plt.xlabel('City')
plt.ylabel('Temperature (C)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/temperature_plot.png')
print("Plot saved as output/temperature_plot.png")

