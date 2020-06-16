from stellarlib.scene_node import SceneNode


class SpriteNode(SceneNode):

    def __init__(self, parent, sprite):

        SceneNode.__init__(self, parent)
        self.sprite = sprite
        self.sprite.node = self
        self.add_component(sprite)
