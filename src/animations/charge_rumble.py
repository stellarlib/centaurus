from stellarlib import animation
from src.settings import PIXEL_SCALE


class ChargeRumble(animation.HitRumble):

    def __init__(self, actor, duration):

        animation.HitRumble.__init__(self, actor.node.sprite, duration, 4, PIXEL_SCALE)
        self.x_shake = 0
        self.y_shake = PIXEL_SCALE
