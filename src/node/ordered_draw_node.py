from stellarlib.scene_node import SceneNode


class OrderedDrawNode(SceneNode):

    def __init__(self, parent):

        SceneNode.__init__(self, parent)

    def before_render(self, target):
        self.order_children()

    def order_children(self):
        # sort the ordered child nodes in place so that those higher on the screen
        # are rendered first - sort by y value
        self.children.sort(key=lambda c: c.position.local_pos()[1])
