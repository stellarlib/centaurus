from stellarlib.input import EventListener


class KeyPressFunction(EventListener):

    def __init__(self, key, function, scene):

        EventListener.__init__(self, key)
        self.function = function
        self.scene = scene

    def on_press(self):
        self.function()
