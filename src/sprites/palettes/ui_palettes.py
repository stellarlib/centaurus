from stellarlib.surface.palette import Palette
from src.color import Color


open_button_palette = Palette()
open_button_palette.add_named_item('main', Color.GREY)
open_button_palette.add_named_item('bright', Color.WHITE)
open_button_palette.add_named_item('shadow', Color.INDIGO)

pressed_button_palette = Palette()
pressed_button_palette.add_named_item('main', Color.INDIGO)
pressed_button_palette.add_named_item('bright', Color.GREY)
pressed_button_palette.add_named_item('shadow', Color.WHITE)

open_button_icon_palette = Palette()
open_button_icon_palette.add_named_item('main', Color.INDIGO)

pressed_button_icon_palette = Palette()
pressed_button_icon_palette.add_named_item('main', Color.YELLOW)
