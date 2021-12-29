import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import upper,pandas_udf,PandasUDFType,udf
from pyspark.sql.types import *
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

spark = SparkSession.builder.appName('xxx').getOrCreate()

states = {"NY":"New York", "CA":"California", "FL":"Florida"}

broadcastStates = spark.sparkContext.broadcast(states)

data = """
James,Smith,USA,CA
"""
data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]

rdd = spark.sparkContext.parallelize(data)

def state_convert(code):
    return broadcastStates.value[code]

result = rdd.map(lambda x: (x[0],x[1],x[2],state_convert(x[3]))).collect()
input()