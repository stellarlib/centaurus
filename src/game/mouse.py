from stellarlib.input import MouseHandler
from src.map import pixel_to_hex


class Mouse(MouseHandler):

    def left_mouse_button_down(self):

        hex_coord = pixel_to_hex(self.scene.hex_layout, self.get_position())
        self.scene.logic.player_control.handle_click(hex_coord.to_tuple())
