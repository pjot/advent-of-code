file = "input.txt"

blizzards = []
walls = set()
with open(file) as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            p = x, y
            if c == "#":
                walls.add(p)
            elif c in "<>v^":
                blizzards.append((p, c))

xs = [x for x, _ in walls]
ys = [y for _, y in walls]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

def reset_blizzard(b, d):
    x, y = b
    match d:
        case ">": return 1, y
        case "<": return max_x-1, y
        case "^": return x, max_y-1
        case "v": return x, 1

def move(b, d):
    x, y = b
    match d:
        case ">": return x+1, y
        case "<": return x-1, y
        case "^": return x, y-1
        case "v": return x, y+1

def move_blizzards():
    global blizzards
    new_blizzards = []
    for b, d in blizzards:
        if (n := move(b, d)) in walls:
            n = reset_blizzard(b, d)
        new_blizzards.append((n, d))
    blizzards = new_blizzards

def neighbours(p):
    x, y = p
    return [
        (x, y+1),
        (x+1, y),
        (x, y-1),
        (x-1, y),
        (x, y),
    ]

def is_outside(n):
    x, y = n
    return y < min_y or y > max_y

def search(start, end):
    horizon = {start}
    steps = 0
    while horizon:
        new_horizon = set()

        move_blizzards()
        blizzard_points = set([p for p, _ in blizzards])
        for h in horizon:
            for n in neighbours(h):
                if n == end:
                    return steps + 1
                if n in walls:
                    continue
                if n in blizzard_points:
                    continue
                if is_outside(n):
                    continue

                new_horizon.add(n)

        horizon = new_horizon
        steps += 1

start = 1, 0
end = max_x-1, max_y

one = search(start, end)
print("Part 1:", one)

two = search(end, start)
three = search(start, end)
print("Part 2:", one + two + three)
