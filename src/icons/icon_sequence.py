from .icon_sprite import IconSprite
from .icons import *


class IconSequence(object):

    icon_sprites = None

    @classmethod
    def init(cls):

        cls.icon_sprites = {ACTION_FULL: IconSprite('action_full'),
                            ACTION_EMPTY: IconSprite('action_empty')}

    def __init__(self, icons, spacing=ICON_SPACING):

        if IconSequence.icon_sprites is None:
            IconSequence.init()

        self.icons = icons
        self.spacing = spacing

    def draw(self, surface):

        for i in range(len(self.icons)):
            self.draw_icon(surface, i)

    def draw_icon(self, surface, i):

        icon = IconSequence.icon_sprites.get(self.icons[i])
        x = i * self.spacing
        icon.draw(surface, pos=(x, 0))
