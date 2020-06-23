from .shape import *


"""

     A --- B
    /       |
   F         C
    |       / 
     E --- D

"""


class EdgeID(object):
    A, B, C, D, E, F = range(6)
    Ae, Be, Ce, De, Ee, Fe = range(6, 12)

    exit_ids = {Ae, Be, Ce, De, Ee, Fe}
    base_edge_ids = {A, B, C, D, E, F}

    edge_mods = {
        Ae: (1, -1),
        Be: (1, 0),
        Ce: (0, 1),
        De: (-1, 1),
        Ee: (-1, 0),
        Fe: (0, -1),
    }

    travel_map = {
        Ae: D,
        Be: E,
        Ce: F,
        De: A,
        Ee: B,
        Fe: C
    }


class Edge(object):

    unit_points = {
        EdgeID.A: (0, -1),
        EdgeID.B: (1, -1),
        EdgeID.C: (1, 0),
        EdgeID.D: (0, 1),
        EdgeID.E: (-1, 1),
        EdgeID.F: (-1, 0),
    }

    edge_constructors = {
        EdgeID.A: (make_horizontal_line, False),
        EdgeID.B: (make_down_right_line, False),
        EdgeID.C: (make_down_left_line, False),
        EdgeID.D: (make_horizontal_line, True),
        EdgeID.E: (make_down_right_line, True),
        EdgeID.F: (make_down_left_line, True),
    }

    core_edge_id = {
        EdgeID.A: EdgeID.A,
        EdgeID.B: EdgeID.B,
        EdgeID.C: EdgeID.C,
        EdgeID.D: EdgeID.D,
        EdgeID.E: EdgeID.E,
        EdgeID.F: EdgeID.F,
        EdgeID.Ae: EdgeID.A,
        EdgeID.Be: EdgeID.B,
        EdgeID.Ce: EdgeID.C,
        EdgeID.De: EdgeID.D,
        EdgeID.Ee: EdgeID.E,
        EdgeID.Fe: EdgeID.F,
    }

    def __init__(self, edge_id, radius):

        self.edge_id = edge_id
        self.radius = radius
        self.points = self._get_points(radius, self.core_edge_id[edge_id])

    def __getitem__(self, i):
        return self.points[i]

    def __iter__(self):
        return (p for p in self.points)

    @staticmethod
    def add_points(a, b):
        return a[0] + b[0], a[1] + b[1]

    @staticmethod
    def mult_point(a, radius):
        return a[0] * radius, a[1] * radius

    def get(self, i):
        return self.points[i]

    def _get_points(self, radius, core_edge_id):

        start = self.mult_point(self.unit_points[core_edge_id], radius)
        edge_constructor, rev = self.edge_constructors[core_edge_id]

        points = [p for p in edge_constructor(start, radius+1, rev)]

        if self.edge_id in EdgeID.exit_ids:

            mod = EdgeID.edge_mods[self.edge_id]
            points = [self.add_points(p, mod) for p in points]

        return points

    def get_travel_code(self, point):

        """
        returns the EdgeID of the next map where this exit coord should wrap around to
        and the index on that edge that should match up
        """

        assert point in self.points
        assert self.edge_id in EdgeID.exit_ids

        i = self.points.index(point)
        i = -1 - i

        return EdgeID.travel_map[self.edge_id], i
