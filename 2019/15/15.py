from intcode import Computer, parse_file


def neighbours(point):
    x, y = point
    return [
        (4, (x + 1, y)),
        (3, (x - 1, y)),
        (1, (x, y + 1)),
        (2, (x, y - 1)),
    ]


def next_point(point, direction):
    x, y = point
    ds = {
        4: (x + 1, y),
        3: (x - 1, y),
        1: (x, y + 1),
        2: (x, y - 1),
    }
    return ds[direction]


def turn_right(d):
    if d == 1:
        return 4
    if d == 2:
        return 3
    if d == 3:
        return 1
    if d == 4:
        return 2


def turn_left(d):
    return turn_right(
        turn_right(
            turn_right(d)
        )
    )


def build_grid(program):
    computer = Computer(program)

    current = (0, 0)
    grid = {current: 1}
    direction = 4

    while True:
        next = next_point(current, direction)
        output = computer.run_with_input(direction)
        grid[next] = output

        if output == 0:
            direction = turn_left(direction)

        if output in [1, 2]:
            direction = turn_right(direction)
            current = next

        if current == (0, 0) and direction == 4:
            break

    return grid


def bfs(grid, start, end=None):
    visited = set()
    distance = 0
    horizon = [start]
    while horizon:
        new_horizon = []
        for p in horizon:
            for _, point in neighbours(p):
                if grid.get(point, 1) == 0:
                    continue

                if end is not None and point == end:
                    return distance + 1

                if point not in visited:
                    new_horizon.append(point)

                visited.add(point)
                grid[point] = 2

        horizon = new_horizon
        distance += 1

    return distance


grid = build_grid(parse_file("input.intcode"))
for k, v in grid.items():
    if v == 2:
        oxygen = k
        break

one = bfs(grid, (0, 0), oxygen)
two = bfs(grid, oxygen) - 1
print('Part 1:', one)
print('Part 2:', two)
