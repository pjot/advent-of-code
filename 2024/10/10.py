Point = tuple[int, int]
Grid = dict[Point, int]
Path = tuple[Point]

def parse(file: str) -> Grid:
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c in "1234567890":
                    grid[x, y] = int(c)
    return grid

def neighbours(p: Point) -> list[Point]:
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

def paths(grid: Grid, p: Point) -> set[Path]:
    done = set()
    horizon = {(p, )}
    while horizon:
        new_horizon = set()

        for path in horizon:
            head = path[0]
            value = grid[head]

            for n in neighbours(head):
                if not grid.get(n):
                    continue

                if grid[n] == value + 1:
                    new_path = (n, *path)
                    if grid[n] == 9:
                        done.add(new_path)
                    else:
                        new_horizon.add(new_path)

        horizon = new_horizon

    return done

grid = parse("input")
one = two = 0
for p in grid:
    if grid[p] == 0:
        all_paths = paths(grid, p)

        unique = set()
        for pp in all_paths:
            unique.add(pp[0])

        one += len(unique)
        two += len(all_paths)

print("Part 1:", one)
print("Part 2:", two)
