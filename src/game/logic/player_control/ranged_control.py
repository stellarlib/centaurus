from .base_control import BaseControl
from src.map import Hex


class RangedControl(BaseControl):

    def __init__(self, control):

        BaseControl.__init__(self, control)
        self._targets = []

    def init_mode(self):

        self._targets = []
        self._targets = [p for p in self.control.game.map.all_points() if self.is_valid_shot(p)]

    def is_valid_shot(self, pos):

        return self.is_in_range(pos) and self.is_targetable(pos) and self.logic.foe_occupied(pos)

    def is_in_range(self, point):

        a = Hex(*point)
        b = Hex(*self.player.pos)

        dist = Hex.hex_distance(a, b)
        return self.player.min_range <= dist <= self.player.max_range

    def handle_click(self, pos):

        if pos in self._targets:
            self.control.player_ranged_attacks(pos)
