def turn(direction):
    if direction == 'N':
        return 'W'
    if direction == 'W':
        return 'S'
    if direction == 'S':
        return 'E'
    if direction == 'E':
        return 'N'


def move(direction, curr):
    dx, dy = 0, 0
    if direction == 'N':
        dy = -1
    if direction == 'W':
        dx = -1
    if direction == 'S':
        dy = 1
    if direction == 'E':
        dx = 1
    x, y = curr
    return x + dx, y + dy


def position_of(c, grid):
    for k, v in grid.items():
        if v == c:
            return k
    return None


def distance_to(c):
    grid = grid_until(c)
    x, y = position_of(c, grid)
    return abs(x) + abs(y)


def grid_until(n):
    def can_turn(p, d):
        return grid.get(move(turn(d), p)) is None

    grid = {}
    grid[0, 0] = 1
    grid[1, 0] = 2
    point = (1, 0)
    value = 2
    direction = 'E'
    while value <= n:
        if can_turn(point, direction):
            direction = turn(direction)

        grid[point] = value
        point = move(direction, point)
        value += 1
    return grid


def surround_sum(point, grid):
    x, y = point
    surrounding = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y - 1),
    ]
    s = 0
    for p in surrounding:
        s += grid.get(p, 0)
    return s


def sum_grid(n):
    def can_turn(p, d):
        return grid.get(move(turn(d), p)) is None

    grid = {}
    grid[0, 0] = 1
    grid[1, 0] = 1
    point = (1, 0)
    value = 1
    direction = 'E'
    while value <= n:
        if can_turn(point, direction):
            direction = turn(direction)

        value = surround_sum(point, grid)
        grid[point] = value
        point = move(direction, point)
    return value


print('Part 1:', distance_to(325489))
print('Part 2:', sum_grid(325489))

