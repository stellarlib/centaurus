from src.map import Tile, Hex


class BaseControl(object):

    def __init__(self, control):

        self.control = control

    @property
    def player(self):
        return self.control.player

    @property
    def logic(self):
        return self.control.logic

    def init_mode(self):
        pass

    def handle_click(self, pos):
        pass

    def is_adj(self, pos):
        a = Hex(*pos)
        b = Hex(*self.player.pos)
        return Hex.hex_distance(a, b) == 1

    def is_passable(self, pos):
        tile = self.control.game.map.get_tile(pos)
        passable = Tile.is_passable(tile)
        return self.is_on_map(pos) and passable

    def is_targetable(self, pos):
        tile = self.control.game.map.get_tile(pos)
        targetable = Tile.is_targetable(tile)
        return self.is_on_map(pos) and targetable

    def is_on_map(self, pos):
        return self.control.game.map.on_map(pos)
