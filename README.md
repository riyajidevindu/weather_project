
# 🌤️ Weather Data Analysis Using Hadoop MapReduce
This project analyzes synthetic weather data using Hadoop Streaming with Python MapReduce scripts. It calculates the maximum and minimum values of temperature, humidity, precipitation, and wind speed for each distinct city.

# 🚀 Setup Instructions

## 1️⃣ Install WSL and Ubuntu on Windows

Open **PowerShell as Administrator** and run:

```bash
    wsl --install
```
After installation, restart and launch Ubuntu.
Set up your username and password. 
(If Ubuntu is not installed use Microsoft Store and Install)

Update Ubuntu:

```bash
    sudo apt update && sudo apt upgrade
```

## 2️⃣ Setup SSH (for Hadoop)
Hadoop uses SSH to manage nodes, even in a single-node setup.
First remove existing OpenSSH server and client (Due to Issue):
```bash
    sudo apt --assume-yes remove openssh-server
```
Reinstall OpenSSH server and client:
```bash
    sudo apt --assume-yes install openssh-server
```

Generate SSH Key (no passphrase):
```bash
    ssh-keygen -t rsa
```
Then press enter key twice for no passphrase

Add SSH key to authorized keys:
```bash
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
```

Start SSH service:
```bash
    sudo service ssh start
```
Test SSH Connection:
```bash
    ssh localhost
```

## 3️⃣ Install Java (Hadoop requirement)

Install Java:

```bash
    sudo apt install openjdk-11-jdk
```

## 4️⃣ Download and Extract Hadoop

Download and extract Hadoop:

```bash
    wget -c https://downloads.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
    tar -xvzf hadoop-3.4.1.tar.gz
    mv hadoop-3.4.1 ~/hadoop-3.4.1
```
## 5️⃣ Configure Hadoop

Move to hadoop file:

```bash
    cd ~/hadoop-3.4.1
```
Configure core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml in ~/hadoop-3.4.1/etc/hadoop/. Refer the following link for futhure details (Configurations code that need to use in the upcomming steps).
```bash
    https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html
```
In this approach we used VSCode for editing the files.
To open core-site.xml file.

```bash
    code etc/hadoop/core-site.xml
```
Copy and paste the relevent configuration code at the end of the file and save it.

Next open hdfs-site.xml file.

```bash
    code etc/hadoop/hdfs-site.xml
```
Copy and paste the relevent configuration code at the end of the file and save it.

Next open mapred-site.xml file.

```bash
    code etc/hadoop/mapred-site.xml
```
Copy and paste the relevent configuration code at the end of the file and save it.

Next open mapred-yarn.xml file.

```bash
    code etc/hadoop/yarn-site.xml
```
Copy and paste the relevent configuration code at the end of the file and save it.

## 6️⃣ Update .bashrc for Environment Variables

Open .bashrc file.
```bash
    code ~/.bashrc
``` 

Add the following codes to the end of the file and save. Edit the jave and hadoop verions according to your vesions.

```bash
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
    export HADOOP_HOME=~/hadoop-3.4.1
    export PATH=$PATH:$HADOOP_HOME/bin
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/
    export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar
``` 
Apply changes:

```bash
   source ~/.bashrc
``` 

## Step 7️⃣: Format HDFS and Start Hadoop

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
## 8️⃣ Clone the Repository into the Root Directory

Move to root directory:

```bash
    cd ~/
``` 

Clone the project:

```bash
    git clone https://github.com/riyajidevindu/weather_project.git
```

## 9️⃣ Prepare Python Virtual Environment

Install Python 3 and pip

```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
```

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

## 🔟 Upload Dataser & Run the Project 

Upload Dataset to HDFS
```bash
    ./run_hadoop.sh
```

## 1️⃣1️⃣ Visualize Analysis Results
```bash
    python scripts/visualizer.py
```
This saves plots in output/.

## 1️⃣2️⃣ Access Hadoop Web UIs
Get your WSL IP:
```bash
    hostname -I
```

Open in your Windows browser:
```bash
    HDFS UI (NameNode): http://<WSL-IP>:9870 or http://localhost:9870
    YARN UI (ResourceManager): http://<WSL-IP>:8088 or http://localhost:8088
```

## 1️⃣3️⃣: Stop Hadoop and WSL

```bash
    cd ~/hadoop-3.4.1
    sbin/stop-dfs.sh
    sbin/stop-yarn.sh
```
```bash
    wsl --shutdown
```
