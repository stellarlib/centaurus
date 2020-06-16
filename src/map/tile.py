from random import randint


class Tile(object):

    n = 8

    GRASS, WOODS, WATER, ROCKS, SAND, CLAY, ROAD, WALL = range(n)

    IMPASSABLE = {WALL, WATER}
    OBSTACLE = {WALL}
    SLOWS_CHARGE = {WOODS, WATER, ROCKS, SAND, CLAY}
    DEADLY = {WATER}

    @classmethod
    def random_tile(cls):
        return randint(0, cls.n-1)

    @classmethod
    def is_passable(cls, t):
        return t not in cls.IMPASSABLE

    @classmethod
    def is_targetable(cls, t):
        return t != cls.WOODS

    @classmethod
    def is_obstacle(cls, t):
        return t in cls.OBSTACLE

    @classmethod
    def slows_charge(cls, t):
        return t in cls.SLOWS_CHARGE

    @classmethod
    def is_deadly(cls, t):
        return t in cls.DEADLY
