import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Location"):
        continue

    parts = line.split(",")
    if len(parts) == 6:
        city, datetime_str, temp, humidity, precip, wind = parts

        try:
            dt = datetime.strptime(datetime_str.strip(), "%Y-%m-%d %H:%M:%S")
            temp = float(temp)
            humidity = float(humidity)
            precip = float(precip)
            wind = float(wind)

            month_key = dt.strftime("%Y-%m")
            print(f"{city}-{month_key}\t{temp},{humidity},{precip},{wind}")
        except Exception:
            continue