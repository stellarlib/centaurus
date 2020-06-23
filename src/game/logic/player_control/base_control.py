from src.map import Hex


class BaseControl(object):

    def __init__(self, control):

        self.control = control

    @property
    def player(self):
        return self.control.player

    @property
    def logic(self):
        return self.control.logic

    @property
    def map(self):
        return self.control.game.map

    def init_mode(self):
        pass

    def handle_click(self, pos):
        pass

    def is_adj(self, pos):
        a = Hex(*pos)
        b = Hex(*self.player.pos)
        return Hex.hex_distance(a, b) == 1

    def is_passable(self, pos):
        passable = self.map.tile_is_passable(pos)
        return self.is_on_map(pos) and passable

    def is_targetable(self, pos):
        targetable = self.map.tile_is_targetable(pos)
        return self.is_on_map(pos) and targetable

    def is_on_map(self, pos):
        return self.map.on_map(pos)

    def is_exit(self, pos):
        return self.map.tile_is_exit(pos)
