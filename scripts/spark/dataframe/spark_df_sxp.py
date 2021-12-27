from pyspark.sql import SparkSession
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# df = spark.read.json("data/people.json")
# print(df.printSchema())
# print("Data Types")
# # df.dtypes
# print(df.dtypes)
# df.show()
# print(df.head())
# print(df.first())
# print(df.take(2))
# df.describe().show()
# print(df.columns)
# print(df.count())
# print(df.distinct().count())
df = spark.read.load("data/people.csv",format="csv", sep=",", inferSchema="true", header="true")
df.show()

# filter
df.select(df['age']>=20).show()
df.filter(df.age >= 20).show()

print("spark Temp tables")
# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT name FROM people")
print(sqlDF.show())

