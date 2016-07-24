from Mapping.Map import MapFactory
from Mapping.Areas import flood_fill, based_on_terrain_dist
world = MapFactory().create_random_map(8)
# regions = flood_fill(world)
# for r in regions:
#     print("New region")
#     for sq in r:
#         print(sq.terrain)
#         print(sq.x_pos, sq.y_pos)
print(based_on_terrain_dist(world)[0][0].normalized_weights())