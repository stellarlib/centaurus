from stellarlib.scene_node import SceneNode
from src.map import pixel_to_hex, Hex, Tile


class GameObjectNode(SceneNode):

    def __init__(self, parent, pos, game):

        SceneNode.__init__(self, parent, pos)
        self.game = game
        self.sprite = None

    def load_sprite(self, sprite_node):

        self.sprite = sprite_node

    def after_render(self, target):

        self.draw_overlapping_trees(target)

    def draw_overlapping_trees(self, surface):

        hex = pixel_to_hex(self.game.hex_layout, self.position.screen_pos())

        bl = Hex.hex_neighbour(hex, 4)
        br = Hex.hex_neighbour(hex, 5)

        for hex in (bl, br):

            if self.game.map.get_tile((hex.x, hex.y)) == Tile.WOODS:
                self.game.map_image.image.draw_overlap_trees(surface, hex)

    def set_pos(self, pos):
        self.position.set_base_position(pos)
