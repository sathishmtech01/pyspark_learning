import os
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from datetime import datetime
import time
# ts stores the time in seconds
ts = time.time()
# print the current timestamp
print(ts)
# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()

# reading from string not working
sc = spark_session.sparkContext
rdd1 = sc.textFile("data.txt")
rdd1 = rdd1.map(lambda line: line.split(","))
rdd1.coalesce(1).saveAsTextFiles("streaming_op/test_"+str(ts))

print(rdd1.collect())