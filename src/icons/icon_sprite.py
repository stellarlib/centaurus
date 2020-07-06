from src.sprites import Sprite
import os


class IconSprite(Sprite):

    sprite_path = os.path.join('assets', 'icons')

    def __init__(self, icon):

        Sprite.__init__(self, icon)
