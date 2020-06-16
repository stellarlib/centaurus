from .sprite_component import SpriteComponent
from .sprite import Sprite
from src.color import Color


class ShieldSprite(SpriteComponent):

    REG = 0
    FLASH = 1

    FLASH_DELAY = 4
    FLASH_DUR = 3
    FLASH_REP = 3

    def __init__(self, parent):
        self.parent = parent
        SpriteComponent.__init__(self, 'shield')
        self.state = ShieldSprite.REG
        self.flashing = False
        self.flash_tick = 0
        self.reps = ShieldSprite.FLASH_REP
        self.destroyed = False

    @property
    def surface(self):
        return self.sprites[self.frame][self.state]

    def _load_sprites(self, name):

        cls = ShieldSprite
        sprites = {
            cls.A: {cls.REG: Sprite('_'.join((name, 'a'))),
                    cls.FLASH: Sprite('_'.join((name, 'a'))),
                    },
            cls.B: {cls.REG: Sprite('_'.join((name, 'b'))),
                    cls.FLASH: Sprite('_'.join((name, 'b')))
                    }
        }

        sprites[cls.A][cls.FLASH].mask(Color.RED)
        sprites[cls.B][cls.FLASH].mask(Color.RED)

        return sprites

    def update(self):
        self.tick += 1
        if self.tick >= SpriteComponent.ANI_RATE:
            self.flip_animation()
            self.tick = 0

        if self.flashing:
            self.update_flash()

    def hit_shield(self):
        self.flashing = True
        self.flash_tick = 0
        self.reps = ShieldSprite.FLASH_REP

    def update_flash(self):

        cls = ShieldSprite

        self.flash_tick += 1

        if self.flash_tick == cls.FLASH_DELAY:
            self.state = cls.FLASH
            self.reps -= 1
        elif self.flash_tick == cls.FLASH_DELAY + cls.FLASH_DUR:
            self.state = cls.REG
            self.flash_tick = 0
            if self.reps == 0:
                self.flashing = False
                if self.destroyed:
                    self.parent.remove_component(self)

    def mark_destroyed(self):
        self.destroyed = True
