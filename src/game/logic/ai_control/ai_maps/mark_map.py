

class MarkMap(object):

    def __init__(self, logic):

        self.logic = logic
        self._map = set()

    def clear(self):
        self._map.clear()
        self.logic.mark_drawer.update_marks()

    def is_marked(self, pos):
        return pos in self._map

    def mark_pos(self, pos):
        self._map.add(pos)
        self.logic.mark_drawer.update_marks()

    def remove_mark(self, pos):
        self._map.remove(pos)
        self.logic.mark_drawer.update_marks()
