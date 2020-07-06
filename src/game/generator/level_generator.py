from src.map import HexMap, Tile, shape
from random import *
from src.map.hex_map_properties import *

from src.game_objects import Archer, Hoplite, Soldier


class LevelGenerator(object):

    MIN_FOES = 4
    MAX_FOES = 35

    MAP_RADIUS = 4

    @classmethod
    def generate_new_map(cls):

        # TEMP - TODO - map generator

        _map = HexMap(cls.MAP_RADIUS)

        # return cls.test_map(_map)
        return cls.random_map(_map)

    @classmethod
    def test_map(cls, _map):

        # for coord in shape.make_vertical_line((0, 0), 5, rev=True):
        #     _map.add_tile(coord, Tile.GRASS)
        #
        # for coord in shape.make_horizontal_line((0, 0), 5):
        #     _map.add_tile(coord, Tile.ROAD)
        # for coord in shape.make_ring((1, 0), 2):
        #     _map.add_tile(coord, Tile.ROAD)

        for coord in shape.make_structure((-2, 1), 3):
            _map.add_tile(coord, Tile.ROAD)

        return _map

    @classmethod
    def random_map(cls, _map):

        for coord in shape.make_hex(cls.MAP_RADIUS):

            if randint(0, 9) < 3:
                t = Tile.WOODS
            else:
                r = randint(0, 99)
                if r < 10:
                    t = Tile.WATER
                elif r < 30:
                    t = Tile.ROCKS
                else:
                    t = Tile.GRASS

            _map.add_tile(coord, t)

        # temp button coord test
        # buttons = [(2, 5), (1, 5), (1, 6), (0, 6), (2,6)]
        # for coord in buttons:
        #     _map.add_tile(coord, Tile.ROAD)

        # add map exit to top row

        # for edge_id in travel_edges
        for id in [EdgeID.Ae, ]:

            edge = Edge(id, cls.MAP_RADIUS)
            _map.add_exit_edge(edge)
            for coord in edge:
                _map.add_tile(coord, Tile.EDGE_ID_TO_EXIT[id])

        return _map

    @classmethod
    def generate_enemies(cls, game, map, threat=0):

        coords = map.get_all_passable()
        shuffle(coords)
        # TODO take that out
        try:
            coords.remove(game.logic.player.pos)
        except:
            print('player spawned on impassible?')

        n = threat + cls.MIN_FOES
        n = min((cls.MAX_FOES, n, len(coords)-5))
        print(n, ' enemies')

        def next_coord():
            return coords.pop()

        def next_class():
            return choice([Soldier, Archer, Hoplite, Archer])

        enemy_list = []
        for i in range(n):
            enemy_list.append(next_class()(game, next_coord()))

        game.logic.load_enemies(enemy_list)

    @classmethod
    def get_start_pos(cls, map):

        coords = map.get_all_passable()

        return choice(coords)
