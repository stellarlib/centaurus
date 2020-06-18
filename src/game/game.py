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


# transitions between different game scenes
from stellarlib.scene.scene_transition import ExitTransition


class Game(Scene):

    def __init__(self, app):

        Scene.__init__(self, app)

        self.hex_layout = None
        self.map = HexMap()
        self.map_image = None
        self.game_objects = None
        self.overlay = None

        self.logic = Logic(self)

        self._initialize()

    def populate_scene_tree(self):

        self.map_image = MapNode(self.scene_tree, self)
        self.game_objects = OrderedDrawNode(self.map_image)
        self.overlay = SceneNode(self.map_image)

    def on_start(self):

        self.set_input()
        init_tiles()
        self.hex_layout = init_hex_layout()
        self.init_map()
        self.logic.init()

    def set_input(self):

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

    def init_map(self):

        # TEMP - TODO - map generator
        from random import randint
        for coord in make_hex(5):

            t = Tile.GRASS
            if randint(0, 2) < 2:
                t = Tile.GRASS
            elif randint(0, 5) == 0:
                t = Tile.WATER

            self.map.add_tile(coord, t)

        self.map_image.init_map_image()

    def _get_screen_dim(self):
        return SCREEN_W, SCREEN_H

    def on_update(self):
        self.logic.update()

    def get_transition(self):

        return ExitTransition()
