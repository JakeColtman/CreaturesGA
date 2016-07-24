from Mapping.Terrain import Terrain


class Square:

    def __init__(self, x_pos, y_pos, terrain : Terrain):
        self.x_pos, self.y_pos, self.terrain = x_pos, y_pos, terrain