from collections import defaultdict
import heapq

def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[x, y] = int(c)
    return grid

def nexts(grid, p, min_step, max_step):
    ns = []
    plus = minus = 0
    x, y, d = p
    if d == 1:
        for i in range(max_step):
            delta = i + 1
            plus += grid.get((x + delta, y), 0)
            minus += grid.get((x - delta, y), 0)

            if delta >= min_step:
                ns.append((x - delta, y, minus))
                ns.append((x + delta, y, plus))

    if d == -1:
        for i in range(max_step):
            delta = i + 1
            plus += grid.get((x, y + delta), 0)
            minus += grid.get((x, y - delta), 0)
            if delta >= min_step:
                ns.append((x, y + delta, plus))
                ns.append((x, y - delta, minus))

    return [
        ((x, y, -d), l) for x, y, l in ns
        if grid.get((x, y))
    ]

def minimum_heat_loss(grid, min_step, max_step):
    candidates = [(0, (0, 0, 1)), (0, (0, 0, -1))]
    heapq.heapify(candidates)
    seen = set()
    xm = max(p[0] for p in grid.keys())
    ym = max(p[1] for p in grid.keys())

    lowest_loss = float("inf")

    while candidates:
        hl, c = heapq.heappop(candidates)
        if c in seen:
            continue
        seen.add(c)

        for candidate, c_hl in nexts(grid, c, min_step, max_step):
            heat_loss = c_hl + hl

            if candidate[0] == xm and candidate[1] == ym:
                lowest_loss = min(lowest_loss, heat_loss)
                continue

            if candidate not in seen and heat_loss < lowest_loss:
                heapq.heappush(candidates, (heat_loss, candidate))

    return lowest_loss

grid = parse("input")

print("Part 1:", minimum_heat_loss(grid, 1, 3))
print("Part 2:", minimum_heat_loss(grid, 4, 10))
