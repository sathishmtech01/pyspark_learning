import os
import pyspark
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from pyspark import SparkConf,SparkContext

# Two ways of initializing spark context
# Initialize sparkcontext using - fn - SparkContext
sc = SparkContext(master = 'local[1]')
# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()

# Initialize sparkcontext using - fn - SparkSession.sparkContext
sc = spark_session.sparkContext