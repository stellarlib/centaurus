from .tile import Tile
from .hex_map_properties import EdgeID, Edge


class HexMap(object):

    def __init__(self, radius):

        self._map = {}
        self.radius = radius
        self.edges = {}
        self.coord_to_edge = {}

        self.load_edge_dict()

    def clear(self):
        self._map.clear()

    def get_tile(self, coord):
        return self._map.get(coord)

    def add_tile(self, coord, tile):
        self._map[coord] = tile

    def on_map(self, coord):
        return coord in self._map and self.tile_is_not_exit(coord)

    def all_points(self):
        for point in self._map.keys():
            yield point

    def tile_is_not_exit(self, coord):
        return self.get_tile(coord) not in Tile.EXIT_TILES

    def tile_is_exit(self, coord):
        return self.get_tile(coord) in Tile.EXIT_TILES

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

    ############################
    # edge methods #
    ################
    def load_edge_dict(self):
        for edge_id in EdgeID.base_edge_ids:
            self.add_edge(Edge(edge_id, self.radius))

    def add_edge(self, edge):
        self.edges[edge.edge_id] = edge

    def add_exit_edge(self, edge):
        self.add_edge(edge)
        for coord in edge:
            if self.coord_to_edge.get(coord):
                raise Exception('This point is already a part of an exit edge')
            self.coord_to_edge[coord] = edge.edge_id

    def is_exit_edge(self, coord):
        return coord in self.coord_to_edge






