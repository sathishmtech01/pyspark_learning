import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import upper,pandas_udf,PandasUDFType,udf
from pyspark.sql.types import *
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()


# creating df on top of pandas dataframe
df = spark_session.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
df.show()
df.groupby('color').avg().show()

df.groupby('color').avg().show()
schema = StructType([
    StructField("color", StringType()),
    StructField("v1", DoubleType()),
])
df = df.withColumn('v', df.v1)
schema = StructType([
    StructField("color", StringType()),
    StructField("fruit", StringType()),
    StructField("v1", LongType()),
    StructField("v2", LongType()),
    StructField("v", DoubleType()),
])
print(schema)
# input()
@pandas_udf(schema, functionType=PandasUDFType.GROUPED_MAP)
def g1(df):
    print(df)
    v = df.v
    return df.assign(v=(v - v.mean()) / v.std())

@udf(returnType=IntegerType())
def g(df):
    print(df)
    return df+1

df.groupby("color").apply(g1).show()



from pyspark.sql.functions import pandas_udf, PandasUDFType
df = spark_session.createDataFrame(
          [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
        ("id", "v"))  # doctest: +SKIP
@pandas_udf("id long, v double", PandasUDFType.GROUPED_MAP)  # doctest: +SKIP
def normalize(pdf):
    v = pdf.v
    return pdf.assign(v=(v - v.mean()) / v.std())
df.groupby("id").apply(normalize).show()  # doctest: +SKIP


# df.show()