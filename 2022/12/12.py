def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == "S":
                    start = x, y
                    grid[start] = "a"
                elif c == "E":
                    end = x, y
                    grid[end] = "z"
                else:
                    grid[x, y] = c
    return grid, start, end

def add(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def possible_steps(grid, position):
    delta = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    current = grid[position]

    for d in delta:
        n = add(position, d)
        if n in grid:
            yield n

def length(grid, start, valid_step):
    distance = {}
    horizon = {start}
    steps = 0
    while horizon:
        new_horizon = set()
        for h in horizon:
            distance[h] = steps

            for s in possible_steps(grid, h):
                if s in distance:
                    continue
                if not valid_step(ord(grid[h]), ord(grid[s])):
                    continue
                new_horizon.add(s)

        horizon = new_horizon
        steps += 1
    return distance

def going_up(one, two):
    return one + 2 > two

def going_down(one, two):
    return two + 2 > one

grid, start, end = parse("input.txt")

distance_up = length(grid, start, going_up)
print("Part 1:", distance_up[end])

distance_down = length(grid, end, going_down)
print("Part 2:", min(
    distance_down[p] for p, v in grid.items()
    if v == "a" and p in distance_down
))
