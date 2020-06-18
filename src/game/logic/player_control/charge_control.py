from .base_control import BaseControl
from src.map import Hex, Tile


class ChargeControl(BaseControl):

    def __init__(self, control):

        BaseControl.__init__(self, control)
        self._paths = {}
        self._targets = {}

    def init_mode(self):

        self._paths.clear()
        self._targets.clear()

        for d in range(6):
            charge_path = self.find_charge_path(d)

            if len(charge_path) == 0:
                continue
            elif len(charge_path) == 1 and self.is_pointless_charge(charge_path):
                continue
            else:
                self._paths[d] = charge_path

        for d, points in self._paths.items():
            for pos in points:
                self._targets[pos] = d

    def find_charge_path(self, d):

        charging = True
        charge_path = []

        pos = Hex(*self.player.pos)

        while charging:

            next_hex = Hex.hex_neighbour(pos, d)
            next_pos = next_hex.to_tuple()
            if self.is_on_map(next_pos):
                if self.is_obstacle(next_pos):
                    charging = False
                elif self.slows_charge(next_pos):
                    charging = False
                    charge_path.append(next_pos)
                else:
                    charge_path.append(next_pos)
            else:
                charging = False

            pos = next_hex

        return charge_path

    def is_obstacle(self, pos):
        tile = self.control.game.map.get_tile(pos)
        return Tile.is_obstacle(tile)

    def slows_charge(self, pos):
        return self.control.game.map.tile_is_slowing(pos)
        # tile = self.control.game.map.get_tile(pos)
        # return Tile.slows_charge(tile)

    def is_deadly(self, pos):
        tile = self.control.game.map.get_tile(pos)
        return Tile.is_deadly(tile)

    def is_pointless_charge(self, charge_path):
        return self.slows_charge(charge_path[0]) or self.is_deadly(charge_path[0])

    def handle_click(self, pos):

        if pos in self._targets:
            self.control.charge_player(self._paths[self._targets[pos]])


"""
hex effects:
grass - clear
forest - stop
rock - obstacle
water - stop - die

for each direction 1-6
starting from player.pos
-check hex adj in that direction

-if it is obstacle - end line, don't add hex
- if it is stop - end line, add hex - special case for water
- if it is grass - add hex, continue
- if off map, end line, don't add hex

store the 6 lines
if they are len 0 remove
if they are len 1 and the hex is a forest or water, remove it
"""
