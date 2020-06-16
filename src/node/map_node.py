from src.map.map_image import MapImage
from stellarlib.scene_node import SceneNode


class MapNode(SceneNode):

    def __init__(self, parent, game):

        SceneNode.__init__(self, parent)
        self.image = MapImage(game)
        self.add_component(self.image)

    def init_map_image(self):
        self.image.init_map_image()
