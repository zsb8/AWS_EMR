# AWS_EMR
Use EMR to read CVS and store in Spark

# Step 1 Create EMR
![image](https://user-images.githubusercontent.com/75282285/225351734-cebdc816-7c2c-464b-9c48-fc946f063cc6.png)

choose Spark
![image](https://user-images.githubusercontent.com/75282285/225352033-7603dcdd-9aed-484c-93f4-872d83dbb004.png)

# Step 2 Place data on S3
I use the data from https://insights.stackoverflow.com/survey

![image](https://user-images.githubusercontent.com/75282285/225352416-707148fd-1078-4dbd-9da6-262f457286fe.png)

![image](https://user-images.githubusercontent.com/75282285/225352682-f4179e6d-142a-4894-8627-03cdc8cb05ff.png)

# Step 3 Make program with PySpark
``` 
from pyspark.sql import SparkSession    
from pyspark.sql.functions import col
```
Read data 
```
spark = SparkSession.builder.appName('zsbDemoApp').getOrCreate()
all_data = spark.read.csv(S3_DATA_SOURCE_PATH, header=True)
```
Write data
```
selected_data = all_data.where((col('Country') == 'United States') & (col('WorkWeekHrs') > 45))
selected_data.write.mode('overwrite').parquet(S3_DATA_OUTPUT_PATH)
```
# Step 4 Set the inbound policy
![image](https://user-images.githubusercontent.com/75282285/225353850-2d9743c9-3b6c-4756-99e1-cd8b56d499f2.png)


# Step 5 Connect to master and run py

![image](https://user-images.githubusercontent.com/75282285/225354097-83c484e9-81b5-4b45-90d9-361a9395bb16.png)
run the command : `spark-submit main.py`
![image](https://user-images.githubusercontent.com/75282285/225354002-fb05f638-4cf3-4b93-bbdc-b51e56abbb03.png)

# Step 6 Check S3
The program will read the CSV, filt data and place the result on S3 output folder.
![image](https://user-images.githubusercontent.com/75282285/225355409-67e6dafa-bbc9-4a34-a48f-cedb414c1af5.png)

# Step 7 Monitor
![image](https://user-images.githubusercontent.com/75282285/225355577-7a5d7ce5-dbfb-47e5-81aa-a5a69f47d13c.png)
HDFS Name Node
![image](https://user-images.githubusercontent.com/75282285/225355739-46e098c1-1db6-4cd9-b167-da32cf8a5972.png)
Resource Manager
![image](https://user-images.githubusercontent.com/75282285/225355848-07b514dc-2d7c-4728-9147-c50dfd395fe6.png)
Spark UI 
![image](https://user-images.githubusercontent.com/75282285/225355970-49bc9671-d5d7-489b-bc7c-cbe6db5daba3.png)











