grid = {}
width = 0
height = 0
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            grid[(x, y)] = c
            width = max(width, x + 1)
            height = max(height, y)

def w(dx, dy):
    x, y, hits = 0, 0, 0
    while y < height:
        x = (x + dx) % width
        y = y + dy
        if grid[(x, y)] == '#':
            hits += 1
    return hits

print('Part 1:', w(3, 1))
print('Part 2:', w(1, 1) * w(3, 1) * w(5, 1) * w(7, 1) * w(1, 2))


