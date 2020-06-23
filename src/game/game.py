from stellarlib.scene import Scene
from src.map import init_hex_layout, HexMap, make_hex, Tile
from src.tile import init_tiles
from stellarlib.scene_node import SceneNode
from src.node.map_node import MapNode
from src.node import OrderedDrawNode
from .logic import Logic
from .mouse import Mouse
from src.settings import SCREEN_W, SCREEN_H
from src.input import KeyPressFunction
from stellarlib.input.constants import *
from .generator.level_generator import LevelGenerator
from src.game_objects import Player


# transitions between different game scenes
from stellarlib.scene.scene_transition import ExitTransition


class Game(Scene):

    def __init__(self, app):

        Scene.__init__(self, app)

        self.hex_layout = None
        self.map = None
        self.map_image = None
        self.game_objects = None
        self.overlay = None
        self.logic = Logic(self)

        self.threat = 0

        self._initialize()

    def _get_screen_dim(self):
        return SCREEN_W, SCREEN_H

    def on_update(self):
        self.logic.update()

    def get_transition(self):

        return ExitTransition()

    def populate_scene_tree(self):

        self.map_image = MapNode(self.scene_tree, self)
        self.game_objects = OrderedDrawNode(self.map_image)
        self.overlay = SceneNode(self.map_image)

    def on_start(self):

        self.set_input()
        init_tiles()
        self.hex_layout = init_hex_layout()
        self.logic.init()

        self.load_new_level(self.generate_next_level(), (0, 0))

    def initialize_player(self, pos=(0, 0)):
        self.logic.add_player(Player(self, pos))

    def set_input(self):

        # TODO TEMP
        def start_new_level():
            self.logic.leave_map()
            level = self.generate_next_level()
            start_pos = LevelGenerator.get_start_pos(level)
            self.load_new_level(level, start_pos, self.logic.player)

        self.input_handler.add_listener(KeyPressFunction(K_n, start_new_level, self))

        def ranged_mode():
            self.logic.player_control.manual_switch_mode('ranged')

        def jump_mode():
            self.logic.player_control.manual_switch_mode('jump')

        def charge_mode():
            self.logic.player_control.manual_switch_mode('charge')

        # menu button
        self.input_handler.add_listener(KeyPressFunction(K_ESCAPE, self.trigger_exit, self))
        # self.input_handler.add_listener(KeyPressFunction(K_SLASH, self.screen_shot, self))

        # player mode keys
        self.input_handler.add_listener(
            KeyPressFunction(K_SPACE, self.logic.player_control.manual_turn_end, self))
        self.input_handler.add_listener(KeyPressFunction(K_z, ranged_mode, self))
        self.input_handler.add_listener(KeyPressFunction(K_x, jump_mode, self))
        self.input_handler.add_listener(KeyPressFunction(K_c, charge_mode, self))

        self.input_handler.set_mouse_handler(Mouse)

    def init_map(self, map):

        self.map = map
        self.map_image.init_map_image()

    def load_new_level(self, new_map, start_pos, player=None):

        print('testing new level')

        self.init_map(new_map)
        # start_pos = LevelGenerator.get_start_pos(self.map)

        if not player:
            self.initialize_player(start_pos)
        else:
            player.move(start_pos)
        print(start_pos)

        LevelGenerator.generate_enemies(self, self.map, self.threat)

        self.threat += 1

    def generate_next_level(self):
        return LevelGenerator.generate_new_map()
