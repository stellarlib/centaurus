from .sprite import Sprite
import os


class ButtonSprite(Sprite):

    sprite_path = os.path.join('assets', 'icons')

    def __init__(self, button):

        Sprite.__init__(self, button)
