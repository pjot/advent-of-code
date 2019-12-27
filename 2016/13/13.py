import time


def build_grid(magic_number, height, width):
    grid = {}
    for x in range(width):
        for y in range(height):
            if is_wall(x, y, magic_number):
                grid[x, y] = '#'
            else:
                grid[x, y] = '.'
    return grid
    

def is_wall(x, y, magic_number):
    d = x * x + 3 * x + 2 * x * y + y + y * y
    ones = 0
    for digit in '{0:b}'.format(d + magic_number):
        if digit == '1':
            ones += 1
    return ones % 2 == 1


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def bfs(grid, start, end):
    distance = 0
    seen = {start}
    horizon = [start]
    locations = 0

    while len(horizon) > 0:
        new_horizon = []
        distance += 1
        for point in horizon:
            for n in neighbours(point):
                if grid.get(n) is None:
                    continue
                if n in seen:
                    continue
                if grid.get(n) == '#':
                    continue

                seen.add(n)
                if n == end:
                    return distance, locations

                new_horizon.append(n)

        if distance == 50:
            locations = len(seen)

        horizon = new_horizon


magic_number = 1358
end = (31, 39)
grid = build_grid(magic_number, 45, 45)

distance, locations = bfs(grid, (1, 1), end)

print('Part 1:', distance)
print('Part 2:', locations)