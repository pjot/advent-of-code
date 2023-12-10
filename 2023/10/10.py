from collections import defaultdict

def parse(file):
    grid = defaultdict(lambda: ".")
    start = (0, 0)
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line):
                grid[x, y] = c
                if c == "S":
                    start = (x, y)
    return grid, start

def directions(v):
    match v:
        case "|": return "NS"
        case "-": return "EW"
        case "L": return "NE"
        case "J": return "NW"
        case "7": return "SW"
        case "F": return "SE"
        case "S": return "NEWS"
    return ""

def for_directions(dirs):
    ds = []
    if "N" in dirs: ds.append(("S", (0, -1)))
    if "S" in dirs: ds.append(("N", (0, 1)))
    if "E" in dirs: ds.append(("W", (1, 0)))
    if "W" in dirs: ds.append(("E", (-1, 0)))
    return ds

def neighbours(grid, p):
    x, y = p
    possible_directions = directions(grid[p])
    deltas = for_directions(possible_directions)
    for matching, (dx, dy) in deltas:
        dp = (x+dx, y+dy)
        if matching in directions(grid[dp]):
            yield (x+dx, y+dy)

def walk(grid, start):
    horizon = [start]
    seen = set()
    seen.add(start)
    steps = 0

    while horizon:
        if horizon:
            steps += 1
        new_horizon = []
        for h in horizon:
            for n in neighbours(grid, h):
                if n in seen:
                    continue

                seen.add(n)
                new_horizon.append(n)

        horizon = new_horizon
    return steps, seen

def enlarge(points, grid):
    larger = set()
    for p in points:
        x, y = p
        mx, my = x*3 + 1, y*3 + 1

        moved = set()
        moved.add((mx, my))

        v = grid[p]
        match v:
            case "|":
                moved.add((mx, my+1))
                moved.add((mx, my-1))
            case "-":
                moved.add((mx+1, my))
                moved.add((mx-1, my))
            case "L":
                moved.add((mx+1, my))
                moved.add((mx, my-1))
            case "J":
                moved.add((mx-1, my))
                moved.add((mx, my-1))
            case "7":
                moved.add((mx-1, my))
                moved.add((mx, my+1))
            case "F":
                moved.add((mx+1, my))
                moved.add((mx, my+1))
            case "S":
                moved.add((mx-1, my))
                moved.add((mx, my+1))
                moved.add((mx+1, my))
                moved.add((mx, my-1))
        larger |= moved
    return larger

def biggest(points):
    xs = ys = []
    for x, y in points:
        xs.append(x)
        ys.append(y)
    return max(xs), max(ys)

def one_point_inside(points):
    x = y = 2
    while True:
        x += 1
        p = x, y
        if p in points:
            return x + 1, y
        if x > 1000:
            x = 2
            y += 3

def possible_neighbours(p):
    x, y = p
    deltas = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]
    for dx, dy in deltas:
        yield x+dx, y+dy

def fill(start, points):
    seen = set()
    seen.add(start)

    horizon = [start]

    while horizon:
        new_horizon = []
        for h in horizon:
            for n in possible_neighbours(h):
                if n in seen:
                    continue
                if n not in points:
                    new_horizon.append(n)
                    seen.add(n)
        horizon = new_horizon

    return seen

def all_neighbours(p):
    x, y = p
    deltas = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1),
    ]
    for dx, dy in deltas:
        yield x+dx, y+dy

def count_inside(points, grid):
    larger = enlarge(points, grid)
    start = one_point_inside(larger)

    all_inside = fill(start, larger)
    max_x, max_y = biggest(all_inside)

    inside = set()
    for y in range(max_y):
        for x in range(max_x):
            if x % 3 == 1 and y % 3 == 1:
                if all(n in all_inside for n in all_neighbours((x, y))):
                    inside.add((x, y))

    return len(inside)

grid, start = parse("input")
steps, seen = walk(grid, start)

print("Part 1:", steps -1)

inside = count_inside(seen, grid)

print("Part 2:", inside)

