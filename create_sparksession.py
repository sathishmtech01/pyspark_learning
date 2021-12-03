from random import random
import os
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
if __name__ == '__main__':
    spark_session = SparkSession.builder.master("local").\
        appName("testing").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4045").\
        getOrCreate()
