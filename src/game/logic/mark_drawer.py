from stellarlib.utilities.hex_tools import hex_to_pixel, Hex
from src.icons import IconSprite
from src.color import Color


class MarkDrawer(object):

    FLASH_RATE = 6
    A = 0
    B = 1

    def __init__(self, logic):
        self.logic = logic
        self._marks = []
        self.tick = 0
        self.state = MarkDrawer.A

        self.icons = self.init_icons()

    def init_icons(self):

        icons = {
            MarkDrawer.A: IconSprite('target'),
            MarkDrawer.B: IconSprite('target')
        }

        icons[MarkDrawer.B].replace_color(Color.RED, Color.WHITE)

        return icons

    def init(self):
        self.logic.game.overlay.add_component(self)

    @property ###
    def mark_map(self):
        return self.logic.ai_control.unit_control.mark_map

    def update(self):

        self.tick += 1
        if self.tick == MarkDrawer.FLASH_RATE:
            self.tick = 0
            self.flash()

    def flash(self):

        if self.state == MarkDrawer.A:
            self.state = MarkDrawer.B
        else:
            self.state = MarkDrawer.A

    def update_marks(self):

        del self._marks[:]
        self._marks.extend(self.mark_map._map)

    def draw(self, surface):

        [self.draw_mark(surface, pos) for pos in self._marks]

    def draw_mark(self, surface, pos):

        icon = self.icons[self.state]
        icon.draw(surface, hex_to_pixel(self.logic.game.hex_layout, Hex(*pos)))
