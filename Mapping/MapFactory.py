from Square import Square
from Terrain import create_terrain_distribution
from random import choice
from typing import Iterable

from map_pb2 import Cell, Terrain, Row, Map, RIVER, SEA
import redis

class MapRepository:  

    def __init__(self):
        self.conn = redis.StrictRedis(host = 'localhost', port=6379)    

    def store_new_map(self, mappy):
        mappy.id = self.conn.incr("id")
        string_map = mappy.SerializeToString()
        self.conn.set("mappy:{0}".format(mappy.id), string_map)
        return mappy.id

    def get_map(self, map_id):
        mappy = Map()
        contents = self.conn.get("mappy:{0}".format(map_id))
        print(contents)
        print(type(contents))
        mappy.ParseFromString(contents)
        print(mappy)
        return mappy

    def create_random_map(self, size):
        mappy = Map()
        for x in range(size):
            row = Row()
            for y in range(size):
                cell = Cell()
                cell.x_pos = x
                cell.y_pos = y
                cell.terrain = self.choose_random_terrain()
                row.cells.extend([cell])
            mappy.rows.extend([row])
        return self.store_new_map(mappy)

    def choose_random_terrain(self):
        return choice(list(Terrain.values()))

    def create_river_map(self):
        mappy = Map()
        for x in range(10):
            row = Row()
            for y in range(10):
                if x < 2 and y < 2:
                    cell = Cell()
                    cell.x_pos = x
                    cell.y_pos = y
                    cell.terrain = RIVER
                    row.cells.extend([cell])
                else:
                    cell = Cell()
                    cell.x_pos = x
                    cell.y_pos = y
                    cell.terrain = SEA
                    row.cells.extend([cell])
            mappy.rows.extend([row])
        return self.store_new_map(mappy)