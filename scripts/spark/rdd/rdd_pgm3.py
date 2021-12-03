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


# Transformations
# reading a simple array/list
rdd1 = sc.parallelize([23, 45, 67, 86, 78, 27, 82 ,82, 45, 67, 86])

# To check the liost of possible fn
print(dir(rdd1))

# Performing Actions
# filter
print(rdd1.filter(lambda x:x>50).collect())
print(rdd1.sortBy(lambda x:x,True).collect())
print(rdd1.sortBy(lambda x:x,False).collect())
print(rdd1.reduce(lambda x,y: x + y))
print(rdd1.map(lambda x : x + 1).collect())
