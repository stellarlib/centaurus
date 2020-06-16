from src.game_objects import Player, Archer, Soldier, Hoplite
from .player_control import PlayerControl
from .ai_control import AIControl
from .mark_drawer import MarkDrawer


class Logic(object):

    def __init__(self, game):

        self.game = game
        self.player_control = PlayerControl(self)
        self.ai_control = AIControl(self)
        self.mark_drawer = MarkDrawer(self)

        self.player = None
        self.actors = []
        self.killed = []

        self._ai_turn = False

    def init(self):

        self.mark_drawer.init()
        self.initialize_player()
        self.add_actor(self.player)

        # TODO this goes in a scenario/map generator
        self.add_actor(Soldier(self.game, (-1, 2)))
        self.add_actor(Archer(self.game, (-3, 0)))
        self.add_actor(Archer(self.game, (0, -2)))
        self.add_actor(Hoplite(self.game, (2, 2)))

        [actor.ai.alert() for actor in filter(lambda a: a != self.player, self.actors)]

    def initialize_player(self):

        self.player = Player(self.game, (0, 0))

    def add_actor(self, actor):

        self.actors.append(actor)
        actor.init(self.game.game_objects)

    def kill_actor(self, actor):

        assert actor not in self.killed
        assert actor in self.actors
        self.killed.append(actor)

    def update(self):

        if self.killed:
            self.clear_killed()

        if self._ai_turn:
            self.ai_control.run_turn()

    def clear_killed(self):

        for actor in self.killed:
            actor.node.orphan()
            self.actors.remove(actor)
        del self.killed[:]

    def get_actor_at(self, pos):

        actor = [actor for actor in self.actors if actor.pos == pos]
        assert len(actor) <= 1
        if actor:
            return actor[0]
        else:
            return None

    def occupied(self, pos):

        return self.get_actor_at(pos) is not None

    def foe_occupied(self, pos):

        actor = self.get_actor_at(pos)
        return actor is not None and actor != self.player

    def foes(self):

        return [actor for actor in self.actors if actor != self.player]

    def start_ai_turn(self):

        self._ai_turn = True
        self.ai_control.init_turn()

    def end_ai_turn(self):

        self._ai_turn = False
        self.player_control.start_player_turn()
