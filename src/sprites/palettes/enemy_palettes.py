from stellarlib.surface.palette import Palette
from src.color import Color


basic_soldier_palette = Palette()
basic_soldier_palette.add_named_item('armor', Color.ORANGE)
basic_soldier_palette.add_named_item('chest', Color.BROWN)
basic_soldier_palette.add_named_item('chest_dark', Color.DARK_BROWN)
basic_soldier_palette.add_named_item('cloak', Color.DARK_GREEN)
basic_soldier_palette.add_named_item('skin', Color.PEACH)
basic_soldier_palette.add_named_item('back_ground', Color.SPRITE_COLORKEY)

mid_soldier_palette = Palette()
mid_soldier_palette.add_named_item('armor', Color.ORANGE)
mid_soldier_palette.add_named_item('chest', Color.BROWN)
mid_soldier_palette.add_named_item('chest_dark', Color.DARK_BROWN)
mid_soldier_palette.add_named_item('cloak', Color.RED)
mid_soldier_palette.add_named_item('skin', Color.PEACH)
mid_soldier_palette.add_named_item('back_ground', Color.SPRITE_COLORKEY)

elite_soldier_palette = Palette()
elite_soldier_palette.add_named_item('armor', Color.ORANGE)
elite_soldier_palette.add_named_item('chest', Color.BLACK)
elite_soldier_palette.add_named_item('cloak', Color.DARK_BLUE)
elite_soldier_palette.add_named_item('skin', Color.PEACH)
elite_soldier_palette.add_named_item('back_ground', Color.SPRITE_COLORKEY)
