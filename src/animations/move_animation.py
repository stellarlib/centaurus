from stellarlib.animation import Lerp, QuadraticHop
from .charge_rumble import ChargeRumble
from src.settings import PIXEL_SCALE
import math


class MoveAnimation(Lerp):

    MOVE_SPEED = 1.6 * PIXEL_SCALE
    JUMP_SPEED = 1.6 * PIXEL_SCALE
    CHARGE_SPEED = 2.6 * PIXEL_SCALE

    @classmethod
    def move(cls, actor, destination, resolve_func):

        return cls(actor, actor._get_screen_pos(),  #actor.node.sprite_node.position.screen_pos(),
                   destination, actor.hop_height, cls.MOVE_SPEED, resolve_func)

    @classmethod
    def jump(cls, actor, destination, resolve_func):

        return cls(actor, actor._get_screen_pos(),  # actor.node.sprite_node.position.screen_pos(),
                   destination, actor.jump_height, cls.JUMP_SPEED, resolve_func)

    @classmethod
    def charge(cls, actor, start, destination, resolve_func):

        move = cls(actor, start, destination, PIXEL_SCALE, cls.CHARGE_SPEED, resolve_func)
        ChargeRumble(actor, move.duration)
        return move

    def __init__(self, actor, start, destination, height, speed, resolve_func):

        self.speed = speed
        self.duration = self.calculate_move_time(start, destination)
        Lerp.__init__(self, actor.node.sprite_node, start, destination, self.duration)

        self.resolve_func = resolve_func

        # add hop animation
        if height > 0:
            QuadraticHop(actor.node.sprite_node, height * PIXEL_SCALE, self.duration)

    def on_complete(self):
        self.resolve_func()

    def calculate_move_time(self, start, destination):

        sx, sy = start
        dx, dy = destination

        x = abs(dx - sx)
        y = abs(dy - sy)

        dist = math.hypot(x, y)

        return int(round(dist / self.speed))
