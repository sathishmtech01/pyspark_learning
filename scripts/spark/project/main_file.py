from pyspark import SparkConf,SparkContext
# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[1]')
# Reading a single csv file
data = sc.textFile("data/2018-05-12_154616.csv")

# reading multiple csv files
data = sc.textFile("data/2018-05-12_*.csv")

# MapPartitionsRDD
print(data)

# header
header = data.first()

# extracting the header of data
print(header)#extract header
print(data.filter(lambda line:line!=header).
      map(lambda line:line.split(",")).
      map(lambda x: (x[0],x[1],int(x[3]),x[5])).
      collect())
#
print(data.count())