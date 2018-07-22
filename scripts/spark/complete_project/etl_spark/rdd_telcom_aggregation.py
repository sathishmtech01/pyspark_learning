from pyspark import SparkConf,SparkContext
import sys
import datetime

# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[1]')


# reading multiple csv files
# sample data
data = sc.textFile("hdfs://localhost:9000/user/sathish/test/*/*")
# all data
#data = sc.textFile("hdfs://localhost:9000/user/sathish/test/*/*")

def count(x):

    #input()
    temp=0
    for val in list(x):
        temp = temp + val[3]
        #out = (val[0],temp)
        out = str(val[0])+","+str(val[2])+","+str(temp)
    #print(out)


    return out
#print(data.collect())

get_count = data.map(lambda line: line.split(",")).\
            map(lambda x : (x[0],x[1],x[2],int(x[3]))).\
            groupBy(lambda x: (x[0],x[2])).\
            map(lambda x: (count(x[1]))).\
            coalesce(1)

print(get_count.collect())

now = datetime.datetime.now()
file_name = "out_rdd_{}_{}_{}_{}".format(now.date(),now.hour,now.minute,now.second)
output_path = "hdfs://localhost:9000/user/sathish/tel_output/"+file_name
print(output_path)
get_count.saveAsTextFile(output_path)
