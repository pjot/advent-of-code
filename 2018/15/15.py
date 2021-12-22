from heapq import heappop, heappush
from collections import defaultdict

class ElfDied(Exception):
    pass

def parse(file):
    grid = {}
    with open(file) as f:
        for y, row in enumerate(f.readlines()):
            for x, v in enumerate(row.strip()):
                grid[x, y] = (v, 200)
    return grid

def bounds(grid):
    xmi, xma = 0, 0
    ymi, yma = 0, 0
    for x, y in grid.keys():
        xmi = min(xmi, x)
        xma = max(xma, x)
        ymi = min(ymi, y)
        yma = max(yma, y)
    return xmi, xma, ymi, yma

def pr(grid):
    xmi, xma, ymi, yma = bounds(grid)
    for y in range(ymi, yma+1):
        things = []
        for x in range(xmi, xma+1):
            v, l = grid.get((x, y), ('_', 0))
            if v in 'EG':
                things.append(f'{v}({l})')
            print(v, end='')
        print('   ' + ', '.join(things))

def things_in(grid):
    ts = []
    for p, (v, _) in grid.items():
        if v in 'EG':
            ts.append(p)
    return sorted(ts, key=lambda t: (t[1], t[0]))

def neighbours(p, grid, all=False):
    x, y = p
    deltas = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    for dx, dy in deltas:
        p = (x+dx, y+dy)
        v, _ = grid.get(p, ('#', 0))
        if v == '.' or all:
            yield p

def distances(grid, start, extra_wall='#'):
    ds = {start: 0}
    seen = set()
    horizon = [(0, start)]
    horizon_set = set(horizon)
    while horizon:
        c, h = heappop(horizon)
        horizon_set.remove((c, h))
        seen.add(h)
        for n in neighbours(h, grid):
            if n in seen:
                continue
            if grid[n][0] == extra_wall:
                continue

            cost = c + 1
            ds[n] = cost

            if (cost, n) not in horizon_set:
                heappush(horizon, (cost, n))
                horizon_set.add((cost, n))
    return ds

def reading_first(points):
    return sorted(
        points,
        key=lambda c: (c[1], c[0]),
        reverse=True
    ).pop()

def reachable_from(grid, start, kind):
    horizon = [start]
    seen = set()
    reachable = set()
    while horizon:
        new_horizon = set()
        for h in horizon:
            seen.add(h)
            for n in neighbours(h, grid, all=True):
                if n in seen:
                    continue
                if grid[n][0] == kind:
                    reachable.add(n)
                    continue
                if grid[n][0] == '.':
                    new_horizon.add(n)
        horizon = new_horizon

    in_range = set()
    for p in reachable:
        for n in neighbours(p, grid):
            in_range.add(n)
    return in_range


def move(t, grid):
    thing = grid[t]
    kind, _ = thing

    enemy = 'E' if kind == 'G' else 'G'

    neighbour_tiles = [
        grid[n][0] for n in neighbours(t, grid, all=True)
    ]
    if enemy in neighbour_tiles:
        return grid, t

    enemies_in_range = reachable_from(grid, t, enemy)
    if not enemies_in_range:
        return grid, t

    distance_to = distances(grid, t, extra_wall=kind)
    distance_enemies = {
        coord: distance_to.get(coord, float('inf'))
        for coord in enemies_in_range
    }

    grouped_distances = defaultdict(list)
    for coord, distance in distance_enemies.items():
        grouped_distances[distance].append(coord)

    closest_distance = min(grouped_distances.keys())
    closest_points = grouped_distances[closest_distance]

    chosen = reading_first(closest_points)

    distance_to = distances(grid, chosen)
    possible_steps = defaultdict(list)
    for n in neighbours(t, grid):
        distance = distance_to.get(n, float('inf'))
        possible_steps[distance].append(n)

    if len(possible_steps) == 0:
        return grid, t

    closest_step = min(possible_steps.keys())
    closest_points = possible_steps[closest_step]

    step = reading_first(closest_points)

    grid[t] = ('.', 0)
    grid[step] = thing
    return grid, step

def lowest_life(points):
    return sorted(
        points,
        key=lambda c: (c[0], c[1][1], c[1][0]),
        reverse=True
    ).pop()[1]

def attack(t, grid, elf_attack):
    thing = grid[t]
    kind, _ = thing
    raise_on_elf_death = elf_attack is not None
    elf_attack = elf_attack or 3

    enemy = 'E' if kind == 'G' else 'G'

    neighbour_enemies = [
        (grid[n][1], n) for n in neighbours(t, grid, all=True)
        if grid[n][0] == enemy
    ]
    if neighbour_enemies:
        lowest = lowest_life(neighbour_enemies)
        c, life = grid[lowest]

        if kind == 'E':
            strength = elf_attack
        else:
            strength = 3

        if life <= strength:
            if kind == 'G' and raise_on_elf_death:
                raise ElfDied()
            grid[lowest] = ('.', 0)
        else:
            grid[lowest] = (c, life-strength)

    return grid

def iterate(grid, i, elf_attack):
    things = things_in(grid)
    seen = set()
    for t in things_in(grid):
        if t in seen:
            continue
#        print('.', end='')
        if grid[t][0] == '.':
            continue
        grid, t = move(t, grid)
        seen.add(t)
        grid = attack(t, grid, elf_attack)
        if is_finished(grid):
            break
#    print()

    return grid

def is_finished(grid):
    seen_e = False
    seen_g = False
    for kind, _ in grid.values():
        if kind == 'E':
            seen_e = True
        if kind == 'G':
            seen_g = True
    return not (seen_e and seen_g)

def remaining_lives(grid):
    return sum(
        life for kind, life in grid.values()
        if kind in 'EG'
    )


def play(grid, elf_attack=None):
    i = 0
    while True:
        grid = iterate(grid, i, elf_attack)
        if is_finished(grid):
            break
        i += 1

    lives = remaining_lives(grid)
    output = i * lives
    return output

file = 'input.txt'

grid = parse(file)

print('Part 1:', play(grid))
elf_attack = 0
while True:
    elf_attack += 1
    try:
        grid = parse(file)
        outcome = play(grid, elf_attack)
    except ElfDied:
        continue
    break
print('Part 2:', outcome)
