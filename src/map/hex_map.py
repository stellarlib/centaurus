

class HexMap(object):

    def __init__(self):

        self._map = {}

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
