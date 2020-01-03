def step(steps):
    hex_grid = {}
    '''
    x = ne-sw
    y = nw-se
    '''
    curr = (0, 0)
    seen = set()
    for step in steps.split(','):
        dx, dy = 0, 0
        if step == 'n':
            dx = 1
            dy = 1
        if step == 's':
            dx = -1
            dy = -1
        if step == 'se':
            dy = -1
        if step == 'nw':
            dy = 1
        if step == 'ne':
            dx = 1
        if step == 'sw':
            dx = -1
        
        x, y = curr
        curr = (x + dx, y + dy)
        seen.add(curr)

    return curr, seen


def neighbours(p):
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
    ]


def bfs(pos):
    horizon = {pos}
    distance = 0
    seen = set()
    while horizon:
        new_horizon = set()
        for h in horizon:
            if h == (0, 0):
                return distance
            seen.add(h)
            for n in neighbours(h):
                if n in seen:
                    continue
                new_horizon.add(n)
        distance += 1
        horizon = new_horizon


def reverse_bfs(search):
    horizon = {(0, 0)}
    distance = 0
    seen = set()
    to_find = len(search)
    while horizon:
        new_horizon = set()
        for h in horizon:
            seen.add(h)
            search.discard(h)
            if len(search) == 1:
                return distance
            for n in neighbours(h):
                if n in seen:
                    continue
                new_horizon.add(n)
        distance += 1
        horizon = new_horizon


with open('input') as f:
    steps = f.readline().strip()

end, positions = step(steps)
print('Part 1:', bfs(end))
print('Part 2:', reverse_bfs(positions))