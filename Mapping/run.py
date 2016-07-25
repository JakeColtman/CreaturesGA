from Mapping.Map import MapFactory
from Mapping.Areas import add_core_regions_to_map, modify_regions
world = MapFactory().create_river_map()
world_with_regions = add_core_regions_to_map(world)
world_with_regions.display()
update, world = modify_regions(world_with_regions)
world.display()
while update:
    update, world = modify_regions(world)
    world.display()
