from flask import Flask, Response
from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('my-topic', group_id='view',bootstrap_servers=['0.0.0.0:9092'])
while True:
    for msg in consumer:
        print(msg.value)
