from .tile import Tile
from .hex_map import HexMap
from stellarlib.utilities.hex_tools import *
from src.settings import TILE_SIZE, HEX_ORIGIN
from .shape import make_hex
from .button_map import ButtonMap


def init_hex_layout():

    return Layout(pointy_layout, Point(*TILE_SIZE), Point(*HEX_ORIGIN))
