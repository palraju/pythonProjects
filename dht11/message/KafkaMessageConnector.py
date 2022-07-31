import string
import json
from kafka import KafkaConsumer, KafkaProducer
from dht11.model.TemparetureHumiditySensor import TemparetureHumiditySensor


class KafkaConnector:

    @staticmethod
    def consumemessage(topicname: string, topicgroup: string):
        consumer = KafkaConsumer(topicname, group_id=topicgroup)
        for msg in consumer:
            print(msg)

    @staticmethod
    def producemessage(topicname: str, value: str):
        producer = KafkaProducer(bootstrap_servers='192.168.1.4:9092')
        ack = producer.send(topicname, bytes(value, 'utf-8'))
        metadata = ack.get()
        print("Metadata" + json.dumps(metadata))


def send(sensorobject: TemparetureHumiditySensor):
    print(" Sending Kafka Message: " + sensorobject.toJson())
    KafkaConnector.producemessage('temparetureSensorTopic', sensorobject.toJson())

# KafkaConnector.producemessage('dht11', 'Hello World !!!')
