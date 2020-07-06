from .palettes.ui_palettes import *
from .button_sprite import ButtonSprite


class ButtonSpriteComponent(object):

    OPEN = 0
    PRESSED = 1

    SIMPLE_DELAY = 5

    def __init__(self, button, simple):

        cls = ButtonSpriteComponent

        self.button_sprites = self._load_button_sprites()
        self.icon_sprites = self._load_icon_sprites(button)
        self.state = cls.OPEN

        self.delayed_unpress = simple
        self.tick = 0


    @classmethod
    def _load_button_sprites(cls):

        buttons = {
                        cls.OPEN: ButtonSprite('button'),
                        cls.PRESSED: ButtonSprite('button')
                    }

        buttons[cls.PRESSED].palette_swap(open_button_palette, pressed_button_palette)

        return buttons

    @classmethod
    def _load_icon_sprites(cls, button):

        icons = {
                    cls.OPEN: ButtonSprite(button),
                    cls.PRESSED: ButtonSprite(button)
                }

        icons[cls.PRESSED].palette_swap(open_button_icon_palette, pressed_button_icon_palette)

        return icons

    @property
    def button_surface(self):
        return self.button_sprites[self.state]

    @property
    def icon_surface(self):
        return self.icon_sprites[self.state]

    def draw(self, target):
        self.button_surface.draw(target)
        self.icon_surface.draw(target)

    def update(self):

        if self.delayed_unpress:

            self.tick_delayed_release()

    def button_down(self):
        self.state = ButtonSpriteComponent.PRESSED
        if self.delayed_unpress:
            self.set_delayed_release()

    def button_up(self):
        self.state = ButtonSpriteComponent.OPEN

    def tick_delayed_release(self):

        if self.tick > 0:
            self.tick -= 1

            if self.tick == 0:
                self.button_up()

    def set_delayed_release(self):
        self.tick = ButtonSpriteComponent.SIMPLE_DELAY
