from stellarlib.scene_node import SceneNode
from src.map import pixel_to_hex, Hex, Tile
from src.sprites.death_sprite_component import DeathSpriteComponent
from src.animations.hit_rumble import HitRumble
from src.settings import PIXEL_SCALE


class DeathEffectNode(SceneNode):

    def __init__(self, game_object):

        parent = game_object.game.game_objects  # parent node
        pos = game_object._get_screen_pos()
        SceneNode.__init__(self, parent, pos)
        self.game_object = game_object
        self.game = game_object.game
        self.sprite_component = self.create_death_sprite()
        self.sprite_component.node = self
        self.add_component(self.sprite_component)

        # apply a rumble effect to sprite
        rumble = HitRumble(self, duration=DeathSpriteComponent.DEATH_FADE_DUR)
        rumble.x_shake = PIXEL_SCALE
        rumble.y_shake = 0

        # if sprite_component.fade_complete - end node

    def create_death_sprite(self):

        return DeathSpriteComponent(self.game_object.name)

    def after_render(self, target):

        self.draw_overlapping_trees(target)

    def draw_overlapping_trees(self, surface):

        hex = pixel_to_hex(self.game.hex_layout, self.position.screen_pos())

        bl = Hex.hex_neighbour(hex, 4)
        br = Hex.hex_neighbour(hex, 5)

        for hex in (bl, br):

            if self.game.map.get_tile((hex.x, hex.y)) == Tile.WOODS:
                self.game.map_image.image.draw_overlap_trees(surface, hex)

    def end_death_effect(self):
        self.orphan()
