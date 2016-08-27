from kafka import KafkaProducer
import json

import attr
from Mapping.Interface.map import MapFragment
from People.Interface.move import UpdatedPosition, MovementRequest

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])


def send_to_kafka(item):
    item_type = type(item).__name__
    ddict = attr.asdict(item)
    ddict["type"] = item_type
    producer.send(json.dumps(ddict))


def parse_kafka_message(item):
    ttype = item["type"]
    del item["type"]
    if ttype == "UpdatedPosition":
        return UpdatedPosition(**item)
    elif ttype == "MovementRequest":
        return MovementRequest(**item)
    elif ttype == "MapFragment":
        return MapFragment(**item)


if __name__ == "__main__":
    test = attr.asdict(UpdatedPosition(id=1, x_pos=1, y_pos=1))
    test["type"] = "UpdatedPosition"
    print(parse_kafka_message(test))
