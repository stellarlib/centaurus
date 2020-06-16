from .base_control import BaseControl
from src.map import Hex


class JumpControl(BaseControl):

    def __init__(self, control):

        BaseControl.__init__(self, control)
        self._targets = []

    def init_mode(self):

        self._targets = []
        self._targets = [p for p in self.control.game.map.all_points() if self.is_valid_jump(p)]

    def is_valid_jump(self, point):

        return self.is_passable(point) and self.in_jump_range(point) and self.is_valid_attack(point)

    def in_jump_range(self, point):

        a = Hex(*point)
        b = Hex(*self.player.pos)

        dist = Hex.hex_distance(a, b)
        return self.player.min_jump <= dist <= self.player.max_jump

    def is_valid_attack(self, point):

        if self.logic.foe_occupied(point):
            foe = self.logic.get_actor_at(point)
            return foe.will_die(self.player.jump_damage)
        else:
            # TODO is this necessary?
            assert not self.logic.occupied(point)
            return True

    def handle_click(self, pos):

        if pos in self._targets:
            if self.control.logic.occupied(pos):
                self.control.player_jump_attacks(pos)
            else:
                self.control.jump_player(pos)
