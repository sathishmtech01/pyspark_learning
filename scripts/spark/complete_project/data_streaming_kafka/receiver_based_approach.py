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
    # print(lines)
    # counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    # counts.pprint()
    ssc.start()
    ssc.awaitTermination()
