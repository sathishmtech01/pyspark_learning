import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import os
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"
if __name__ == "__main__":
    # uncomment while running in terminal
    # `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
    # if len(sys.argv) != 3:
    #     print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
    #     sys.exit(-1)
    # sys.argv[1], int(sys.argv[2])
    hostname = "localhost"
    port = int(9999)
    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc, 10)

    lines = ssc.socketTextStream(hostname, port)
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)
    counts.pprint()
    ssc.start()
    ssc.awaitTermination()