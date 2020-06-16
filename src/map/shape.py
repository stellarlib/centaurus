

def make_hex(radius):

    for x in range(-radius, radius + 1):

        y1 = max(-radius, -x - radius)
        y2 = min(radius, -x + radius)
        for y in range(y1, y2 + 1):
            yield (x, y)
