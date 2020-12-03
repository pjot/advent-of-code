from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

grid = {}
width = 0
height = 0
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            grid[Point(x, y)] = c
            width = max(width, x + 1)
            height = max(height, y)

def w(dx, dy):
    pos = Point(0, 0)
    hits = 0
    while pos.y < height:
        pos = Point(
            (pos.x + dx) % width,
            pos.y + dy
        )
        if grid[pos] == '#':
            hits += 1
    return hits

print('Part 1:', w(3, 1))
print('Part 2:', w(1, 1) * w(3, 1) * w(5, 1) * w(7, 1) * w(1, 2))


