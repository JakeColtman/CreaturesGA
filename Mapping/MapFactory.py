from Square import Square
from Terrain import create_terrain_distribution
from random import choice
from typing import Iterable

from map_pb2 import Cell, Terrain, Row, Map

class MapFactory:        

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
        return mappy

    def choose_random_terrain(self):
        return choice(list(Terrain.values()))

    def create_river_map(self):
        grid = []
        for x in range(10):
            row = []
            for y in range(10):
                if x < 2 and y < 2:
                    row.append(Square(x, y, Terrain.river))
                else:
                    row.append(Square(x, y, Terrain.sea))
            grid.append(row)
        return Map(grid)
