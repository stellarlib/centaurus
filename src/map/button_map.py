

class ButtonMap(object):

    def __init__(self):

        self._buttons = {}
        self._map = {}
        self._groups = {}

    def add_button(self, button, group_id):
        assert self._map.get(button.map_pos) is None
        assert button not in self._buttons.values()
        self._buttons[button.button_id] = button
        self._map[button.map_pos] = button
        self._add_to_group(button, group_id)
        button.group_id = group_id

    def _add_to_group(self, button, group_id):

        if group_id in self._groups:
            self._groups[group_id].append(button)
        else:
            self._groups[group_id] = [button]

    def get_button(self, coord):
        return self._map[coord]

    def get_button_by_id(self, button_id):
        return self._buttons[button_id]

    def get_button_group(self, group_id):
        return self._groups[group_id]

    def is_button(self, coord):
        return coord in self._map

    def press_button(self, coord):

        button = self.get_button(coord)
        group = self.get_button_group(button.group_id)
        others = [b for b in group if b is not button]
        if len(others) > 0:
            for b in others:
                b.button_up()

        button.toggle()
        button.press()
