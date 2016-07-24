from Mapping.Square import Square
from Mapping.Square import Terrain
from random import choice
from typing import Iterable


class Map:
    def __init__(self, grid):
        self.grid = grid


def manhatten_distance(first_square: Square, second_square: Square) -> int:
    return abs(first_square.x_pos - second_square.x_pos) + abs(first_square.y_pos - second_square.y_pos)


class MapFactory:
    def create_random_map(self, size):
        grid = []
        for x in range(size):
            row = []
            for y in range(size):
                row.append(Square(x, y, self.choose_random_terrain()))
            grid.append(row)
        return Map(grid)

    def choose_random_terrain(self):
        return choice(list(Terrain))
