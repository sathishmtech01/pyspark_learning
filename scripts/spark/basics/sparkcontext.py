from pyspark import SparkContext
sc = SparkContext(master = 'local[2]')

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