# Navigate to Hadoop directory
cd ~/hadoop-3.4.1

# HDFS NameNode directory
NAMENODE_DIR="/home/$USER/hadoopdata/hdfs/namenode"

# Check if Hadoop is formatted
if [ ! -d "$NAMENODE_DIR/current" ]; then
    echo "First-time setup: Formatting NameNode..."
    bin/hdfs namenode -format
else
    echo "Hadoop is already formatted. Skipping format step."
fi

# Start Hadoop
echo "Starting Hadoop services..."
sbin/start-dfs.sh
sbin/start-yarn.sh
sleep 5

# Create input dir
bin/hdfs dfs -mkdir -p /weather

# Upload dataset
echo "Uploading dataset to HDFS..."
bin/hdfs dfs -put -f ~/weather_project/data/weather_data.csv /weather/

# Make sure output directory exists locally
mkdir -p ~/weather_project/output

##########################
# Job 1: Min/Max Values
##########################
echo "Running Job 1: Min/Max per City..."

bin/hdfs dfs -rm -r -f /weather/output_minmax

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /weather/weather_data.csv \
-output /weather/output_minmax \
-mapper ~/weather_project/scripts/mapper_min_max.py \
-reducer ~/weather_project/scripts/reducer_min_max.py

hdfs dfs -cat '/weather/output_minmax/part-*'
bin/hdfs dfs -get -f /weather/output_minmax/part-* ~/weather_project/output/results_minmax.txt

###############################
# Job 2: Monthly Avg Temp
###############################
echo "Running Job 2: Monthly Avg Temperature..."

bin/hdfs dfs -rm -r -f /weather/output_monthly_avg

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /weather/weather_data.csv \
-output /weather/output_monthly_avg \
-mapper ~/weather_project/scripts/mapper_monthly_avg.py \
-reducer ~/weather_project/scripts/reducer_monthly_avg.py

hdfs dfs -cat '/weather/output_monthly_avg/part-*'
bin/hdfs dfs -get -f /weather/output_monthly_avg/part-* ~/weather_project/output/results_monthly_avg.txt

echo "All jobs completed!"
