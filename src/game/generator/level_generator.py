from src.map import HexMap, Tile, shape
from random import *

from src.game_objects import Archer, Hoplite, Soldier


class LevelGenerator(object):

    MIN_FOES = 4
    MAX_FOES = 64

    def __init__(self):
        pass

    @classmethod
    def generate_new_map(cls):

        # TEMP - TODO - map generator

        _map = HexMap()

        for coord in shape.make_hex(4):

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

        return _map

    @classmethod
    def generate_enemies(cls, game, map, threat=0):

        n = threat + cls.MIN_FOES +10

        coords = map.get_all_passable()
        shuffle(coords)
        coords.remove(game.logic.player.pos)

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
