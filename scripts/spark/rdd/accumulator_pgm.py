import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import upper,pandas_udf,PandasUDFType,udf
from pyspark.sql.types import *
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
spark = SparkSession.builder.appName('accumulatorrr').getOrCreate()
j=0
for i in [1,2,3,4,5]:
    j=j+i
print(j)


accum=spark.sparkContext.accumulator(0)
rdd=spark.sparkContext.parallelize([1,2,3,4,5])
rdd.foreach(lambda x:accum.add(x))
print(accum.value)

accuSum=spark.sparkContext.accumulator(0)
def countFun(x):
    global accuSum
    accuSum+=x
rdd.foreach(countFun)
print(accuSum.value)

accumCount=spark.sparkContext.accumulator(0)
rdd2=spark.sparkContext.parallelize([1,2,3,4,5])
rdd2.foreach(lambda x:accumCount.add(1))
print(accumCount.value)