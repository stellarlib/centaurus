from src.sprites import SpriteComponent
from src.node import SpriteNode, GameObjectNode
from src.map import hex_to_pixel, Hex
from src.settings import PIXEL_SCALE
from src.animations.hit_rumble import HitRumble
from src.node.death_effect_node import DeathEffectNode
from src.animations.attack_animation import AttackAnimation


class GameObject(object):

    ACTOR_OFFSET = PIXEL_SCALE * 5

    def __init__(self, game, name, pos):

        self.game = game
        self.name = name
        self.pos = pos
        self.node = None

        # stats
        self.hp = 1
        self.max_hp = 1

        self.dead = False

    @property
    def alive(self):
        return not self.dead

    def init(self, parent):
        self.create_node(parent)

    def create_node(self, parent):
        self.node = GameObjectNode(parent, self._get_screen_pos(), self.game)
        self.node.load_sprite(SpriteNode(self.node, SpriteComponent(self.name)))

    def _get_screen_pos(self):
        return self._get_hex_pos(self.pos)

    def _get_hex_pos(self, pos):
        px, py = hex_to_pixel(self.game.hex_layout, Hex(*pos))
        py -= GameObject.ACTOR_OFFSET
        return px, py

    # API
    def place(self, pos):
        self.pos = pos
        self.node.set_pos(self._get_screen_pos())

    def move(self, pos):
        self.place(pos)
        self.trigger_hazard(pos)

    def die(self):
        self.dead = True
        self.game.logic.kill_actor(self)
        self.on_death()

    def hit(self, n):

        self.on_hit(n)

    def on_hit(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.die()
        else:
            self.hit_effect()

    def hit_effect(self):
        self.node.sprite_node.sprite_component.flashing = True
        HitRumble(self.node.sprite_node)

    def melee_attack(self, foe):
        foe.hit(1)

    def range_attack(self, foe):
        foe.hit(2)

    def on_death(self):
        self.trigger_death_effect()

    def trigger_death_effect(self):
        DeathEffectNode(self)

    def will_die(self, n):
        return n >= self.hp

    def start_melee_attack(self, foe, resolve_func):

        def melee_resolve():
            self.melee_attack(foe)
            resolve_func()

        AttackAnimation(self, foe, melee_resolve)

    def trigger_hazard(self, pos):

        if self.game.map.tile_is_deadly(pos):
            self.die()

    def on_removal(self):
        pass