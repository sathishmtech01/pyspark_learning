import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 pyspark-shell'


if __name__ == '__main__':

    sc = SparkContext(appName="PythonStreamingRecieverKafkaWordCount")
    ssc = StreamingContext(sc, 2) # 2 second window
    broker, topic = "localhost:2181","my-topic"
    kvs = KafkaUtils.createStream(ssc,broker,"streaming-consumer",{topic:1})
    lines = kvs.map(lambda x: x[1])
    lines.pprint()
    # hdfs://localhost:9000/test
    # save in local
    # lines.saveAsTextFiles("data/output")

    # save in hdfs
    lines.saveAsTextFiles("hdfs://localhost:9000/test")

    ssc.start()
    ssc.awaitTermination()