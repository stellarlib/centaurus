from random import randint, shuffle


# vertical line draw modes
RANDOM_ALT = 0
LEFT_ALT = 1
RIGHT_ALT = 2


def make_hex(radius, start_point=(0, 0)):

    sx, sy = start_point

    for x in range(-radius, radius + 1):

        y1 = max(-radius, -x - radius)
        y2 = min(radius, -x + radius)
        for y in range(y1, y2 + 1):
            yield (x + sx, y + sy)


def make_horizontal_line(start_point, length, rev=False):

    sx, sy = start_point

    if rev:
        step = -1
        fx = sx - length
    else:
        step = 1
        fx = sx + length

    for x in range(sx, fx, step):
        yield (x, sy)


def make_down_right_line(start_point, length, rev=False):

    sx, sy = start_point

    if rev:
        step = -1
        fy = sy - length
    else:
        step = 1
        fy = sy + length
    for y in range(sy, fy, step):
        yield (sx, y)


def make_down_left_line(start_point, length, rev=False):

    sx, sy = start_point

    mod = 1
    if rev:
        mod = -1

    for i in range(length):

        y = sy + (i * mod)
        x = sx - (i * mod)

        yield (x, y)


def make_vertical_line(start_point, length, rev=False, mode=0):

    # default - up

    global RANDOM_ALT, LEFT_ALT, RIGHT_ALT

    rm = 0
    if mode == LEFT_ALT:
        rm = 0
    elif mode == RIGHT_ALT:
        rm = 1
    elif mode == RANDOM_ALT:
        rm = randint(0, 1)

    sx, sy = start_point

    mod = 1
    if rev:
        mod = -1

    for i in range(length):

        mx = ((i + rm) // 2) * mod
        my = i * mod

        x = sx - mx
        y = sy + my

        yield x, y


def make_ring(start_point, radius):

    return ((x, y) for x, y in make_hex(radius, start_point) if is_outer_point((x, y), start_point, radius))


def is_outer_point(point, start_point, radius):

    x, y = point
    sx, sy = start_point

    dx, dy = x - sx, y - sy
    ax, ay = abs(dx), abs(dy)

    return ax == radius or ay == radius or radius - (dx + dy) == 0 or -radius - (dx + dy) == 0


def make_structure(start_point, radius):

    ring = [p for p in make_ring(start_point, radius)]
    shuffle(ring)
    ring.pop()
    return (point for point in ring)

