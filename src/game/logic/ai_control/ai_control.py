from .unit_ai.behaviours import *
from .unit_control import UnitControl


class AIControl(object):

    def __init__(self, logic):

        self.logic = logic
        self.actor_queue = []
        self.locked = False
        self.ready = True
        self.unit_control = UnitControl(self)

    def init_turn(self):
        self.unit_control.init()

    def reset_turn(self):
        self.ready = True
        self.release()
        del self.actor_queue[:]
        self.unit_control.reset()

    def end_turn(self):
        self.logic.end_ai_turn()
        self.reset_turn()

    def run_turn(self):

        if self.locked:
            return

        self.actor_queue = [a for a in self.actor_queue if a[0].alive]

        if self.actor_queue:
            self.run_actor_queue()
        elif self.ready:
            self.generate_actor_queue()
        else:
            self.end_turn()

    def generate_actor_queue(self):

        self.ready = False

        for actor in self.logic.foes():
            self.actor_queue.append(actor.ai.get_behaviour())

        # take out all passing enemies
        self.actor_queue = [a for a in self.actor_queue if a[0] != STAY]

        self._sort_actor_queue()

        if not self.actor_queue:
            self.end_turn()

    def run_actor_queue(self):

        if self.actor_queue[-1][1] in (APPROACH, RETREAT):
            self.run_batch_movement()
        else:
            self.run_behaviour(*self.actor_queue.pop())

    def _sort_actor_queue(self):
        self.actor_queue.sort(key=lambda a: a[1], reverse=True)

    def lock(self):
        self.locked = True

    def release(self):
        self.locked = False

    def run_batch_movement(self):

        self.lock()
        self.unit_control.run_batch_movement(self.actor_queue)
        del self.actor_queue[:]

    def run_behaviour(self, actor, behaviour):

        self.lock()
        self.unit_control.run_behaviour(actor, behaviour)
