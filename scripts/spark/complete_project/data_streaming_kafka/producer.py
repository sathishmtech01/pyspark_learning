# producer.py

import time
from kafka import SimpleProducer, KafkaClient
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
import sys
import random
import json
# Assign a topic
topic = 'my-topic'


def data_streaming(config_path):
    """

    :param config_path:
    :return:
    """

    cellsite_id = [config_path["cellsite_id"]["start"]+str(i).zfill(config_path["cellsite_id"]["zfill"])
                   for i in range(config_path["cellsite_id"]["min"],config_path["cellsite_id"]["max"])]

    customer_number = [config_path["customer_number"]["start"]+str(i).zfill(config_path["customer_number"]["zfill"])
                   for i in range(config_path["customer_number"]["min"],config_path["customer_number"]["max"])]

    types = config_path["data"]["types"]


    while True:
        data = random.choice(cellsite_id) + "," + \
               random.choice(customer_number) + "," + \
               random.choice(types) + "," + \
               str(random.randint(10, 1000))


        data = data.encode()
        #data = "Hello world saaaathish\n".encode()
        producer.send_messages(topic, data)
        # To reduce CPU usage create sleep time of 0.2sec
        time.sleep(1)


def send_data(data):


    producer.send_messages(topic, data)
    # To reduce CPU usage create sleep time of 0.2sec
    time.sleep(0.2)

if __name__ == '__main__':

    # Reading the configuration files
    try:
        if (sys.argv[1].lower() == 'develop'):
            config_path = 'config/develop.json'
        elif (sys.argv[1].lower() == 'staging'):
            config_path = 'config/staging.json'
        elif (sys.argv[1].lower() == 'prod'):
            config_path = 'config/prod.json'
        else:
            config_path = 'config/dev.json'
    except:
        config_path = 'config/dev.json'
    # open the config file and make as dictionary
    with open(config_path) as config_data_file:
        config_data = json.load(config_data_file)

    data_streaming(config_data)