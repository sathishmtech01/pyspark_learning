import os
import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()


# creating df on top of pandas dataframe
s = ps.Series([1, 3, 5, np.nan, 6, 8])
print(s)

