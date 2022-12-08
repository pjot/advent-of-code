def parse(file):
    grid = {}
    mx, my = 0, 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            for x, char in enumerate(line):
                height = int(char)
                grid[(x, y)] = height
                mx = max(mx, x)
            my = max(my, y)
    return grid, mx, my

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def add(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def towards(grid, point, delta):
    while True:
        point = add(point, delta)
        if grid.get(point) is not None:
            yield grid[point]
        else:
            break

def is_visible(grid, point):
    height = grid[point]
    for direction in DIRECTIONS:
        if all(height > n for n in towards(grid, point, direction)):
            return True
    return False

def scenic_score(grid, point):
    height = grid[point]
    score = 1
    for direction in DIRECTIONS:
        d = 0
        for p in towards(grid, point, direction):
            d += 1
            if p >= height:
                break
        score *= d
    return score

grid, mx, my = parse("input.txt")

visible = 0
highest_score = 0
for y in range(my + 1):
    for x in range(mx + 1):
        if is_visible(grid, (x, y)):
            visible += 1

        score = scenic_score(grid, (x, y))
        highest_score = max(highest_score, score)

print("Part 1:", visible)
print("Part 2:", highest_score)
