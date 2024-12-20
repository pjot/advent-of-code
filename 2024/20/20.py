Point = tuple[int, int]

def parse(file: str) -> tuple[set[Point], Point, Point]:
    walls = set()
    start = 0, 0
    end = 0, 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                continue
            for x, c in enumerate(line):
                if c == "S":
                    start = x, y
                if c == "E":
                    end = x, y
                if c == "#":
                    walls.add((x, y))

    return walls, start, end

def neighbours(p: Point) -> list[Point]:
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

def walk(
    walls: set[Point],
    start: Point,
    end: Point
) -> dict[Point, int]:
    steps = 0
    horizon = {start}
    distances = {}
    while horizon:
        new_horizon = set()
        for h in horizon:
            if h in distances:
                continue

            distances[h] = steps

            for n in neighbours(h):
                if n == end:
                    distances[n] = steps + 1
                    return distances

                if n in walls:
                    continue

                new_horizon.add(n)
        steps += 1
        horizon = new_horizon

    return distances

def generate_path(
    distances: dict[Point, int],
    start: Point,
    end: Point,
) -> list[Point]:
    path = [end]
    current = end
    while current != start:
        d = distances[current]
        for n in neighbours(current):
            if distances.get(n) == d - 1:
                current = n
                path.append(n)
                break

    return list(reversed(path))

def manhattan(a: Point, b: Point) -> int:
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

def solve(
    path: list[Point],
    distances: dict[Point, int]
):
    one = two = 0
    for i, p1 in enumerate(path):
        path_ahead = path[i+100:]
        for p2 in path_ahead:
            cheat_steps = manhattan(p1, p2)
            if cheat_steps > 20:
                continue

            saving = distances[p2] - distances[p1] - cheat_steps
            if saving < 100:
                continue

            if cheat_steps <= 2:
                one += 1
            if cheat_steps <= 20:
                two += 1
    return one, two

walls, start, end = parse("input")
distances = walk(walls, start, end)
path = generate_path(distances, start, end)
one, two = solve(path, distances)

print("Part 1:", one)
print("Part 2:", two)
