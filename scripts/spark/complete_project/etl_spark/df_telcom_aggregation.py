from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
from pyspark.sql.types import StructType, StructField, IntegerType,StringType
from pyspark.sql import functions as fun

schema = StructType([
    StructField("cell_site", StringType(), True),
    StructField("phone_no", StringType(), True),
    StructField("type", StringType(), True),
    StructField("value", IntegerType(), True)])
import sys
import datetime

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

print(spark)

df = spark.read.csv("hdfs://localhost:9000/user/sathish/test/*/*",schema=schema,sep=",")
#print(df.show())

df_agg = df.groupBy("cell_site","type").agg(fun.sum("value"))

now = datetime.datetime.now()
file_name = "out_df_{}_{}_{}_{}".format(now.date(),now.hour,now.minute,now.second)
output_path = "hdfs://localhost:9000/user/sathish/tel_output/"+file_name
print(output_path)
df_agg.write.csv(output_path,mode="append")

#print(df.select("name").show())
