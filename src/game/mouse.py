from stellarlib.input import MouseHandler
from src.map import pixel_to_hex


class Mouse(MouseHandler):

    def left_mouse_button_down(self):

        hex_coord = pixel_to_hex(self.scene.hex_layout, self.get_position()).to_tuple()

        if self.scene.map.part_of_map(hex_coord):
            self.scene.logic.player_control.handle_click(hex_coord)
        elif self.scene.buttons.is_button(hex_coord):
            button = self.scene.buttons.get_button(hex_coord)
            button.press()
