"""
csk@csk-ai-revolution:~/sparkscala/spark-2.4.0-bin-hadoop2.6/bin$ ./pyspark
Python 2.7.12 (default, Mar  1 2021, 11:38:31) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
2021-11-27 16:19:00 WARN  Utils:66 - Your hostname, csk-ai-revolution resolves to a loopback address: 127.0.1.1; using 192.168.1.7 instead (on interface wlp1s0)
2021-11-27 16:19:00 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
2021-11-27 16:19:11 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Python version 2.7.12 (default, Mar  1 2021 11:38:31)
SparkSession available as 'spark'.
>>> sc = spark.sparkContext
>>> rdd = sc.parallelize([("a",7),("b",5)])
>>> rdd.count()
2                                                                               
>>> rdd = sc.parallelize([1,2,3])
>>> rdd.count()
3
>>> 
"""