from .tile import Tile


class HexMap(object):

    def __init__(self):

        self._map = {}

    def clear(self):
        self._map.clear()

    def get_tile(self, coord):
        return self._map.get(coord)

    def add_tile(self, coord, tile):
        self._map[coord] = tile

    def on_map(self, coord):
        return coord in self._map

    def all_points(self):
        for point in self._map.keys():
            yield point

    def all_of_tile(self, tile):
        return [t for t in self.all_points() if self.get_tile(t) == tile]

    def all_except(self, not_tile):
        return [t for t in self.all_points() if self.get_tile(t) != not_tile]

    def tile_is_obstacle(self, coord):
        return Tile.is_obstacle(self.get_tile(coord))

    def tile_is_passable(self, coord):
        return Tile.is_passable(self.get_tile(coord))

    def tile_is_targetable(self, coord):
        return Tile.is_targetable(self.get_tile(coord))

    def tile_is_deadly(self, coord):
        return Tile.is_deadly(self.get_tile(coord))

    def tile_is_slowing(self, coord):
        return Tile.is_slowing(self.get_tile(coord))

    def get_all_passable(self):
        return [pos for pos in self.all_points() if self.tile_is_passable(pos)]
