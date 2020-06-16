from .sprite import Sprite


class SpriteComponent(object):

    ANI_RATE = 15
    A = 0
    B = 1

    def __init__(self, sprite_name):
        self.node = None
        self.sprites = self._load_sprites(sprite_name)
        self.tick = 0
        self.frame = SpriteComponent.A

    @property
    def surface(self):
        return self.sprites[self.frame]

    def draw(self, target):
        self.surface.draw(target)

    def update(self):
        self.tick += 1
        if self.tick >= SpriteComponent.ANI_RATE:
            self.flip_animation()
            self.tick = 0

    def flip_animation(self):

        if self.frame == SpriteComponent.A:
            self.frame = SpriteComponent.B
        else:
            self.frame = SpriteComponent.A

    def _load_sprites(self, name):

        sprites = {
            SpriteComponent.A: Sprite('_'.join((name, 'a'))),
            SpriteComponent.B: Sprite('_'.join((name, 'b')))
        }

        return sprites
