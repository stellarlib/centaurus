from src.animations.charge_animation import ChargeAnimation
from src.map import Tile, Hex
from random import choice


class ChargeBuilder(object):

    def __init__(self, actor, charge_path, start, end, charge_resolve, final_resolve):

        self.actor = actor  # player
        self.logic = actor.game.logic
        self.map = self.logic.game.map
        self.charge_path = charge_path
        self.start = start
        self.end = end
        self.charge_resolve = charge_resolve
        self.final_func = final_resolve

        self._charge_effects = []
        self._obstruction_map = set()

        self.charge_path.insert(0, actor.pos)
        self.calculate()
        self.build()

    def calculate(self):

        self.initialize_obstruction_map()

        for i in range(1, len(self.charge_path)):

            pos = self.charge_path[i]
            foe = self.get_foe(pos)

            if foe:
                trample = self.calculate_foe_trample(foe)
                self._charge_effects.append([i, foe, trample])

    def build(self):

        charge = ChargeAnimation(self.actor, self.start, self.end, self.charge_resolve, self.final_func)
        charge.init(self._charge_effects)

    def calculate_foe_trample(self, foe):

        # get all adj hexes to foe
        # filter out obstructed hexes
        # if any hex is deadly, choose that
        # otherwise choose a random hex
        # add chosen hex to obstruction map
        # if no valid hex, return DIES constant

        adj = [h.to_tuple() for h in Hex.get_hex_neighbours(Hex(*foe.pos))]

        valid_adj = [a for a in adj if self.is_valid_run_pos(a)]

        if not valid_adj:
            return 'trample'

        deadly = [a for a in valid_adj if self.is_deadly(a)]
        if deadly:
            run_pos = choice(deadly)
        else:
            run_pos = choice(valid_adj)

        self._obstruction_map.add(run_pos)
        return run_pos

    def is_valid_run_pos(self, pos):
        return self.map.on_map(pos) and pos not in self._obstruction_map

    def is_deadly(self, pos):
        return self.map.tile_is_deadly(pos)

    def initialize_obstruction_map(self):
        self._obstruction_map.update(self.charge_path)
        self._obstruction_map.update([p for p in self.logic.game.map.all_points() if self.is_obstructed(p)])

    def is_obstructed(self, pos):
        return self.map.tile_is_obstacle(pos) or self.logic.occupied(pos)

    def _get_hex_pos(self, hex):
        return self.actor._get_hex_pos(hex)

    def get_foe(self, pos):
        return self.logic.get_actor_at(pos)
