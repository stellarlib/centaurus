from src.sprites import Sprite
import os


class IconSprite(Sprite):

    icon_path = os.path.join('assets', 'icons')

    def __init__(self, icon):

        Sprite.__init__(self, icon)

    @staticmethod
    def get_file_path(icon):
        filename = ''.join((icon, '.png'))
        return os.path.join(IconSprite.icon_path, filename)
