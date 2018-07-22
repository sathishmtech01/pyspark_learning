import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 pyspark-shell'

if __name__ == '__main__':

    sc = SparkContext(appName="PythonStreamingDirectKafkaWordCount")
    ssc = StreamingContext(sc, 2)
    brokers, topic = "localhost:9092","my-topic"
    kvs = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})
    lines = kvs.map(lambda x: x[1])
    lines.pprint()
    #hdfs://localhost:9000/test
    # save in local
    #lines.saveAsTextFiles("data/output")

    # save in hdfs
    lines.saveAsTextFiles("hdfs://localhost:9000/user/sathish/test")

    ssc.start()
    ssc.awaitTermination()