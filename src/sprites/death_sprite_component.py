from .sprite_component import SpriteComponent


class DeathSpriteComponent(SpriteComponent):

    FLASH_INTERVAL = 4
    FLASH_DUR = 3
    FLASH_REP = 5

    DEATH_FADE_DUR = 40

    def __init__(self, sprite_name):
        SpriteComponent.__init__(self, sprite_name)
        self.tick = 0
        self.alpha = 255
        self.flashing = True
        self.fade_complete = False

    def on_update(self):

        self.fade()

        if self.tick >= self.DEATH_FADE_DUR:
            self.fade_complete = True
            self.node.end_death_effect()

        self.tick += 1

    def fade(self):

        self.alpha = self.set_alpha()
        for sprite_pair in self.sprites.values():
            for sprite in sprite_pair.values():
                sprite.set_alpha(self.alpha)

    def set_alpha(self):

        return 255 - int((self.tick / self.DEATH_FADE_DUR) * 255)
