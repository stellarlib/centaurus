from .ai import AI
from .behaviours import *
from src.map import Hex, Tile


class RangedAI(AI):

    def __init__(self, owner):
        AI.__init__(self, owner)
        self.mark = None
        self._range = 4

    def _get_behaviour(self):

        if self.mark:
            return self.owner, RANGE
        elif self.adj_to_player():
            return self.owner, RETREAT
        elif self.player_in_range():
            return self.owner, MARK
        else:
            return self.owner, APPROACH

    def set_mark(self, pos):
        self.mark = pos

    def clear_mark(self):
        self.mark = None

    def get_tiles_in_range(self):

        player = Hex(*self.owner.pos)

        def in_range(coord):
            c = Hex(*coord)
            return Hex.hex_distance(player, c) <= self._range

        coords = self.owner.game.map.all_except(Tile.WOODS)

        return filter(in_range, coords)

    def hard_clear_mark(self):
        self.owner.game.logic.ai_control.unit_control.clear_mark(self.owner)
        self.clear_mark()
