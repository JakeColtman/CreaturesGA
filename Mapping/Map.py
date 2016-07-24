from Mapping.Square import Square
from Mapping.Terrain import Terrain
from random import choice
from typing import Iterable
import itertools


class Map:
    def __init__(self, grid):
        self.grid = grid

    def get_area_around_coordinate(self, x_pos, y_pos, distance):
        max_coordinate = len(self.grid) - 1
        min_x = max(0, x_pos - distance)
        max_x = min(max_coordinate, x_pos + distance)
        min_y = max(0, y_pos - distance)
        max_y = min(max_coordinate, y_pos + distance)

        x_positions = range(min_x, max_x + 1)
        y_positions = range(min_y, max_y + 1)
        coords = list(itertools.product(x_positions, y_positions))
        return [self.grid[x[0]][x[1]] for x in coords]


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
