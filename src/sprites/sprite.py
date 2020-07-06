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

    @classmethod
    def get_file_path(cls, sprite):
        filename = ''.join((sprite, '.png'))
        return os.path.join(cls.sprite_path, filename)

    def replace_color(self, old, new):

        self._surface.replace_color(old, new)

    def palette_swap(self, old_palette, new_palette):
        self._surface.palette_swap(old_palette, new_palette)

    def mask(self, mask_color):

        self._surface.create_mask(mask_color, Color.SPRITE_COLORKEY)

    def set_alpha(self, alpha):

        self._surface.set_alpha(alpha)

