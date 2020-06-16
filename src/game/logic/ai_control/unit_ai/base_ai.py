from .ai import AI
from .behaviours import *


class BaseAI(AI):

    def __init__(self, owner):
        AI.__init__(self, owner)

    def _get_behaviour(self):

        if self.adj_to_player():
            return self.owner, ATTACK
        else:
            return self.owner, APPROACH
