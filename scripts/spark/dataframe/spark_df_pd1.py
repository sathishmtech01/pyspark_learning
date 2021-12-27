# Different ways of creating Spark Dataframe
import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()


# creating df using row
# df = spark_session.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])
# creating df by explicit schema
# df = spark_session.createDataFrame([
#     (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
#     (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
#     (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
# ], schema='a long, b double, c string, d date, e timestamp')
# creating df on top of pandas dataframe
# pandas_df = pd.DataFrame({
#     'a': [1, 2, 3],
#     'b': [2., 3., 4.],
#     'c': ['string1', 'string2', 'string3'],
#     'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
#     'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
# })
# df = spark_session.createDataFrame(pandas_df)
# creating df on top of rdd
rdd = spark_session.sparkContext.parallelize([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
])
df = spark_session.createDataFrame(rdd, schema=['a', 'b', 'c', 'd', 'e'])
df


print(df)
print(df.show())
df.show(1)
df.show(1, vertical=True)


