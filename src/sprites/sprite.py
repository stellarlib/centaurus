import os
from src.settings import PIXEL_SCALE
from src.color import Color
from stellarlib import Surface


class Sprite(object):

    sprite_path = os.path.join('assets', 'sprites')
    colorkey = Color.SPRITE_COLORKEY

    def __init__(self, sprite):
        self._surface = Surface(self.get_file_path(sprite), scale=PIXEL_SCALE, colorkey=Color.SPRITE_COLORKEY)
        self._surface.center_offset()

    def draw(self, target, pos=(0, 0)):
        self._surface.draw(target, pos=pos)

    @staticmethod
    def get_file_path(sprite):
        filename = ''.join((sprite, '.png'))
        return os.path.join(Sprite.sprite_path, filename)

    def replace_color(self, old, new):

        self._surface.replace_color(old, new)

    def mask(self, mask_color):

        self._surface.create_mask(mask_color, Color.SPRITE_COLORKEY)
