def parse(file):
    walls = set()
    pebbles = set()
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line):
                if c == "#":
                    walls.add((x, y))
                if c == "O":
                    pebbles.add((x, y))
    return walls, pebbles

def move(p, direction, things, max_x, max_y):
    x, y = p
    while True:
        match direction:
            case "N":
                pn = x, y - 1
            case "S":
                pn = x, y + 1
            case "E":
                pn = x + 1, y
            case "W":
                pn = x - 1, y

        if pn in things:
            return x, y

        px, py = pn

        if px < 0 or py < 0 or px > max_x or py > max_y:
            return x, y

        x, y = pn

def sorter(direction):
    def k(p):
        x, y = p
        match direction:
            case "N":
                return y, x
            case "S":
                return -y, x
            case "E":
                return -x, y
            case "W":
                return x, y
    return k

def tilt(direction, pebbles, walls):
    n_peb = sorted(list(pebbles), key=sorter(direction))
    max_x = max([p[0] for p in pebbles | walls])
    max_y = max([p[1] for p in pebbles | walls])

    new_pebbles = set()

    for p in n_peb:
        x, y = p
        while True:
            match direction:
                case "N":
                    pn = x, y - 1
                case "S":
                    pn = x, y + 1
                case "E":
                    pn = x + 1, y
                case "W":
                    pn = x - 1, y

            if pn in new_pebbles | walls:
                new_pebbles.add((x, y))
                break

            px, py = pn

            if px < 0 or py < 0 or px > max_x or py > max_y:
                new_pebbles.add((x, y))
                break

            x, y = pn

    return new_pebbles

def load(pebbles, walls):
    max_y = max([p[1] for p in pebbles | walls])
    return sum(max_y + 1 - y for _, y in pebbles)

def cycle(pebbles, walls):
    pebbles = tilt("N", pebbles, walls)
    pebbles = tilt("W", pebbles, walls)
    pebbles = tilt("S", pebbles, walls)
    pebbles = tilt("E", pebbles, walls)

    return pebbles

def one(pebbles, walls):
    pebbles = tilt("N", pebbles, walls)
    return load(pebbles, walls)

def two(pebbles, walls):
    states = {}
    states[frozenset(pebbles)] = 0

    big = 1000000000 - 1

    for i in range(big):
        pebbles = cycle(pebbles, walls)

        f = frozenset(pebbles)
        if f in states:
            c = i - states[f]
            left = big - i
            if left % c == 0:
                return load(pebbles, walls)
        else:
            states[f] = i

walls, pebbles = parse("input")
print("Part 1:", one(pebbles, walls))
print("Part 2:", two(pebbles, walls))
