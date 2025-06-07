#!/usr/bin/env python3
import sys

from collections import defaultdict

city_stats = defaultdict(lambda: {
    'max_temp': float('-inf'), 'min_temp': float('inf'),
    'max_humidity': float('-inf'), 'min_humidity': float('inf'),
    'max_precip': float('-inf'), 'min_precip': float('inf'),
    'max_wind': float('-inf'), 'min_wind': float('inf'),
})

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    city, values = line.split("\t")
    temp, humidity, precip, wind = map(float, values.split(","))
    
    city_stats[city]['max_temp'] = max(city_stats[city]['max_temp'], temp)
    city_stats[city]['min_temp'] = min(city_stats[city]['min_temp'], temp)
    
    city_stats[city]['max_humidity'] = max(city_stats[city]['max_humidity'], humidity)
    city_stats[city]['min_humidity'] = min(city_stats[city]['min_humidity'], humidity)
    
    city_stats[city]['max_precip'] = max(city_stats[city]['max_precip'], precip)
    city_stats[city]['min_precip'] = min(city_stats[city]['min_precip'], precip)
    
    city_stats[city]['max_wind'] = max(city_stats[city]['max_wind'], wind)
    city_stats[city]['min_wind'] = min(city_stats[city]['min_wind'], wind)

for city, stats in city_stats.items():
    print(f"{city}\tTemperature: Max={stats['max_temp']}C Min={stats['min_temp']}C, "
          f"Humidity: Max={stats['max_humidity']}% Min={stats['min_humidity']}%, "
          f"Precipitation: Max={stats['max_precip']}mm Min={stats['min_precip']}mm, "
          f"Wind: Max={stats['max_wind']}km/h Min={stats['min_wind']}km/h")
