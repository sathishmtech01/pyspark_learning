from pyspark import SparkConf,SparkContext

# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[1]')

rdd = sc.parallelize([("a",7),("b",5)])
rdd2 = sc.parallelize([""])
# Transform
print(rdd2)
# action
# TODO
print(rdd2.count())
def test():

    return 10