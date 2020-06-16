PIXEL_SCALE = 4

# SCREEN_W = 220 * PIXEL_SCALE
# SCREEN_H = 220 * PIXEL_SCALE
SCREEN_W = 250 * PIXEL_SCALE
SCREEN_H = 240 * PIXEL_SCALE


TILE_W = 20 * PIXEL_SCALE
TILE_H = 20 * PIXEL_SCALE

SIZE = 12 * PIXEL_SCALE

TILE_SIZE = SIZE + PIXEL_SCALE, SIZE
#HEX_ORIGIN = 110 * PIXEL_SCALE, 110 * PIXEL_SCALE
HEX_ORIGIN = 125 * PIXEL_SCALE, 125 * PIXEL_SCALE

MAP_W = SCREEN_W
MAP_H = SCREEN_H

TREE_POSITIONS = [
                  (0, PIXEL_SCALE * -10),
                  (PIXEL_SCALE * -10, PIXEL_SCALE * -4)
                 ]

RUMBLE_MAG = max((1, PIXEL_SCALE // 2))