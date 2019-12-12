def coords_for_path(path):
    x, y = 0, 0
    coords = []
    for corner in path:
        direction = corner[0]
        length = int(corner[1:])

        dx, dy = 0, 0
        if direction == 'R':
            dx = 1
        if direction == 'L':
            dx = -1
        if direction == 'U':
            dy = 1
        if direction == 'D':
            dy = -1

        for _ in range(length):
            x += dx
            y += dy
            coords.append((x, y))
    return coords


def parse_file(file):
    with open(file) as f:
        path1 = f.readline().split(',')
        path2 = f.readline().split(',')
    return path1, path2


def distance(x, y):
    return abs(x) + abs(y)


def lowest_distance(coords):
    lowest = float('inf')
    for x, y in coords:
        d = distance(x, y)
        if d < lowest:
            lowest = d
    return lowest


def lowest_step(intersection, coords1, coords2):
    lowest_step = float('inf')
    for x, y in intersections:
        first = coords1.index((x, y))
        second = coords2.index((x, y))
        steps = first + second + 2
        lowest_step = min(steps, lowest_step)
    return lowest_step


path1, path2 = parse_file('input.path')

coords1 = coords_for_path(path1)
coords2 = coords_for_path(path2)

intersections = set(coords1) & set(coords2)

print('Part 1:', lowest_distance(intersections))
print('Part 2:', lowest_step(intersections, coords1, coords2))
