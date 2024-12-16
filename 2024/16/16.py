import heapq

Point = tuple[int, int]
Grid = set[Point]

def parse(file: str) -> tuple[Grid, Point, Point]:
    grid = set()
    start = (0, 0)
    end = (0, 0)
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            if not line.strip():
                continue
            for x, c in enumerate(line):
                if c in ".ES":
                    grid.add((x, y))
                if c == "S":
                    start = x, y
                if c == "E":
                    end = x, y
    return grid, start, end

def neighbours(p: Point, d: str) -> list[tuple[int, Point, str]]:
    return [
        (1, move(p, d), d),
        (1001, move(p, turn_left(d)), turn_left(d)),
        (1001, move(p, turn_right(d)), turn_right(d)),
    ]

def turn_right(d: str) -> str:
    if d == "E":
        return "S"
    if d == "W":
        return "N"
    if d == "N":
        return "E"
    if d == "S":
        return "W"
    return d

def turn_left(d: str) -> str:
    return turn_right(turn_right(turn_right(d)))

def move(p: Point, d: str) -> Point:
    x, y = p
    if d == "E":
        return x + 1, y
    if d == "W":
        return x - 1, y
    if d == "N":
        return x, y - 1
    if d == "S":
        return x, y + 1
    return p

grid, start, end = parse("input")

seen = {(start, "E"): 0}
lowest = float("inf")
best = set()

states = [(0, start, "E", [start])]

while states:
    cost, p, d, path = heapq.heappop(states)

    if cost > lowest:
        break

    if p == end:
        lowest = cost
        best |= set(path)

    seen[p, d] = cost

    for new_cost, n, new_direction in neighbours(p, d):
        if n not in grid:
            continue

        stored = seen.get((n, new_direction), float("inf"))
        if cost + new_cost < stored:
            new_state = (cost + new_cost, n, new_direction, path + [n])
            heapq.heappush(states, new_state)

print("Part 1:", lowest)
print("Part 2:", len(best))
