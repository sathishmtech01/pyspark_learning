# Import data types
from pyspark.sql.types import *
from pyspark.sql import Row,SparkSession
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
print(spark)

df = spark.read.json("data/people.json")
df.show()
(df
    .write
    .partitionBy("name")
    .bucketBy(42, "age")
    .saveAsTable("people_partitioned_bucketed_test"))