from Mapping.Map import Map
from Mapping.Square import Square
from typing import List, Callable
from Mapping.Map import manhatten_distance
import itertools
from Mapping.Terrain import create_terrain_distribution, average_distribution


class Region:
    def __init__(self, world, squares):
        self.squares = squares
        self.world = world

    def get_average_distribution(self):
        distributions = [create_terrain_distribution(self.world.get_area_around_coordinate(sq.x_pos, sq.y_pos, 2))
                              for sq in self.squares]
        return average_distribution(distributions)


RegionMapper = Callable[[Map], List[Region]]


def core_regions(world_map: Map) -> List[Region]:
    def point_in_region(region: Region, square: Square) -> bool:
        if not square.terrain == region.squares[0].terrain:
            return False
        else:
            min_distance = min([manhatten_distance(region_square, square) for region_square in region])
            return min_distance == 1

    regions = []

    for row in world_map.grid:
        for col in row:
            for region in regions:
                if point_in_region(region, col):
                    region.squares.append(col)
                    break
            else:
                regions.append(Region(world_map, [col]))

    return regions
