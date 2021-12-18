def parse(file):
    with open(file) as f:
        line = f.readline().strip()

    xs, ys = line.replace('target area: ', '').split(' ')

    xs = xs.replace('x=', '').replace(',', '')
    xs = [int(x) for x in xs.split('..')]

    ys = ys.replace('y=', '').replace(',', '')
    ys = [int(y) for y in ys.split('..')]

    return xs, ys

def step(x, y, v, u):
    x += v
    y += u
    if v > 0:
        v -= 1
    elif v < 0:
        v += 1
    u -= 1
    return x, y, v, u

def is_match(v, u, xs, ys):
    x, y = 0, 0
    x0, x1 = xs
    y0, y1 = ys
    max_y = 0
    while y >= y0 and x <= x1:
        x, y, v, u = step(x, y, v, u)
        max_y = max(y, max_y)
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True, max_y

    return False, 0

xs, ys = parse('input.txt')
max_y = 0
working = 0
for v in range(-10, 200):
    for u in range(-120, 120):
        works, highest = is_match(v, u, xs, ys)
        if works:
            working += 1
            up = u + 120
            vp = v + 10
        if works and highest > max_y:
            max_y = highest

print("Part 1:", max_y)
print("Part 2:", working)
