import hashlib


def neighbours(i, path, point):
    x, y = point
    hash = hashlib.md5((i + path).encode()).hexdigest()
    points = []
    open_letters = 'bcdef'
    if hash[0] in open_letters and y > 0:
        points.append(('U', (x, y - 1)))
    if hash[1] in open_letters and y < 3:
        points.append(('D', (x, y + 1)))
    if hash[2] in open_letters and x > 0:
        points.append(('L', (x - 1, y)))
    if hash[3] in open_letters and x < 3:
        points.append(('R', (x + 1, y)))
    return points


def shortest_path(i):
    curr = (0, 0)
    end = (3, 3)
    horizon = [('', curr)]
    distance = 0
    shortest = None
    longest = 0
    while len(horizon) > 0:
        new_horizon = []
        for path, point in horizon:
            if point == end:
                longest = max(longest, distance)
                if shortest is None:
                    shortest = path
                continue
            for p, n in neighbours(i, path, point):
                new_horizon.append((path + p, n))

        distance += 1
        horizon = new_horizon
    return shortest, longest


one, two = shortest_path('mmsxrhfx')
print('Part 1:', one)
print('Part 2:', two)