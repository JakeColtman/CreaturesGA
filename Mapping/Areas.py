from Mapping.Map import Map
from Mapping.Square import Square
from typing import List, Callable
from Mapping.Map import manhatten_distance
import itertools
from Mapping.Terrain import create_terrain_distribution

Region = List[Square]
RegionMapper = Callable[[Map], List[Region]]

def flood_fill(world_map: Map) -> List[Region]:

    def point_in_region(region:Region, square:Square) -> bool:
        if not square.terrain == region[0].terrain:
            return False
        else:
            min_distance = min([manhatten_distance(region_square, square) for region_square in region])
            return min_distance == 1

    regions = []

    for row in world_map.grid:
        for col in row:
            for region in regions:
                if point_in_region(region, col):
                    region.append(col)
                    break
            else:
                regions.append([col])

    return regions

def based_on_terrain_dist(world_map: Map):
    distance = 2
    distributions = []
    for row in world_map.grid:
        dist_row = []
        for sq in row:
            dist_row.append(create_terrain_distribution(world_map.get_area_around_coordinate(sq.x_pos, sq.y_pos, distance)))
        distributions.append(dist_row)

    return distributions




