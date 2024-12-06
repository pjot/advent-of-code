
import time
def parse(file):
    walls = set()
    ym, xm = 0, 0
    guard = None
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            ym = max(y, ym)
            for x, c in enumerate(line.strip()):
                xm = max(x, xm)
                if c == "#":
                    walls.add((x, y))
                if c in "v<>^":
                    guard = (x, y, c)

    return walls, (xm, ym), guard

def move(x, y, d):
    if d == ">": return x + 1, y
    if d == "<": return x - 1, y
    if d == "v": return x, y + 1
    if d == "^": return x, y - 1

def rotate(d):
    if d == ">": return "v"
    if d == "<": return "^"
    if d == "v": return "<"
    if d == "^": return ">"

def iterate(walls, guard, limit):
    x, y, d = guard
    max_x, max_y = limit
    seen = set()
    while True:
        moved = move(x, y, d)

        if moved in walls:
            d = rotate(d)
        else:
            x, y = moved
            if x > max_x or x < 0 or y > max_y or y < 0:
                return seen
            seen.add(moved)

def loops(walls, guard, limit):
    x, y, d = guard
    max_x, max_y = limit
    seen = set()
    while True:
        moved = move(x, y, d)

        if moved in walls:
            d = rotate(d)
        else:
            x, y = moved
            if x > max_x or x < 0 or y > max_y or y < 0:
                return False

        if (x, y, d) in seen:
            return True
        
        seen.add((x, y, d))

def limits(walls):
    ymi = xmi = 1000000
    yma = xma = 0
    for x, y in walls:
        ymi = min(ymi, y)
        xmi = min(xmi, x)
        yma = max(yma, y)
        xma = max(xma, x)

    return ymi, yma, xmi, xma


walls, limit, guard = parse("input")

print("Part 1:", len(iterate(walls, guard, limit)))

ymi, yma, xmi, xma = limits(walls)
two = 0
for y in range(ymi, yma+1):
    for x in range(xmi, xma+1):
        added_wall = {(x, y)}
        if loops(walls | added_wall, guard, limit):
            two += 1

print("Part 2:", two)
