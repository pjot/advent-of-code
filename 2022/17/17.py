def parse(file):
    with open(file) as f:
        return f.readlines()[0].strip()

def add(point, delta):
    px, py = point
    dx, dy = delta
    return px+dx, py+dy

def move(shape, delta):
    return [add(s, delta) for s in shape]

def top(stuck):
    if not stuck:
        return 0
    return max([y for x, y in stuck]) + 1

def can_move(shape, delta, stuck):
    shape = move(shape, delta)
    for point in shape:
        sx, sy = point

        if sx < 0:
            return False
        if sx > 6:
            return False
        if sy < 0:
            return False

        if point in stuck:
            return False
    return True

def iterate(stuck, shape, moves, current):
    while True:
        if current == len(moves):
            current = 0
        m = moves[current]
        current += 1

        if m == ">":
            dx = 1
        elif m == "<":
            dx = -1

        if can_move(shape, (dx, 0), stuck):
            shape = move(shape, (dx, 0))

        if can_move(shape, (0, -1), stuck):
            shape = move(shape, (0, -1))
        else:
            return stuck | set(shape), current

def prune_bottom(stuck):
    lowest = top(stuck) - 25
    return { s for s in stuck if s[1] > lowest }

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

moves = parse("input.txt")
stuck = set()

move_count = len(moves)
big_number = 1000000000000

i = 0
current = 0
while i < big_number:
    shape = shapes[i % 5]
    i += 1
    start = (2, top(stuck) + 3)
    shape = move(shape, start)

    stuck, current = iterate(stuck, shape, moves, current)

    # keep the stuck parts small-ish
    if i % 50 == 0 and i > 0:
        stuck = prune_bottom(stuck)

    # part 1
    if i == 2022:
        print("Part 1:", top(stuck))

    # start looking for cycle - trial and error to find 5000
    elif i == 5000:
        start_i = i
        start_current = current
        start_top = top(stuck)

    # check if we've found a cycle
    elif i > 5000:
        same_i = i % 5 == start_i % 5
        same_current = current % move_count == start_current

        if same_i and same_current:
            cycle_length = i - start_i
            top_diff_per_cycle = top(stuck) - start_top

            remaining_cycles = (big_number - i) // cycle_length

            # warp to i close to big number
            i += remaining_cycles * cycle_length

            # move all stuck up
            delta_y = remaining_cycles * top_diff_per_cycle
            stuck = set(move(stuck, (0, delta_y)))

print("Part 2:", top(stuck))

