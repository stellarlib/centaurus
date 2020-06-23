from random import randint
from src.map.hex_map_properties import EdgeID


class Tile(object):

    n = 15

    GRASS, WOODS, WATER, ROCKS, SAND, CLAY, ROAD, WALL, EXIT,\
        EXIT0, EXIT1, EXIT2, EXIT3, EXIT4, EXIT5 = range(n)

    OPEN = {GRASS, ROAD}
    IMPASSABLE = {WALL, ROCKS, WATER}
    OBSTACLE = {WALL, ROCKS}
    SLOWS_CHARGE = {WOODS, WATER, SAND, CLAY}
    DEADLY = {WATER}
    SHELTERED = {WOODS, WALL, ROCKS, WATER}

    EXIT_TILES = {EXIT, EXIT0, EXIT1, EXIT2, EXIT3, EXIT4, EXIT5}
    IMPASSABLE.update(EXIT_TILES)
    OBSTACLE.update(EXIT_TILES)
    SHELTERED.update(EXIT_TILES)

    EDGE_ID_TO_EXIT = {
        EdgeID.Ae: EXIT0,
        EdgeID.Be: EXIT1,
        EdgeID.Ce: EXIT2,
        EdgeID.De: EXIT3,
        EdgeID.Ee: EXIT4,
        EdgeID.Fe: EXIT5,
    }

    @classmethod
    def random_tile(cls):
        return randint(0, cls.n-1)

    @classmethod
    def is_open(cls, t):
        return t not in cls.OPEN

    @classmethod
    def is_passable(cls, t):
        return t not in cls.IMPASSABLE

    @classmethod
    def is_targetable(cls, t):
        return t not in cls.SHELTERED

    @classmethod
    def is_obstacle(cls, t):
        return t in cls.OBSTACLE

    @classmethod
    def is_slowing(cls, t):
        return t in cls.SLOWS_CHARGE

    @classmethod
    def is_deadly(cls, t):
        return t in cls.DEADLY
