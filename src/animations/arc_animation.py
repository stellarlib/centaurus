from stellarlib.animation import Lerp, QuadraticHop
from src.settings import PIXEL_SCALE
import math


class ArcAnimation(Lerp):

    def __init__(self, actor, projectile_node, destination, height, speed, resolve_func):

        start = actor.node.sprite_node.position.screen_pos()
        duration = self.calculate_move_time(start, destination, speed)
        Lerp.__init__(self, projectile_node, start, destination, duration)
        self.resolve_func = resolve_func

        # add hop
        QuadraticHop(projectile_node, height * PIXEL_SCALE, duration)

    def on_complete(self):
        self.resolve_func()

    def calculate_move_time(self, start, destination, speed):

        sx, sy = start
        dx, dy = destination

        x = abs(dx - sx)
        y = abs(dy - sy)

        dist = math.hypot(x, y)

        return int(round(dist / speed))
