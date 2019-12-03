def coords_for_path(path):
    x, y = 0, 0
    coords = set()
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
            coords.add((x, y))
    return coords

def distance(x, y):
    return abs(x) + abs(y)

def lowest_distance(coords):
    lowest = float('inf')
    for x, y in coords:
        d = distance(x, y)
        if d < lowest:
            lowest = d
    return lowest

def parse_file(file):
    with open(file) as f:
        path1 = f.readline().split(',')
        path2 = f.readline().split(',')
    return path1, path2

path1, path2 = parse_file('input.path')
coords1 = coords_for_path(path1)
coords2 = coords_for_path(path2)

intersections = coords1 & coords2

print lowest_distance(intersections)
