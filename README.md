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


# Setp 5 connect master to run py

![image](https://user-images.githubusercontent.com/75282285/225354097-83c484e9-81b5-4b45-90d9-361a9395bb16.png)
run the command : `spark-submit main.py`
![image](https://user-images.githubusercontent.com/75282285/225354002-fb05f638-4cf3-4b93-bbdc-b51e56abbb03.png)


