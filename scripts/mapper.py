#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Location"):  # Skip header
        continue
    parts = line.split(",")
    if len(parts) == 6:
        city, datetime, temp, humidity, precip, wind = parts
        try:
            temp = float(temp)
            humidity = float(humidity)
            precip = float(precip)
            wind = float(wind)
            print(f"{city}\t{temp},{humidity},{precip},{wind}")
        except ValueError:
            continue  # Skip if conversion fails
