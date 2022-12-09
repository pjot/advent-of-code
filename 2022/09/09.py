def parse(file):
    movements = []
    with open(file) as f:
        for line in f.readlines():
            direction, delta = line.strip().split()
            movements.append((direction, int(delta)))
    return movements

def add(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def move(p, direction):
    delta = {
        "U": (0, -1),
        "D": (0, 1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    return add(p, delta[direction])

def sign(n):
    if n == 0:
        return n
    return int(n / abs(n))

def follow(head, tail):
    if head == tail:
        return tail

    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty

    if dy == 0:
        if dx > 1:
            return tx + 1, ty
        if dx < -1:
            return tx - 1, ty

    elif dx == 0:
        if dy > 1:
            return tx, ty + 1
        if dy < -1:
            return tx, ty - 1

    elif abs(dx) + abs(dy) > 2:
        return tx + sign(dx), ty + sign(dy)

    return tail

def visited_positions(length, movements):
    rope = [(0, 0)] * length
    positions = {rope[-1]}
    for direction, delta in movements:
        for _ in range(delta):
            next_rope = [move(rope.pop(0), direction)]
            for tail in rope:
                head = next_rope[-1]
                next_rope.append(follow(head, tail))
            rope = next_rope

            positions.add(rope[-1])
    return len(positions)

movements = parse("input.txt")

print("Part 1:", visited_positions(2, movements))
print("Part 2:", visited_positions(10, movements))
