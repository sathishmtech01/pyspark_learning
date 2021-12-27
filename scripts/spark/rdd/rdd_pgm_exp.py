# libraries
import os
import pyspark
from pyspark.sql import SparkSession
# ignore -
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from pyspark import SparkConf,SparkContext

# Two ways of initializing spark context
# Initialize sparkcontext using - fn - SparkContext
# sc = SparkContext(master = 'local[1]')
# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()

# Initialize sparkcontext using - fn - SparkSession.sparkContext
sc = spark_session.sparkContext
# Spark
# Python - pyspark library to connect spark

# Transformations
# reading a simple array/list
rdd1 = sc.parallelize([23, 45, 67, 86, 78, 27, 82 ,82, 45, 67, 86])
print(rdd1)
print(dir(rdd1))

# # action
# # getting count for the RDD
# print(rdd1.count())
# print(rdd1.max())
# print(rdd1.min())
#
# # get partitions
# print(rdd1.getNumPartitions())
# print(rdd1.getStorageLevel())
# # check with different storage level # https://sparkbyexamples.com/spark/spark-persistence-storage-levels/
# # different storage levels - Only Disk, Only memory , disk and memory
# # problems - realtime - faster result -> memory ,
# # problems requires intermidate storage and batch process - disk only
# # intermediate problems - mem and disk
# rdd1.persist(pyspark.StorageLevel.MEMORY_ONLY)
# print(rdd1.getStorageLevel())

print(rdd1.collect())
# filter
# print(rdd1.filter(lambda n:n>50).collect())
# print(rdd1.sortBy(lambda x:x,True).collect())
# print(rdd1.sortBy(lambda x:x,False).collect())
# revist - reduce - https://sparkbyexamples.com/apache-spark-rdd/spark-rdd-reduce-function-example/
# min(x,y), max(x,y) sum -> x+y
print(rdd1.reduce(lambda x,y : max(x,y)))

#
print(rdd1.map(lambda x : x + 1).collect())






