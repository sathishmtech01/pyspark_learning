# Import data types
from pyspark.sql.types import *
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
#df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")

# Manually Specifying Options
df = spark.read.load("data/people.json", format="json")
#df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")


# csv file

df = spark.read.load("data/people.csv",format="csv", sep=",", inferSchema="true", header="true")
df.show()

# run sql directly on files

df = spark.sql("SELECT * FROM parquet.`data/users.parquet`")
df.show()