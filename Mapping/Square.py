from enum import Enum


class Terrain(Enum):
    river = 1
    sea = 2
    plain = 3
    mountain = 4


class Square:

    def __init__(self, x_pos, y_pos, terrain : Terrain):
        self.x_pos, self.y_pos, self.terrain = x_pos, y_pos, terrain