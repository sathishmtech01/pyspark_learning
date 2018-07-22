import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 pyspark-shell'


if __name__ == '__main__':
    def test(x):
        #print(x.flatMap(lambda x:x.split('|')))
        x = x.map(lambda x:x[1])
        x.saveAsTextFiles("hdfs://localhost:9000/user/sathish/test")
        print("Hello")

    sc = SparkContext(appName="PythonStreamingRecieverKafkaWordCount")
    ssc = StreamingContext(sc, 2) # 2 second window
    broker, topic = "localhost:2181","my-topic"
    kvs = KafkaUtils.createStream(ssc,broker,"streaming-consumer",{topic:1})
    lines = kvs.map(lambda x: x[1])
    #lines.foreachRDD(lambda x:test(x))
    lines.pprint()
    # hdfs://localhost:9000/test
    # save in local
    # lines.saveAsTextFiles("data/output")

    # save in hdfs
    #lines.foreachRDD()
    lines.saveAsTextFiles("hdfs://localhost:9000/user/sathish/test/")

    ssc.start()
    ssc.awaitTermination()