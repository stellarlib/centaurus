from src.settings import PIXEL_SCALE
from .arrow_component import ArrowComponent


class JavelinComponent(ArrowComponent):

    JAVELIN_LEN = PIXEL_SCALE * 10

    def __init__(self, node):

        ArrowComponent.__init__(self, node)

    def get_projectile_length(self):
        return self.JAVELIN_LEN
