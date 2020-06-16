from .soldier import Soldier
from src.sprites.shield_sprite import ShieldSprite
from src.animations.hit_rumble import HitRumble


class Hoplite(Soldier):

    def __init__(self, game, pos, hp=1):
        Soldier.__init__(self, game, pos, hp)
        self.shield = 2
        self.shield_component = None

    def hit(self, n):

        if self.shield > 0:
            self.shield -= n
            self.shield_component.hit_shield()
            HitRumble(self.node.sprite)
            if self.shield <= 0:
                self.shield_component.mark_destroyed()
        else:
            self.on_hit(n)

    def init(self, parent):
        self.create_node(parent)
        self.create_shield_component()

    def create_shield_component(self):

        self.shield_component = ShieldSprite(self.node.sprite)
        self.node.sprite.add_component(self.shield_component)

    def will_die(self, n):
        return self.shield == 0
