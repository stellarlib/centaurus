from stellarlib.utilities.flood_fill import hex_flood
from src.map.tile import Tile


class DijkstraMap(object):

    def __init__(self, logic):

        self.logic = logic
        self._map = {}

    @property
    def map(self):
        return self.logic.game.map

    def clear(self):
        self._map.clear()

    def update(self):
        self.calculate_dijkstra()

    def get_value(self, pos):
        return self._map.get(pos)

    def calculate_dijkstra(self):

        start_edge = {self.logic.player.pos}

        edge = set(start_edge)
        touched_set = set(start_edge)

        value = 0
        dijkstra = {self.logic.player.pos: value}

        while edge:

            value += 1

            edge = hex_flood(edge, self.is_valid_tile, touched_set)
            touched_set.update(edge)

            for e in edge:
                dijkstra[e] = value

        self._map.update(dijkstra)

    def is_valid_tile(self, pos):
        on_map = self.map.on_map(pos)
        passable = self.map.tile_is_passable(pos)
        return on_map and passable
