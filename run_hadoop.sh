#!/bin/bash
cd ~/hadoop-3.4.1
bin/hdfs dfs -mkdir -p /weather
bin/hdfs dfs -put -f ~/weather_project/data/weather_data.csv /weather/
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /weather/weather_data.csv \
-output /weather/output \
-mapper ~/weather_project/scripts/mapper.py \
-reducer ~/weather_project/scripts/reducer.py
bin/hdfs dfs -cat /weather/output/part-*
