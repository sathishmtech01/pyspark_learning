
from pyspark import SparkContext
# initialization of spark
# master is machine | server allooting
sc = SparkContext(master = 'local[*]')

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