import os
from src.color import Color
from src.settings import PIXEL_SCALE
from stellarlib import Surface


class TileImage(Surface):

    tile_path = os.path.join('assets', 'hex')

    def __init__(self, tile):

        Surface.__init__(self, self.get_file_path(tile), scale=PIXEL_SCALE, colorkey=Color.PURE_WHITE)
        self.center_offset()

    @staticmethod
    def get_file_path(tile):
        filename = ''.join((tile, '.png'))
        return os.path.join(TileImage.tile_path, filename)
