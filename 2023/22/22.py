from collections import defaultdict

def parse(file):
    bricks = []
    with open(file) as f:
        for line in f.readlines():
            a, b = line.strip().split("~")
            a = tuple(int(c) for c in a.split(","))
            b = tuple(int(c) for c in b.split(","))
            bricks.append((a, b))
    return bricks

def can_move(brick, heights):
    a, b = brick
    x1, y1, z1 = a
    x2, y2, z2 = b
    if z1 == z2 == 1:
        return False

    z = z1 - 1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if z <= heights[x, y]:
                return False

    return True

def move(brick):
    (x1, y1, z1), (x2, y2, z2) = brick
    return (x1, y1, z1-1), (x2, y2, z2-1)

def new_heights(heights, brick):
    (x1, y1, z1), (x2, y2, z2) = brick

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            heights[x, y] = max(heights[x, y], z2)

    return heights

def fall(bricks):
    new_bricks = []
    moved = 0

    heights = defaultdict(lambda: 0)
    bricks.sort(key=lambda b: b[0][2])

    for brick in bricks:
        if can_move(brick, heights):
            b = move(brick)
            moved += 1
            while can_move(b, heights):
                b = move(b)
        else:
            b = brick

        new_bricks.append(b)
        heights = new_heights(heights, b)

    return new_bricks, moved

def removable(bricks):
    fallen = count = 0
    for b in bricks:
        remaining = list(set(bricks) - {b})
        _, moved = fall(remaining)
        if moved > 0:
            fallen += moved
        else:
            count += 1
    return count, fallen

def stabilize(bricks):
    moved = 1
    while moved > 0:
        bricks, moved = fall(bricks)
    return bricks

bricks = parse("input")
bricks = stabilize(bricks)
one, two = removable(bricks)

print("Part 1:", one)
print("Part 2:", two)

