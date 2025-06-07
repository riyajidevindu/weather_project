import sys

current_key = None
sum_temp = sum_humidity = sum_precip = sum_wind = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    try:
        temp, humidity, precip, wind = map(float, value.split(","))
    except:
        continue

    if key == current_key:
        sum_temp += temp
        sum_humidity += humidity
        sum_precip += precip
        sum_wind += wind
        count += 1
    else:
        if current_key:
            print(f"{current_key}\tAvg_Temp={sum_temp/count:.2f}, "
                  f"Avg_Humidity={sum_humidity/count:.2f}, "
                  f"Avg_Precip={sum_precip/count:.2f}, "
                  f"Avg_Wind={sum_wind/count:.2f}")
        current_key = key
        sum_temp = temp
        sum_humidity = humidity
        sum_precip = precip
        sum_wind = wind
        count = 1

if current_key:
    print(f"{current_key}\tAvg_Temp={sum_temp/count:.2f}, "
          f"Avg_Humidity={sum_humidity/count:.2f}, "
          f"Avg_Precip={sum_precip/count:.2f}, "
          f"Avg_Wind={sum_wind/count:.2f}")