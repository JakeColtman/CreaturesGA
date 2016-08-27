from kafka import KafkaConsumer, KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])


def send_to_kafka(item):
    item_type = type(item).__name__
    item["type"] = item_type
    producer.send(json.dumps(item))

def parse_kafka_message(item):
    if item.type == ""