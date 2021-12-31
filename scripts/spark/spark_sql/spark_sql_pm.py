# Import data types
from pyspark.sql.types import *
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from pyspark.sql import Row,SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

print(spark)

# Generic Load/Save Functions
df = spark.read.load("data/users.parquet")
df.show()
df.printSchema()
#df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")

# Manually Specifying Options
df = spark.read.load("data/people.json", format="json")
#df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")


# csv file

df = spark.read.load("data/people.csv",format="csv", sep=",", inferSchema="true", header="true")
df.show()

# Bucketing
print("Hello")
# df.write.bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed")

# run sql directly on files

df = spark.sql("SELECT * FROM parquet.`data/users.parquet`")
df.show()

print("hello")
df = spark.sql("SELECT * FROM parquet.`spark-warehouse/people_partitioned/favorite_color=__HIVE_DEFAULT_PARTITION__/*.parquet`")
df.show()
print("hello")

# df = spark.sql("SELECT * FROM parquet.`namesAndAges.parquet`")
# df1 = spark.sql("SELECT * FROM parquet.`spark-warehouse/people_partitioned_bucketed_test/name=Andy/*.parquet`")
# print("Spark warehouse")
# df1.show()
#df.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")

df = spark.read.parquet("data/users.parquet")
df.show()
(df
    .write
    .partitionBy("favorite_color")
    .saveAsTable("people_partitioned"))