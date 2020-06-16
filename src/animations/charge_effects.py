from src.animations.move_animation import MoveAnimation
from src.map import Hex
from src.settings import PIXEL_SCALE


class ChargeEffects(object):

    TRAMPLE = 0
    RUN = 1

    effect_type_mod = {
        TRAMPLE: 0 * PIXEL_SCALE,
        RUN: 0 * PIXEL_SCALE
    }

    def __init__(self, damage, animation, charge_effects, final_resolve):

        self.charge_damage = damage
        self.animation = animation
        self._charge_effects = charge_effects
        self.effect_list = []
        self.final_resolve = final_resolve
        self.hex_move_time = self.calculate_hex_move_time()

        self._blocking_animations = []

        self.compute()

    def calculate_hex_move_time(self):

        a = Hex(*self.animation.hex_start)
        b = Hex(*self.animation.hex_end)
        hex_distance = Hex.hex_distance(a, b)

        return self.animation.move.duration / hex_distance

    @property
    def completed(self):
        # the charge effects are over if all the animations triggered by the
        # charge have resolved
        return True not in [a.active for a in self._blocking_animations]

    def update(self):

        new_effects = [e for e in self.effect_list if e[1] == self.animation.tick]

        if new_effects:
            for effect in new_effects:
                if effect[0] == ChargeEffects.RUN:
                    self.trigger_run_effect(effect)
                elif effect[0] == ChargeEffects.TRAMPLE:
                    self.trigger_trample_effect(effect)

    def compute(self):

        for i, foe, run_pos in self._charge_effects:
            if run_pos == 'trample':
                self.effect_list.append((ChargeEffects.TRAMPLE, self.calc_delay(i, ChargeEffects.TRAMPLE), foe))
            else:
                self.effect_list.append((ChargeEffects.RUN, self.calc_delay(i, ChargeEffects.RUN), foe,run_pos))

    def calc_delay(self, i, effect_type):

        # need to come up with a frame count from when charge started to where this effect should happen
        return int(i * self.hex_move_time - self.hex_move_time/2) + ChargeEffects.effect_type_mod[effect_type]

    def trigger_run_effect(self, effect):

        effect_type, delay, foe, run_pos = effect

        if self.charge_damage > 0:
            foe.hit(self.charge_damage)
            if not foe.alive:
                return

        self._blocking_animations.append(foe.start_move(run_pos))

    def trigger_trample_effect(self, effect):

        print('trampled to death, TODO')
        foe = effect[2]
        foe.die()
