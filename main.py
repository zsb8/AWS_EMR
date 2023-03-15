from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_DATA_SOURCE_PATH = 's3://test-zsb/data-source/survey_results_public.csv'
S3_DATA_OUTPUT_PATH = 's3://test-zsb/data-output'


def main():
    spark = SparkSession.builder.appName('zsbDemoApp').getOrCreate()
    all_data = spark.read.csv(S3_DATA_SOURCE_PATH, header=True)
    print(f'Total number of record in the source is {all_data.count()}')
    selected_data = all_data.where((col('Country') == 'United States') & (col('WorkWeekHrs') > 45))
    print(f'The number of negineers who work more than 45 hours a week in the US is {selected_data.count()}')
    selected_data.write.mode('overwrite').parquet(S3_DATA_OUTPUT_PATH)
    print(f'Select data was successfully saved to s3 {S3_DATA_OUTPUT_PATH}')


if __name__ == '__main__':
    main()
