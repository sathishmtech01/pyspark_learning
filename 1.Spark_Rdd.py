import requests
import sys
import os
from pyspark import SparkConf,SparkContext
os.environ['SPARK_HOME'] = "/usr/lib/spark"

# Spark Content
conf = SparkConf().setMaster("local").setAppName("puspark")
sc = SparkContext(conf=conf)
print(sc)

# data download
# f = requests.get ("http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz")
# with open("data/kddcup.data_10_percent.gz","wb") as file:
#     file.write(f.content)

# data
data_file = "data/kddcup.data_10_percent.gz"
# transform
raw_data = sc.textFile(data_file)
print(raw_data)
# action
print(raw_data.count())

