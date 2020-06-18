from stellarlib.animation import Lerp


class AttackAnimation(Lerp):

    ATTACK_SPEED = 16

    def __init__(self, actor, foe, resolve_func):

        Lerp.__init__(self, actor.node.sprite_node, actor._get_screen_pos(), foe._get_screen_pos(), AttackAnimation.ATTACK_SPEED)
        self.resolve_func = resolve_func
        self.flip_point = int(self.duration / 2)

    def on_update(self):
        if self.tick == self.flip_point:
            self.step_vector.mult(-1.0)
            self.resolve_func()
