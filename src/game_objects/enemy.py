from .game_object import GameObject
from src.animations.move_animation import MoveAnimation


class Enemy(GameObject):

    def __init__(self, game, name, pos, hp=1):

        GameObject.__init__(self, game, name, pos)
        self.max_hp = hp
        self.hp = hp
        self.ai = self._load_ai()
        self.hop_height = 4

    def _load_ai(self):
        raise NotImplementedError

    def start_ai_attack(self, resolve_func):

        # TODO this inits attack effect and passes in resolve func
        player = self.game.logic.player
        if player.alive:
            self.start_melee_attack(player, resolve_func)
        #     self.melee_attack(player)
        #
        # resolve_func()

    def start_ai_ranged_attack(self, resolve_func):
        raise Exception('only archer enemy should be firing ranged')

    def start_move(self, pos, resolve_func=None):

        def move_resolve():
            if resolve_func is not None:
                resolve_func()
            self.move(pos)

        return MoveAnimation.move(self, self._get_hex_pos(pos), move_resolve)
