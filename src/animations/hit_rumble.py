from stellarlib import animation
from src.settings import RUMBLE_MAG, RUMBLE_DURATION, RUMBLE_FREQUENCY


class HitRumble(animation.HitRumble):

    def __init__(self, node, duration=RUMBLE_DURATION):

        animation.HitRumble.__init__(self, node, duration, RUMBLE_FREQUENCY, RUMBLE_MAG)
