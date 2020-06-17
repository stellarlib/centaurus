from .sprite_component import SpriteComponent
from .sprite import Sprite
from src.color import Color


class ShieldSprite(SpriteComponent):

    FLASH_INTERVAL = 4
    FLASH_DUR = 3
    FLASH_REP = 3

    def __init__(self, parent):
        self.parent = parent
        SpriteComponent.__init__(self, 'shield')
        self.destroyed = False

    def hit_shield(self):
        self.flashing = True
        self.flash_tick = 0
        self.reps = ShieldSprite.FLASH_REP

    def on_flash_update(self):
        if self.destroyed:
            self.parent.remove_component(self)

    def mark_destroyed(self):
        self.destroyed = True
