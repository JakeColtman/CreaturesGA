from Square import Square
from Terrain import create_terrain_distribution
from random import choice
from typing import Iterable
from Mapping.MapFactory import MapFactory
from Mapping.Map import Map
from Mapping.move_pb2 import Movement
import redis
from kafka import KafkaProducer

class MapRepository:  

    def __init__(self, conn = redis.StrictRedis(host = 'localhost', port=6379), factory = MapFactory()):
        self.conn = conn
        self.factory = factory
        self.cache = {}
        self.kafka = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

    def new_map(self):
        map = self.factory.create_random_map_data(10)
        map_id = self.conn.incr("map:id")
        self.conn.set("map:{0}".format(map_id), map.SerializeToString())
        return map_id

    def get_map(self, map_id):
        if map_id in self.cache:
            return self.cache[map_id]

        mappy = Map()
        contents = self.conn.get("mappy:{0}".format(map_id))
        print(contents)
        print(type(contents))
        mappy.ParseFromString(contents)
        print(mappy)
        return mappy

    def register_move(self, movemet: Movement) -> True:
        producer.send("movement", movement)