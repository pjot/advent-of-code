import time
def parse(file):
    walls = []
    tx = ty = 0
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            x, y = [int(n) for n in line.split(",")]
            walls.append((x, y))
            tx = max(x, tx)
            ty = max(y, ty)
    return walls, (tx, ty)

def neighbours(p):
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

def outside(p, target):
    x, y = p
    tx, ty = target
    inside = 0 <= x <= tx and 0 <= y <= ty
    return not inside

def shortest_path(walls, fallen, target):
    walls = set(walls[:fallen])
    seen = set()
    start = 0, 0
    steps = 0
    horizon = {start}
    while horizon:
        new_horizon = set()
        for h in horizon:
            seen.add(h)
            for n in neighbours(h):
                if n == target:
                    return steps + 1

                if outside(n, target):
                    continue
                if n in seen:
                    continue
                if n in walls:
                    continue

                new_horizon.add(n)

        horizon = new_horizon
        steps += 1

    return -1

def first_failed(walls, target):
    little = 0
    big = len(walls)
    while True:
        test = little + (big - little) // 2
        if shortest_path(walls, test, target) > 0:
            little = test
            if little == test and big - little == 1:
                little = big
        else:
            big = test
        if little == big:
            x, y = walls[test]
            return f"{x},{y}"


walls, target = parse("input")
print("Part 1:", shortest_path(walls, 1024, target))
print("Part 2:", first_failed(walls, target))
