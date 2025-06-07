#!/usr/bin/env python3
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Location") or not line:
        continue  # Skip header or empty lines

    parts = line.split(",")
    if len(parts) != 6:
        continue  # Malformed line

    city, datetime_str, temp, humidity, precipitation, wind = parts

    try:
        dt = datetime.strptime(datetime_str.strip(), "%Y-%m-%d %H:%M:%S")
        month_key = dt.strftime("%Y-%m")

        print(f"{city}-{month_key}\tTemperature:{temp},Humidity:{humidity},Precipitation:{precipitation},Wind:{wind}")
    except Exception as e:
        continue  # Skip lines with date parse errors
