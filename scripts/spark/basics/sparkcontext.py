import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
from pyspark import SparkConf,SparkContext

# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[2]')
print(sc)

#
# # spark version
print(sc.version)
# # python version
print(sc.pythonVer)
# #
print(sc.master)
print(str(sc.sparkHome))
print(str(sc.sparkUser()))
#
print(sc.appName) # Return application name
print(sc.applicationId) # Retrieve application ID
print(sc.defaultParallelism) # Return default level of parallelism
print(sc.defaultMinPartitions)


config = (SparkConf().
        setMaster("local").
        setAppName("myapp").
        set("spark.executer.memory","1g"))

# getting the configuration

print(config.getAll())
input()

sc= SparkContext(conf=config)

# spark version
print(sc.version)
# python version
print(sc.pythonVer)
#
print(sc.master)
print(str(sc.sparkHome))
print(str(sc.sparkUser()))

print(sc.appName) # Return application name
print(sc.applicationId) # Retrieve application ID
print(sc.defaultParallelism) # Return default level of parallelism
print(sc.defaultMinPartitions)


# Deploying
# sathish@sathish-Latitude-3480:/usr/lib/spark$ ./bin/spark-submit '/home/sathish/Sathish/BOL/scripts/spark/basics/sparkcontext.py' &
