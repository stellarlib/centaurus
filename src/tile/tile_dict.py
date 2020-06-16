from ..map import Tile
from .tile_image import TileImage


_tile_dict = None


def init_tiles():
    global _tile_dict
    _tile_dict = {
        Tile.GRASS: TileImage('grass'),
        Tile.WOODS: TileImage('woods'),
        Tile.CLAY: TileImage('clay'),
        Tile.SAND: TileImage('sand'),
        Tile.WATER: TileImage('water'),
        Tile.ROAD: TileImage('road'),
        Tile.ROCKS: TileImage('rocks'),
        Tile.WALL: TileImage('wall'),
    }


def get_tile_image(tile):

    return _tile_dict[tile]
