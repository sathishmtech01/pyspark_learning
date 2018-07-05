##Kafka Streaming

1. Producer
2. Consumer

## Spark Kafka

1. Receiver based approach
2. Direct approach


Google drive link:

https://docs.google.com/document/d/1dN2ZZ1K5DgKjPwhn321cgDygp49jpx6Wu1zK17EoXSw/edit

**Terminal 1:** 

sathish@sathish-Latitude-3480:~$ cd kafka_2.11-1.1.0/
sathish@sathish-Latitude-3480:~/kafka_2.11-1.1.0$ bin/kafka-server-start.sh config/server.properties


**Terminal 2:** 

sathish@sathish-Latitude-3480:~$ cd kafka_2.11-1.1.0/
sathish@sathish-Latitude-3480:~/kafka_2.11-1.1.0$ bin/zookeeper-server-start.sh config/zookeeper.properties

Steps covered :

1. producer.py streams a sample random telecom data
2. consumer.py receives the streaming data
3. receiver_based_approach.py and direct_approach.py receives the streaming data through spark and then stores the streaming data in hadoop
