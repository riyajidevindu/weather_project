
# 🌤️ Weather Data Analysis Using Hadoop MapReduce
This project analyzes synthetic weather data using Hadoop Streaming with Python MapReduce scripts. It calculates the maximum and minimum values of temperature, humidity, precipitation, and wind speed for each distinct city.

# 🚀 Setup Instructions

## 1️⃣ Install Hadoop in WSL (Ubuntu)

Install Java:

```bash
    sudo apt update
    sudo apt install openjdk-11-jdk
```
Download and extract Hadoop:

```bash
    wget -c https://downloads.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
    tar -xvzf hadoop-3.4.1.tar.gz
    mv hadoop-3.4.1 ~/hadoop-3.4.1
```

Configure core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml in ~/hadoop-3.4.1/etc/hadoop/. Refer the following link for futhure details.

```bash
    https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html
```

Format HDFS:

```bash
    cd ~/hadoop-3.4.1
    bin/hdfs namenode -format
```   

Start Hadoop:

```bash
    sbin/start-dfs.sh
    sbin/start-yarn.sh
```   

## 2️⃣ Prepare Python Virtual Environment

Navigate to the project directory:

```bash
    cd ~/weather_project

```
Create and activate a virtual environment:

```bash
    python3 -m venv venv
    source venv/bin/activate
```
Install dependencies:
```bash
    pip install pandas matplotlib
```

## 3️⃣ Run the Project 

Upload Dataset to HDFS