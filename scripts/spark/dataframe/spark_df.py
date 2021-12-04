from pyspark.sql import SparkSession
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

print(spark)

df = spark.read.json("data/people.json")

print(df.printSchema())
print("Data Types")
# df.dtypes
print(df.dtypes)
df.show()
df.head()
df.first()
df.take(2)
df.describe().show()
df.columns
df.count()
df.distinct().count()
df.printSchema()

input()
print(df.select("name").show())

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

sqlDF = spark.sql("SELECT * FROM people")
print(sqlDF.show())


# Register the DataFrame as a global temporary view
df.createGlobalTempView("people")

# TODO : How to check the spark session is active or not in pyspark.
# Global temporary view is tied to a system preserved database `global_temp`
spark.sql("SELECT * FROM global_temp.people").show()
print(spark)

print("Test")
spark_new = spark.newSession()
print(spark_new)
print()
spark_new.sql("SELECT * FROM global_temp.people").show()
# error
#spark.newSession().sql("SELECT * FROM people").show()