from collections import defaultdict

def parse(file):
    grid = {}
    with open(file) as f:
        for y, row in enumerate(f):
            for x, c in enumerate(row.rstrip()):
                if c == '#':
                    c = ' '
                grid[x, y] = c
    return grid

def neighbours(grid, p):
    x, y = p
    deltas = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    for dx, dy in deltas:
        n = x+dx, y+dy
        v = grid.get(n, ' ')
        if v in '.ABCD':
            yield n, v

def distance(start, end, grid):
    if start == end:
        return 0
    horizon = set([start])
    seen = set()
    steps = 0
    while horizon:
        steps += 1
        new_horizon = set()
        for h in horizon:
            seen.add(h)
            for n, v in neighbours(grid, h):
                if n in seen:
                    continue
                if n == end:
                    return steps
                else:
                    new_horizon.add(n)
        horizon = new_horizon

def perform_move(grid, move):
    start, end = move
    steps = distance(start, end, grid)
    grid[start], grid[end] = '.', grid[start]
    return grid, steps

moves_one = [
    ((5, 2), (1, 1)),
    ((7, 2), (2, 1)),
    ((9, 2), (10, 1)),
    ((7, 3), (4, 1)),
    ((5, 3), (7, 3)),
    ((9, 3), (7, 2)),
    ((4, 1), (5, 3)),
    ((3, 2), (5, 2)),
    ((10, 1), (9, 3)),
    ((3, 3), (9, 2)),
    ((2, 1), (3, 3)),
    ((1, 1), (3, 2)),
]
moves_two = [
    ((7, 2), (11, 1)),
    ((7, 3), (10, 1)),
    ((5, 2), (1, 1)),
    ((7, 4), (2, 1)),
    ((7, 5), (8, 1)),
    ((5, 3), (7, 5)),
    ((5, 4), (4, 1)),
    ((5, 5), (7, 4)),
    ((8, 1), (5, 5)),
    ((10, 1), (5, 4)),
    ((3, 2), (5, 3)),
    ((4, 1), (5, 2)),
    ((9, 2), (6, 1)),
    ((9, 3), (10, 1)),
    ((9, 4), (7, 3)),
    ((9, 5), (7, 2)),
    ((6, 1), (9, 5)),
    ((3, 3), (9, 4)),
    ((3, 4), (9, 3)),
    ((3, 5), (9, 2)),
    ((2, 1), (3, 5)),
    ((10, 1), (3, 4)),
    ((11, 1), (3, 3)),
    ((1, 1), (3, 2)),
]

pod_cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

def solve(grid, moves):
    pod_moves = defaultdict(int)
    for move in moves:
        _, end = move
        grid, steps = perform_move(grid, move)
        pod_moves[grid[end]] += steps

    total_cost = 0
    for k, v in pod_moves.items():
        total_cost += pod_cost[k] * v

    return total_cost

grid = parse('input.txt')
one = solve(grid, moves_one)
print('Part 1:', one)

grid = parse('input2.txt')
two = solve(grid, moves_two)
print('Part 2:', two)
