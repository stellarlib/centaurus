from .behaviours import *
from src.map import Hex


class AI(object):

    def __init__(self, owner):
        self.owner = owner
        self._alert = False
        self._range = 1

    @property
    def player(self):
        return self.owner.game.logic.player

    @property
    def map(self):
        return self.owner.game.map

    @property
    def alerted(self):
        return self._alert

    def alert(self):
        self._alert = True

    def get_behaviour(self):
        if not self.alerted:
            return self.owner, STAY
        return self._get_behaviour()

    def _get_behaviour(self):
        raise NotImplementedError

    def adj_to_player(self):

        player = Hex(*self.player.pos)
        owner = Hex(*self.owner.pos)

        return Hex.hex_distance(player, owner) == 1

    def player_in_range(self):

        player = Hex(*self.player.pos)
        owner = Hex(*self.owner.pos)

        return Hex.hex_distance(player, owner) <= self._range
