from stellarlib.scene_node import SceneNode


class SpriteNode(SceneNode):

    def __init__(self, parent, sprite):

        SceneNode.__init__(self, parent)
        self.sprite_component = sprite
        self.sprite_component.node = self
        self.add_component(sprite)
