

class TravelComponent(object):

    def __init__(self, player):

        self.player = player

    @property
    def game(self):
        return self.player.game

    def travel_to_next_level(self, exit_pos):

        old_map = self.game.map
        self.leave_map()
        # get new map
        new_map = self.game.generate_next_level()
        # get position on new map
        new_pos = self.get_new_start_pos(old_map, new_map, exit_pos)
        self.start_on_new_map(new_map, new_pos)

    def leave_map(self):

        self.game.logic.leave_map()

    def start_on_new_map(self, new_map, new_pos):

        self.player.fully_restore()
        self.game.load_new_level(new_map, new_pos, self.player)

    def get_new_start_pos(self, old_map, new_map, exit_pos):

        exit_edge = old_map.edges[old_map.coord_to_edge[exit_pos]]
        entrance_edge_id, i = exit_edge.get_travel_code(exit_pos)
        return new_map.edges[entrance_edge_id][i]
