from stellarlib import Vector
from stellarlib.draw import draw_line
from src.color import Color
from src.settings import PIXEL_SCALE


class ArrowComponent(object):

    ARROW_LEN = PIXEL_SCALE * 6

    def __init__(self, node):

        self.node = node
        self.last_pos = Vector()
        self.current_pos = Vector()
        self.tail = None

    def update(self):
        self.last_pos.set(*self.current_pos)
        self.current_pos.set(*self.node.position.draw_position)
        self.update_tail()

    def draw(self, surface):

        if self.tail:
            self.draw_arrow(surface)

    def get_projectile_length(self):
        return self.ARROW_LEN

    def update_tail(self):

        tail = Vector()
        tail.match(self.current_pos)
        tail.sub(self.last_pos)
        if tail.x == 0.0 and tail.y == 0.0:
            self.tail = None
        else:
            self.tail = tail.get_normalized()
            self.tail.mult(self.get_projectile_length())
            self.tail.add(self.current_pos)

    def draw_arrow(self, surface):

        draw_line(surface, Color.PURE_WHITE, self.current_pos.coord, self.tail.coord, PIXEL_SCALE)
