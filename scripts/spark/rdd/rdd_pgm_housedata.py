from random import random
import os
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

def string_to_int(val):
    try:
        return int(float(val))
    except:
        return 0
print(string_to_int("100"))
# input()

def count(x1,x2):
    sum_=0
    # print(x2)
    for i in x2:
        # print(i)
        # input()
        sum_ = sum_ + i[1]
    return (x1,sum_)
# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()
sc = spark_session.sparkContext

# Reading a single csv file
data = sc.textFile("data/input/house/2018-05-12_154616.csv")

# reading multiple csv files
# data = sc.textFile("data/input/house/2018-05-12_*.csv")

# print(data.collect())

# filter the headers
header = data.first()
# print(header)


# remove header
step1 = data.filter(lambda line: line != header)
# print(step1.collect())

# single string line gets splitted to array of data
step2 = step1.map(lambda line: line.split(","))
# print(step2.collect())

# chossing only two set of columns
step3 = step2.map(lambda x: ((x[1]), string_to_int(x[5])))
# print(step3.collect())

# groupby city ie x[0]
step4 = step3.groupBy(lambda x: x[0])
print(step4.collect())

# aggregation
step5 = step4.map(lambda x: count(x[0],x[1]))
print(step5.collect())

# All steps in one go
# coalesce - partition -1 - revisit
step_all = data.filter(lambda line: line != header)\
                .map(lambda line: line.split(","))\
                .map(lambda x: ((x[1]), string_to_int(x[5])))\
                .groupBy(lambda x: x[0])\
                .map(lambda x: count(x[0],x[1])).map(lambda x:str(x[0])+","+str(x[1])).coalesce(3)
# print(step_all.getNumPartitions())
step_all.saveAsTextFile("data/output5")
print(step_all.collect())