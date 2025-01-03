Grid = dict[tuple[int, int], str]

def parse(file: str) -> Grid:
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line):
                grid[x, y] = c
    return grid

def xmas_count(grid: Grid, x: int, y: int) -> int:
    if grid[x, y] != "X":
        return 0

    def g(x1, y1, x2, y2, x3, y3):
        return (
            grid.get((x + x1, y + y1), "") +
            grid.get((x + x2, y + y2), "") +
            grid.get((x + x3, y + y3), "")
        )

    words = [
        g( 1,  0,  2,  0,  3,  0),
        g(-1,  0, -2,  0, -3,  0),
        g( 0,  1,  0,  2,  0,  3),
        g( 0, -1,  0, -2,  0, -3),
        g( 1,  1,  2,  2,  3,  3),
        g(-1, -1, -2, -2, -3, -3),
        g( 1, -1,  2, -2,  3, -3),
        g(-1,  1, -2,  2, -3,  3),
    ]
    return words.count("MAS")

def x_mas_count(grid: Grid, x: int, y: int) -> int:
    if grid[x, y] != "A":
        return 0

    one = {
        grid.get((x - 1, y - 1), ""),
        grid.get((x + 1, y + 1), ""),
    }
    two = {
        grid.get((x + 1, y - 1), ""),
        grid.get((x - 1, y + 1), ""),
    }
    correct = {"M", "S"}

    if one == correct and two == correct:
        return 1

    return 0

grid = parse("input")
one, two = 0, 0
for x, y in grid.keys():
    one += xmas_count(grid, x, y)
    two += x_mas_count(grid, x, y)

print("Part 1:", one)
print("Part 2:", two)
