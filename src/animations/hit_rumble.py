from stellarlib import animation
from src.settings import RUMBLE_MAG# , RUMBLE_DURATION, RUMBLE_FREQUENCY


class HitRumble(animation.HitRumble):

    def __init__(self, node):

        animation.HitRumble.__init__(self, node, 12, 2, RUMBLE_MAG)
