type Point = tuple[int, int]
type Rolls = set[Point]

def parse(file: str) -> Rolls:
    rolls = set()
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            for x, c in enumerate(line):
                if c == "@":
                    rolls.add((x, y))
    return rolls

def neighbours(p: Point, rolls: Rolls) -> int:
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    x, y = p
    ns = 0
    for dx, dy in deltas:
        if (x + dx, y + dy) in rolls:
            ns += 1
    return ns

def accessible(rolls: Rolls) -> Rolls:
    accessible = set()
    for p in rolls:
        if neighbours(p, rolls) < 4:
            accessible.add(p)
    return accessible

def two(rolls: Rolls) -> int:
    initial_roll_count = len(rolls)
    while to_remove := accessible(rolls):
        rolls -= to_remove
    return initial_roll_count - len(rolls)

rolls = parse("input")
print("Part 1:", len(accessible(rolls)))
print("Part 2:", two(rolls))

