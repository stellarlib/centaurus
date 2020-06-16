from .move_animation import MoveAnimation
from .charge_rumble import ChargeRumble
from stellarlib.animation import Animation
from .charge_effects import ChargeEffects
from src.settings import PIXEL_SCALE


class ChargeAnimation(Animation):

    CHARGE_SPEED = MoveAnimation.CHARGE_SPEED

    def __init__(self, actor, start, dest, charge_resolve, final_resolve):

        Animation.__init__(self, actor.node.sprite)
        self.actor = actor
        self.tick = 0
        self.hex_start = start
        self.hex_end = dest

        self.pix_start = actor._get_hex_pos(start)
        self.pix_end = actor._get_hex_pos(dest)

        self.move = MoveAnimation(actor, self.pix_start, self.pix_end, PIXEL_SCALE, self.CHARGE_SPEED, charge_resolve)
        ChargeRumble(actor, self.move.duration)

        # TODO resolve function that releases control can't happen until charge effect are fully resolved
        self.final_resolve = final_resolve
        self.charge_effects = None

    def init(self, charge_effects):
        self.charge_effects = ChargeEffects(self.actor.charge_damage, self, charge_effects, self.final_resolve)

    def on_update(self):

        self.charge_effects.update()
        if not self.move.active and self.charge_effects.completed:
            self.end()

        self.tick += 1

    def on_complete(self):
        self.final_resolve()

    def update(self):
        self.on_update()
