def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    grid[x, y] = c
    return grid

def move(x, y, d):
    match d:
        case ">": return x + 1, y, d
        case "<": return x - 1, y, d
        case "v": return x, y + 1, d
        case "^": return x, y - 1, d

def bounce(d, mirror):
    match d, mirror:
        case "^", "/": return ">"
        case ">", "/": return "^"
        case "v", "/": return "<"
        case "<", "/": return "v"

        case "^", "\\": return "<"
        case ">", "\\": return "v"
        case "v", "\\": return ">"
        case "<", "\\": return "^"

def beam(grid, x, y, d):
    horizon = {(x, y, d)}
    seen = set()

    width = max(set(p[0] for p in grid.keys()))
    height = max(set(p[1] for p in grid.keys()))

    while horizon:
        new_horizon = set()
        for x, y, d in horizon:
            if x > width or x < 0:
                continue
            if y > height or y < 0:
                continue

            seen.add((x, y, d))

            if (x, y) in grid:
                v = grid[x, y]
                if v == "-" and d in "^v":
                    new_horizon.add((x - 1, y, "<"))
                    new_horizon.add((x + 1, y, ">"))
                    continue

                if v == "|" and d in "<>":
                    new_horizon.add((x, y - 1, "^"))
                    new_horizon.add((x, y + 1, "v"))
                    continue

                if v in "/\\":
                    d = bounce(d, v)

            new_horizon.add(move(x, y, d))

        horizon = new_horizon - seen

    visited = set((x, y) for x, y, _ in seen)
    return len(visited)

def one(grid):
    return beam(grid, 0, 0, ">")

def two(grid):
    width = max(set(p[0] for p in grid.keys()))
    height = max(set(p[1] for p in grid.keys()))

    energized = []
    for x in range(width):
        energized.append(beam(grid, x, 0, "v"))
        energized.append(beam(grid, x, height, "^"))

    for y in range(height):
        energized.append(beam(grid, 0, y, ">"))
        energized.append(beam(grid, width, y, "<"))

    return max(energized)

grid = parse("input")

print("Part 1:", one(grid))
print("Part 2:", two(grid))
