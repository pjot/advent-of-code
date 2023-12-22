def parse(file):
    clay = set()
    with open(file) as f:
        for line in f.readlines():
            parts = line.strip().split(", ")

            for p in parts:
                v, val = p.split("=")
                if ".." not in val:
                    first = v
                    first_value = int(val)
                else:
                    d, e = val.split("..")
                    for i in range(int(d), int(e) + 1):
                        if first == "x":
                            clay.add((first_value, i))
                        else:
                            clay.add((i, first_value))
    return clay

def below(p):
    x, y = p
    return x, y + 1

def above(p):
    x, y = p
    return x, y - 1

def next_to(p):
    x, y = p
    return {(x + 1, y), (x - 1, y)}

def empty(p, wall):
    deltas = [1, -1]
    seen = [False, False]
    x, y = p
    points = set()
    for d in range(100):
        for i, di in enumerate(deltas):
            if seen[i]:
                continue

            l = x + d * di, y

            if below(l) not in wall:
                return set()

            if l in wall:
                seen[i] = True
            else:
                points.add(l)

        if all(seen):
            return points

    return set()

def iterate(clay, source, moving, settled, limit):
    new_moving = set()
    for m in moving:
        b = below(m)
        if b not in clay:
            new_moving.add(b)
            continue

        to_settle = empty(m, clay)
        if to_settle:
            settled = settled | (to_settle - clay)
            new_moving.add(above(m))
        else:
            new_moving = new_moving | (next_to(m) - clay)

    mov = set()
    for x, y in new_moving:
        if y <= limit and (x, y):
            mov.add((x, y))

    return mov, settled

def inside(seen, min_y, max_y):
    return len([1 for _, y in seen if min_y <= y <= max_y])

def run(clay):
    source = (500, 0)
    moving = {below(source)}
    seen = {below(source)}
    settled = set()

    ys = [y for x, y in clay]
    max_y = max(ys)
    min_y = min(ys)

    count = 0

    while True:
        new_moving, settled = iterate(
            clay | settled,
            source,
            moving,
            settled,
            max_y
        )
        seen = seen | new_moving | settled

        moving = new_moving

        new_count = len(seen)
        if new_count == count:
            break

        count = new_count

    return inside(seen, min_y, max_y), len(settled)

clay = parse("input")
one, two = run(clay)

print("Part 1:", one)
print("Part 2:", two)

