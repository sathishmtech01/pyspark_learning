from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("puspark")
sc = SparkContext(conf=conf)
print(sc)