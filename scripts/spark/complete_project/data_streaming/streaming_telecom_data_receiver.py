from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def combine(data):
    output = ""
    for i in len(data):
        output = output+","+str(i)
    return output

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
    #     exit(-1)
    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc, 1)

    #lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    lines = ssc.socketTextStream("127.0.0.1", 9999)
    counts = lines.flatMap(lambda line: line.split(","))\
                  .map(lambda word: combine)

    #print(counts.collect())
    counts.saveAsTextFiles("data1/output", )
    #print(counts.)
    print("Hi")
    counts.pprint()
    #["Hello testint"].pprint()
    #lines.collect().pprint()
    ssc.start()
    ssc.awaitTermination()