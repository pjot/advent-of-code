Point = tuple[int, int]
Direction = str
Guard = tuple[Point, Direction]
Walls = set[Point]

def parse(file: str) -> tuple[Walls, Guard]:
    walls = set()
    guard = ((0, 0), "<")
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    walls.add((x, y))
                if c in "v<>^":
                    guard = ((x, y), c)

    return walls, guard

def move(p: Point, d: Direction) -> Point:
    x, y = p
    if d == ">": return x + 1, y
    if d == "<": return x - 1, y
    if d == "v": return x, y + 1
    if d == "^": return x, y - 1
    return p

def rotate(d: Direction) -> Direction:
    if d == ">": return "v"
    if d == "<": return "^"
    if d == "v": return "<"
    if d == "^": return ">"
    return d

def limits(walls: Walls) -> Point:
    xl, yl = 0, 0
    for x, y in walls:
        xl = max(x, xl)
        yl = max(y, yl)
    return xl, yl

def within_bounds(p: Point, bounds: Point) -> bool:
    x, y = p
    max_x, max_y = bounds
    inside_x = 0 <= x <= max_x
    inside_y = 0 <= y <= max_y
    return inside_x and inside_y

def tick(walls: Walls, p: Point, d: Direction) -> tuple[Point, Direction]:
    moved = move(p, d)
    if moved in walls:
        return p, rotate(d)
    else:
        return moved, d

def iterate(walls: Walls, guard: Guard) -> set[Point]:
    p, d = guard
    bounds = limits(walls)
    seen = {p}
    while True:
        p, d = tick(walls, p, d)

        if not within_bounds(p, bounds):
            return seen

        seen.add(p)

def loops(walls: Walls, guard: Guard) -> bool:
    p, d = guard
    bounds = limits(walls)
    seen = {guard}
    while True:
        p, d = tick(walls, p, d)

        if not within_bounds(p, bounds):
            return False

        if (p, d) in seen:
            return True

        seen.add((p, d))

walls, guard = parse("input")

seen = iterate(walls, guard)
print("Part 1:", len(seen))

two = 0
for p in seen:
    if loops(walls | {p}, guard):
        two += 1
print("Part 2:", two)
