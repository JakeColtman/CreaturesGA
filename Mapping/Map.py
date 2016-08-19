from Mapping.Square import Square
from Mapping.Terrain import Terrain, create_terrain_distribution
from random import choice
from typing import Iterable
import itertools
from time import sleep
from Mapping.move_pb2 import LEFT, RIGHT, UP, DOWN

class Map:
    def __init__(self, conn, slug):
        self.slug = slug
        self.conn = conn
        self.pos_key = "pos:{0}".format(self.slug)

    def move(self, direction):
        conn = self.conn
        if direction == LEFT:
            x, y = conn.decr(self.pos_key + ":x"), conn.get(self.pos_key + ":y")
        elif direction == RIGHT:
            x, y = conn.incr(self.pos_key + ":x"), conn.get(self.pos_key + ":y")
        if direction == DOWN:
            x, y = conn.get(self.pos_key + ":x"), conn.decr(self.pos_key + ":y")
        elif direction == UP:
            x, y = conn.get(self.pos_key + ":x"), conn.incr(self.pos_key + ":y")

        return [x,y]
