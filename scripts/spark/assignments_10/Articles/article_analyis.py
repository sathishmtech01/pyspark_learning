from pyspark.sql.types import *
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from pyspark.sql.functions import upper,pandas_udf,concat,col,lit,concat_ws
# from pyspark.sql import functions
# print(dir(functions))
# input()
from pyspark.sql import Row,SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

print(spark)

# Manually Specifying Options
df = spark.read.json("articles.json", multiLine=True)
print(df.schema)
# print(df.select("Heading").collect()[0])
df.select(df.Heading).show()

from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf

def func(fruit1, fruit2):
    if fruit1 == None or fruit2 == None:
        return 3
    if fruit1 == fruit2:
        return 1
    return 0

func_udf = udf(func, IntegerType())
df = df.withColumn('new_column',func_udf(df['Heading'], df['Heading']))
df.show()
# df = df.withColumn('others',concat(lit("hello"),col("Heading"),lit("hello")))

print(dir(df))
df.select(df.new_column).show()
df.head()
# https://stackoverflow.com/questions/31450846/concatenate-columns-in-apache-spark-dataframe
