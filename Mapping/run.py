from Mapping.Map import MapFactory
from Mapping.Areas import flood_fill
world = MapFactory().create_random_map(5)
regions = flood_fill(world)
for r in regions:
    print("New region")
    for sq in r:
        print(sq.terrain)
        print(sq.x_pos, sq.y_pos)