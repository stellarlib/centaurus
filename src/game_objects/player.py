from .game_object import GameObject
from src.node import SpriteNode, GameObjectNode, ProjectileNode
from src.sprites import SpriteComponent
from stellarlib.scene_node import SceneNode
from .player_overlay import PlayerOverlay
from src.settings import PIXEL_SCALE
from src.animations.move_animation import MoveAnimation
from src.game.logic.player_control.charge_builder import ChargeBuilder


class Player(GameObject):

    ACTIONS = 3
    overlay_pos = (PIXEL_SCALE * 15, PIXEL_SCALE * 15)
    jump_height = PIXEL_SCALE * 7
    hop_height = PIXEL_SCALE * 2

    def __init__(self, game, pos):

        GameObject.__init__(self, game, 'centaur', pos)

        self.actions = Player.ACTIONS
        self.max_actions = Player.ACTIONS

        # player jump stats
        self.min_jump = 2
        self.max_jump = 2
        self.jump_damage = 1

        # player ranged stats
        self.min_range = 2
        self.max_range = 3
        self.ammo = 0

        # charging
        self.charge_damage = 0

        self.player_overlay = PlayerOverlay(self)

    def create_node(self, parent):
        self.node = GameObjectNode(parent, self._get_screen_pos(), self.game)
        self.node.load_sprite(SpriteNode(self.node, SpriteComponent('centaur')))
        self.create_icon_overlay()

    def create_icon_overlay(self):

        overlay = SceneNode(self.game.overlay, Player.overlay_pos)
        overlay.add_component(self.player_overlay)

    def spend_actions(self, x):
        self.actions -= x
        self.player_overlay.update_icons()

    def restore(self, x):
        self.actions += x
        self.actions = min((self.max_actions, self.actions))
        self.player_overlay.update_icons()

    def fully_restore(self):
        self.actions = self.max_actions
        self.player_overlay.update_icons()

    def die(self):
        self.dead = True
        self.game.logic.kill_actor(self)
        print('game over - player died')
        self.on_death()

    def start_move(self, pos, resolve_func):

        def move_resolve():
            self.move(pos)
            resolve_func()

        MoveAnimation.move(self, self._get_hex_pos(pos), move_resolve)

    def start_jump(self, pos, resolve_func):

        def jump_resolve():
            self.move(pos)
            resolve_func()

        MoveAnimation.jump(self, self._get_hex_pos(pos), jump_resolve)

    def start_jump_attack(self, pos, resolve_func):

        def jump_resolve():
            self.move(pos)
            resolve_func()

        MoveAnimation.jump(self, self._get_hex_pos(pos), jump_resolve)

    def start_ranged_attack(self, target_pos, resolve_func):

        target = self.game.logic.get_actor_at(target_pos)

        def on_hit():
            self.range_attack(target)
            resolve_func()

        ProjectileNode.javelin(self, self._get_hex_pos(target_pos), on_hit)

    def start_charge(self, charge_path, final_resolve_func):

        def charge_resolve():
            self.move(charge_path[-1])

        ChargeBuilder(self, charge_path, self.pos, charge_path[-1], charge_resolve, final_resolve_func)
