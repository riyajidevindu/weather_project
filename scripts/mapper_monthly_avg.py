#!/usr/bin/env python3
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Location") or not line:
        continue  # Skip header or empty lines

    parts = line.split(",")
    if len(parts) == 6:
        city, datetime_str, temp, humidity, precipitation, wind = parts

        try:
            # Parse the correct date format
            dt = datetime.strptime(datetime_str.strip(), "%Y-%m-%d %H:%M:%S")
            month_key = dt.strftime("%Y-%m")
            
            # Emit raw numbers (no labels)
            print(f"{city}-{month_key}\t{temp},{humidity},{precipitation},{wind}")
        except Exception:
            continue
