from .enemy import Enemy
from src.game.logic.ai_control.unit_ai import BaseAI


class Soldier(Enemy):

    def __init__(self, game, pos, hp=1):

        Enemy.__init__(self, game, 'soldier', pos, 5)

    def _load_ai(self):
        return BaseAI(self)
