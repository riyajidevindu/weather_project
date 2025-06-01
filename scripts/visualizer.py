import pandas as pd
import matplotlib.pyplot as plt

# Read the reducer output
results = []
with open('../output/results.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        city = parts[0]
        values = parts[1].split(', ')
        data = {v.split('=')[0].split(': ')[1]: float(v.split('=')[1].replace('C', '').replace('%','').replace('mm','').replace('km/h','')) for v in values}
        data['City'] = city
        results.append(data)

df = pd.DataFrame(results)

# Plot max/min temperature
plt.figure(figsize=(10,5))
plt.bar(df['City'], df['Max'], color='red', label='Max')
plt.bar(df['City'], df['Min'], color='blue', label='Min')
plt.title('Max and Min Temperature by City')
plt.xlabel('City')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()
