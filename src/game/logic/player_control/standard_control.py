from .base_control import BaseControl


class StandardControl(BaseControl):

    def __init__(self, control):

        BaseControl.__init__(self, control)

    def handle_click(self, pos):

        if self.is_adj(pos):
            if self.control.logic.occupied(pos):
                self.control.player_attacks(pos)
            elif self.is_passable(pos):
                self.control.move_player(pos)
