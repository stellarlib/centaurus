from .unit_ai.behaviours import *
from .ai_maps import DijkstraMap, MoveMap, MarkMap
from src.map import Hex
from random import shuffle, choice


class UnitControl(object):

    PROXIMITY_WEIGHT = 10
    IMPASSABLE_WEIGHT = 1023

    def __init__(self, ai_control):
        self.ai_control = ai_control
        self.logic = self.ai_control.logic

        self.mark_map = MarkMap(self.ai_control.logic)
        self.move_map = MoveMap(self.ai_control.logic)
        self.dijkstra_map = DijkstraMap(self.ai_control.logic)

    def init(self):
        # run at start of ai turn
        # calculate dijkstra
        self.dijkstra_map.update()
        self.move_map.init()

    def reset(self):
        self.dijkstra_map.clear()
        self.move_map.clear()

    # ai controls
    def run_batch_movement(self, actor_queue):

        moves = []

        for actor, behaviour in actor_queue:
            moves.append(self.assign_move(actor, behaviour))

        moves = [m for m in moves if m is not None]

        # TODO initiate set of animations, final animation gets callback to release ai
        # called when last move is complete
        for i in range(len(moves)):
            actor, move = moves[i]
            if i == len(moves) -1:
                actor.start_move(move, self.ai_control.release)
            else:
                actor.start_move(move)

    def run_behaviour(self, actor, behaviour):

        if behaviour == ATTACK:
            self.attack(actor)
        elif behaviour == RANGE:
            self.ranged_attack(actor)
        elif behaviour == MARK:
            self.mark(actor)

    # movement rules
    def assign_move(self, actor, behaviour):

        move = None
        if behaviour == APPROACH:
            move = self.get_approach(actor)
        elif behaviour == RETREAT:
            move = self.get_retreat(actor)

        if move is None:
            return None
        else:
            # move actor on move map
            self.move_map.move(actor, move)

        return actor, move

    def get_approach(self, actor):

        adj = self.get_adj(actor)
        return self.best_approach(adj)

    def best_approach(self, adj):
        weighted = {}
        for a in adj:
            value = self.dijkstra_map.get_value(a)
            if value:
                weighted[a] = value

        if weighted:

            best = min(weighted.values())
            moves = [x for x in weighted.keys() if weighted[x] == best]
            return choice(moves)
        else:
            return None

    def get_retreat(self, actor):
        adj = self.get_adj(actor)
        return self.best_retreat(adj)

    def best_retreat(self, adj):
        weighted = {}
        for a in adj:
            value = self.dijkstra_map.get_value(a)
            if value:
                weighted[a] = value

        if weighted:

            best = max(weighted.values())
            moves = [x for x in weighted.keys() if weighted[x] == best]
            return choice(moves)
        else:
            return None

    def get_adj(self, actor):
        a = Hex(*actor.pos)
        return self.move_map.available_moves([h.to_tuple() for h in Hex.get_hex_neighbours(a)])

    # attack logic
    def attack(self, actor):
        actor.start_ai_attack(self.ai_control.release)

    def ranged_attack(self, actor):
        self.clear_mark(actor)
        actor.start_ai_ranged_attack(self.ai_control.release)

    def mark(self, actor):

        mark_pos = self.get_mark_pos(actor)
        if mark_pos:
            actor.ai.set_mark(mark_pos)
            self.mark_map.mark_pos(mark_pos)
        self.ai_control.release()

    def get_mark_pos(self, actor):

        in_range = actor.ai.get_tiles_in_range()

        # can't mark a previously marked tile
        in_range = [coord for coord in in_range if not self.mark_map.is_marked(coord)]
        # in_range = filter(lambda c: not self.mark_map.is_marked(c), in_range)
        # don't shoot at tiles occupied by another monster
        friendly_occupied = {foe.pos for foe in self.logic.foes()}
        # in_range = filter(lambda c: c not in friendly_occupied, in_range)
        in_range = [coord for coord in in_range if coord not in friendly_occupied]

        weighted = self.weigh_mark_options(actor, in_range)

        if not weighted:
            return None

        return self.get_best_mark(weighted)

    def weigh_mark_options(self, actor, in_range):

        actor_pos = Hex(*actor.pos)
        weighted = {}

        for coord in in_range:

            value = self.dijkstra_map.get_value(coord)
            if value is None:
                weighted[coord] = UnitControl.IMPASSABLE_WEIGHT
            else:
                weighted[coord] = value * UnitControl.PROXIMITY_WEIGHT
                weighted[coord] += Hex.hex_distance(actor_pos, Hex(*coord))

        return weighted

    def get_best_mark(self, weighted_marks):

        best = min(weighted_marks.values())
        possible = [k for k in weighted_marks.keys() if weighted_marks[k] == best]

        return choice(possible)

    def clear_mark(self, actor):

        mark = actor.ai.mark
        self.mark_map.remove_mark(mark)
