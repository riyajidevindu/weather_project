# Navigate to Hadoop directory
cd ~/hadoop-3.4.1

# Path to HDFS metadata (NameNode directory) from hdfs-site.xml
NAMENODE_DIR="/home/$USER/hadoopdata/hdfs/namenode"

# Check if Hadoop has been formatted already
if [ ! -d "$NAMENODE_DIR/current" ]; then
    echo "🟢 First-time setup: Formatting NameNode..."
    bin/hdfs namenode -format
else
    echo "✅ Hadoop is already formatted. Skipping format step."
fi

# Start HDFS and YARN
echo "🚀 Starting Hadoop services..."
sbin/start-dfs.sh
sbin/start-yarn.sh

# Wait a few seconds to make sure Hadoop services are up
sleep 5

# Create HDFS input directory (if not exists)
echo "📁 Creating /weather in HDFS (if not exists)..."
bin/hdfs dfs -mkdir -p /weather

# Upload dataset to HDFS
echo "📤 Uploading dataset to HDFS..."
bin/hdfs dfs -put -f ~/weather_project/data/weather_data.csv /weather/

# Remove existing output if it exists
echo "🧹 Cleaning previous output directory..."
bin/hdfs dfs -rm -r -f /weather/output

# Run Hadoop Streaming job
echo "🔄 Running MapReduce job..."
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /weather/weather_data.csv \
-output /weather/output \
-mapper ~/weather_project/scripts/mapper.py \
-reducer ~/weather_project/scripts/reducer.py

# Download and show results
echo "📥 Retrieving results from HDFS..."
bin/hdfs dfs -get -f /weather/output/part-* ~/weather_project/output/results.txt

echo "📄 MapReduce Output:"
cat ~/weather_project/output/results.txt
