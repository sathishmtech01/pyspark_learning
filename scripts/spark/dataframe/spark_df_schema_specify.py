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

sc = spark.sparkContext

# Load a text file and convert each line to a Row.
lines = sc.textFile("data/people.txt")
parts = lines.map(lambda l: l.split(","))
# Each line is converted to a tuple.
people = parts.map(lambda p: (p[0], int(p[1].strip())))
print(people.collect())
# The schema is encoded in a string.
schemaString = "name age"
print(schemaString)
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]

fields = [StructField("name", StringType(), True),StructField("age", IntegerType(), True)]
print(fields)
schema = StructType(fields)
print(schema)
# Apply the schema to the RDD.
schemaPeople = spark.createDataFrame(people, schema)

# Creates a temporary view using the DataFrame
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
results = spark.sql("SELECT name FROM people")

results.show()