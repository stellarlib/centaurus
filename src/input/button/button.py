from src.sprites import ButtonSpriteComponent
from src.node import SpriteNode
from stellarlib.scene_node import SceneNode
from src.map import Hex, hex_to_pixel
from src.animations.hit_rumble import HitRumble


class Button(object):

    def __init__(self, game, button_id, map_pos, function, simple=False):

        self.button_id = button_id
        self.game = game
        self.map_pos = map_pos
        self.function = function

        self.group_id = None
        self.hidden = False
        self.pressed = False
        self.button_sprite = ButtonSpriteComponent(self.button_id, simple)

        self.node = SceneNode(game.overlay, pos=self._get_pixel_pos(self.map_pos))
        self.node.add_component(self.button_sprite)

    def press(self):

        if not self.hidden:
            self.on_press()

    def on_press(self):
        self.function()

    def _get_pixel_pos(self, pos):
        px, py = hex_to_pixel(self.game.hex_layout, Hex(*pos))
        return px, py

    def toggle(self):
        if self.pressed:
            self.button_up()
        else:
            self.button_down()

    def button_down(self):
        self.button_sprite.button_down()
        self.pressed = True

    def button_up(self):
        self.button_sprite.button_up()
        self.pressed = False

    def rumble(self):
        HitRumble(self.node)
