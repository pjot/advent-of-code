from heapq import heappop, heappush

INF = float('inf')

def parse(file):
    grid = {}
    end_x, end_y = 0, 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            end_y = max(y, end_y)
            for x, c in enumerate(line.strip()):
                grid[x, y] = int(c)
                end_x = max(x, end_x)
    return grid, (end_x, end_y)

def expand(grid, end):
    new = {k: v for k, v in grid.items()}
    end_x, end_y = end
    end_x += 1
    end_y += 1
    for a in range(5):
        for b in range(5):
            if a == b and a == 0:
                continue
            for x, y in grid.keys():
                v = grid.get((x, y))
                v += a + b
                if v > 9:
                    v = v % 9
                p = (a * end_x + x, b * end_y + y)
                new[p] = v
    return new, (end_x * 5 - 1, end_y * 5 - 1)

def neighbours(grid, p):
    deltas = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    x, y = p
    for dx, dy in deltas:
        pp = (x + dx, y + dy)
        if grid.get(pp):
            yield pp

def lowest_neighbour(g, p):
    ns = [g.get(n, INF) for n in neighbours(g, p)]
    return min(ns) if ns else 0

def solve(grid, end):
    horizon = [(0, (0, 0))]
    seen = set((0, 0))
    costs = {(0, 0): 0}

    while horizon:
        _, h = heappop(horizon)
        seen.add(h)
        for n in neighbours(g, h):
            if n in seen:
                continue

            cost = min(
                costs.get(n, INF),
                g[n] + lowest_neighbour(costs, n)
            )

            costs[n] = cost
            if (cost, n) not in horizon:
                heappush(horizon, (cost, n))

    return costs[end]

g, end = parse('input.txt')
print("Part 1:", solve(g, end))

g, end = expand(g, end)
print("Part 2:", solve(g, end))
