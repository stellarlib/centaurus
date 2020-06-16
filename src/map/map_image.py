from src.map import Tile, hex_to_pixel, Hex
from src.tile import get_tile_image
from src.settings import MAP_W, MAP_H, TREE_POSITIONS
from stellarlib import BaseSurface
from src.color import Color
from src.sprites import TreeSprite


class MapImage(object):

    def __init__(self, game):

        self.game = game
        self.map = self.game.map
        self.surface = self.init_surface()
        self.tree_sprite = TreeSprite()

    def init_surface(self):

        surface = BaseSurface.make_blank(MAP_W, MAP_H)
        surface.fill(Color.BLACK)

        return surface

    def init_map_image(self):
        self._draw_tiles()
        self._draw_trees()

    def _draw_tiles(self):
        for point in self.map.all_points():
            self._draw_tile(point)

    def _draw_tile(self, hex_coord):

        tile_image = get_tile_image(self.map.get_tile(hex_coord))
        pixel_coord = hex_to_pixel(self.game.hex_layout, Hex(*hex_coord))
        tile_image.draw(self.surface, pixel_coord)

    def _draw_trees(self):

        points = list(self.map.all_of_tile(Tile.WOODS))
        points.sort(key=lambda p: p[0], reverse=True)
        [self._draw_tree(point) for point in points]

    def _draw_tree(self, hex_coord):

        px, py = hex_to_pixel(self.game.hex_layout, Hex(*hex_coord))
        [self.tree_sprite.draw(self.surface, pos=(px + tx, py + ty))
            for (tx, ty) in TREE_POSITIONS]

    def draw(self, display_surface):

        self.surface.draw(display_surface)

    def update(self):
        pass

    def draw_overlap_trees(self, surface, hex):

        px, py = hex_to_pixel(self.game.hex_layout, hex)
        [self.tree_sprite.draw(surface, pos=(px + tx, py + ty))
            for tx, ty in TREE_POSITIONS]
