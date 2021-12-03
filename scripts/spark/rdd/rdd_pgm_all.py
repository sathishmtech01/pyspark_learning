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
# get partitions
print(rdd1.getNumPartitions())

print(rdd1.getStorageLevel())
# check with different storage level
rdd1.persist(pyspark.StorageLevel.MEMORY_AND_DISK_2 )
print(rdd1.getStorageLevel())

# return the o/p
print(rdd1.collect())
# count
print(rdd1.count())
# distinct records
print(rdd1.distinct().collect())

print(rdd1.first())

print(rdd1.take(5))
input()

# filter
print(rdd1.filter(lambda x:x>50).collect())


print(rdd1.sortBy(lambda x:x,True).collect())
print(rdd1.sortBy(lambda x:x,False).collect())
print(rdd1.reduce(lambda x,y: x + y))
print(rdd1.map(lambda x : x + 1).collect())


rdd2 = sc.parallelize([23, 45, 67, 86, 78, 27, 82 ,82, 45, 67, 86])

print(rdd1.union(rdd2).collect())
print(rdd1.intersection(rdd2).collect())
print(rdd1.cartesian(rdd2).collect())


