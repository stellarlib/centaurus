from .enemy import Enemy
from src.game.logic.ai_control.unit_ai import RangedAI
from src.node import ProjectileNode

# from src.sprites.palettes import *


class Archer(Enemy):

    def __init__(self, game, pos, hp=1):

        Enemy.__init__(self, game, 'archer', pos, hp)

    def on_node_creation(self):
        # self.node.sprite_node.sprite_component.palette_swap(basic_soldier_palette, elite_soldier_palette)
        pass

    def _load_ai(self):
        return RangedAI(self)

    def on_death(self):
        # if still has a mark down on board, clear it
        self.trigger_death_effect()

    def on_removal(self):
        if self.ai.mark:
            self.ai.hard_clear_mark()

    def start_ai_ranged_attack(self, resolve_func):

        mark = self.ai.mark
        self.ai.clear_mark()

        self.shoot(mark, resolve_func)

    def shoot(self, target_pos, resolve_func):

        target = self.game.logic.get_actor_at(target_pos)

        def on_hit():

            resolve_func()
            if target:
                self.range_attack(target)

        ProjectileNode.arrow(self, self._get_hex_pos(target_pos), on_hit)
