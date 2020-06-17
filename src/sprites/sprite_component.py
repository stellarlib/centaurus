from .sprite import Sprite
from src.color import Color


class SpriteComponent(object):

    ANI_RATE = 15
    A = 0
    B = 1

    REG = 0
    FLASH = 1

    FLASH_INTERVAL = 4
    FLASH_DUR = 3
    FLASH_REP = 4

    def __init__(self, sprite_name):
        self.node = None
        self.sprites = self._load_sprites(sprite_name)
        self.ani_tick = 0
        self.frame = SpriteComponent.A
        self.state = SpriteComponent.REG

        self.flashing = False
        self.flash_tick = 0
        self.reps = self.set_repetitions()

    @classmethod
    def set_repetitions(cls):
        return cls.FLASH_REP

    @property
    def surface(self):
        return self.sprites[self.frame][self.state]

    @classmethod
    def _load_sprites(cls, name):

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

    def draw(self, target):
        self.surface.draw(target)

    def update(self):
        self.ani_tick += 1
        if self.ani_tick >= SpriteComponent.ANI_RATE:
            self.flip_animation()
            self.ani_tick = 0

        if self.flashing:
            self.update_flash()
            self.on_flash_update()

        self.on_update()

    def on_update(self):
        pass

    def on_flash_update(self):
        pass

    def flip_animation(self):

        if self.frame == SpriteComponent.A:
            self.frame = SpriteComponent.B
        else:
            self.frame = SpriteComponent.A

    def update_flash(self):

        self.flash_tick += 1

        if self.flash_tick == self.FLASH_INTERVAL:
            self.state = self.FLASH
            self.reps -= 1
        elif self.flash_tick == self.FLASH_INTERVAL + self.FLASH_DUR:
            self.state = self.REG
            self.flash_tick = 0
            if self.reps == 0:
                self.flashing = False
                self.reps = self.FLASH_REP

