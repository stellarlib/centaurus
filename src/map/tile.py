from random import randint


class Tile(object):

    n = 8

    GRASS, WOODS, WATER, ROCKS, SAND, CLAY, ROAD, WALL = range(n)

    OPEN = {GRASS, ROAD}
    IMPASSABLE = {WALL, ROCKS, WATER}
    OBSTACLE = {WALL, ROCKS}
    SLOWS_CHARGE = {WOODS, WATER, SAND, CLAY}
    DEADLY = {WATER}
    SHELTERED = {WOODS, WALL, ROCKS, WATER}

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
