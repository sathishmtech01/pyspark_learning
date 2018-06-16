from pyspark import SparkConf,SparkContext
import sys

# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[1]')

# Reading a single csv file
data = sc.textFile("data/input/house/2018-05-12_154616.csv")

# reading multiple csv files
data = sc.textFile("data/input/house/2018-05-12_*.csv")

# MapPartitionsRDD
print(data)

# Module for changing string to int
def string_to_int(val):
    try:
        return int(float(val))
    except:
        return 0

# Module getting the count
def count(x):
    temp=0
    for val in list(x):
        temp = temp + val[1]
        #out = (val[0],temp)
        out = str(val[0])+","+str(temp)
    #print(out)
    return out

# header
# address,city,state,zip,price,sqft,bedrooms,bathrooms,days_on_zillow,sale_type,url
header = data.first()

# extracting the header of data
print(header)#extract header

# Group by city and find the sum
# transform : map and groupby
# coalesce 1 - denoting the number of partition data
get_count = data.filter(lambda line: line != header).\
            map(lambda line: line.split(",")).map(
    lambda x: ((x[1]), string_to_int(x[5]))).\
    groupBy(lambda x: x[0]).\
    map(lambda x: (count(x[1]))).coalesce(1)

# save as text file
#get_count.saveAsTextFile("data/output2")

# see all the data
# action : collect and count
print(get_count.collect())
print(get_count.count())
# get count of data
print(data.count())
