def parse(file):
    grid = {}
    path = []
    start = None

    with open(file) as f:
        maze, raw_path = f.read().split("\n\n")

    for y, line in enumerate(maze.splitlines()):
        for x, c in enumerate(line):
            if c != " ":
                if start is None:
                    start = x+1, y+1
                grid[x+1, y+1] = c

    curr = ""
    for c in raw_path:
        if c in {"L", "R"}:
            path.append(int(curr))
            path.append(c)
            curr = ""
        else:
            curr += c
    path.append(int(curr))

    return grid, start, path

grid, start, path = parse("input.txt")

xs = [p[0] for p in grid]
ys = [p[1] for p in grid]

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

def step(me, direction):
    x, y = me
    match direction:
        case ">": p = x + 1, y
        case "<": p = x - 1, y
        case "^": p = x, y - 1
        case "v": p = x, y + 1
    return p

def square(p):
    x, y = p
    if x > 100:
        return 2
    if y < 51:
        return 1
    if y < 101:
        return 3
    if x > 50:
        return 5
    if y < 151:
        return 4
    return 6

def topleft(square):
    match square:
        case 1:
            return 50, 0
        case 2:
            return 100, 0
        case 3:
            return 50, 50
        case 4:
            return 0, 100
        case 5:
            return 50, 100
        case 6:
            return 0, 150

def flip_x(p):
    x, y = p
    tl, _ = topleft(square(p))
    x = 2 * tl + 51 - x
    return x, y

def flip_y(p):
    x, y = p
    _, tl = topleft(square(p))
    y = 2 * tl + 51 - y
    return x, y

def cw(p):
    if p == (1, 1):
        return 50, 1
    elif p == (50, 1):
        return 50, 50
    elif p == (50, 50):
        return 1, 50
    elif p == (1, 50):
        return 1, 1

    x, y = p
    if y == 1:
        y = x
        x = 50
    elif y == 50:
        y = x
        x = 1
    elif x == 1:
        x = 51 - y
        y = 1
    elif x == 50:
        x = 51 - y
        y = 50
    return x, y

def ccw(p):
    return cw(cw(cw(p)))

def rotate(p, f):
    tl = topleft(square(p))

    p = move_to(p, tl)
    p = f(p)
    p = move_to(p, neg(tl))

    x, y = p
    return int(x), int(y)

def u(p):
    x, y = p
    return x, y - 50

def d(p):
    x, y = p
    return x, y + 50

def l(p):
    x, y = p
    return x - 50, y

def r(p):
    x, y = p
    return x + 50, y

def move_to(p, m):
    xp, yp = p
    xm, ym = m
    return xp - xm, yp - ym

def neg(a):
    x, y = a
    return -x, -y

def teleport_one(p, direction):
    x, y = p
    match direction:
        case ">": p = min_x, y
        case "<": p = max_x, y
        case "^": p = x, max_y
        case "v": p = x, min_y
    while p not in grid:
        p = step(p, direction)
    return p, direction

def teleport_two(p, direction):
    match square(p), direction:
        case 1, "^": # 6 >
            p = d(p)
            p = d(p)
            p = d(p)
            p = l(p)
            p = rotate(p, ccw)
            p = flip_y(p)
            return p, ">"
        case 6, "<": # 1 v
            p = r(p)
            p = u(p)
            p = u(p)
            p = u(p)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "v"

        case 4, "<": # 1 >
            p = u(p)
            p = u(p)
            p = r(p)
            p = flip_y(p)
            return p, ">"
        case 1, "<": # 4 >
            p = d(p)
            p = d(p)
            p = l(p)
            p = flip_y(p)
            return p, ">"

        case 5, "v": # 6 <
            p = d(p)
            p = l(p)
            p = rotate(p, ccw)
            p = flip_y(p)
            return p, "<"
        case 6, ">": # 5 ^
            p = u(p)
            p = r(p)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "^"

        case 4, "^": # 3 >
            p = u(p)
            p = r(p)
            p = rotate(p, ccw)
            p = flip_y(p)
            return p, ">"
        case 3, "<": # 4 v
            p = d(p)
            p = l(p)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "v"

        case 6, "v": # 2 v
            p = u(p)
            p = u(p)
            p = u(p)
            p = r(p)
            p = r(p)
            p = rotate(p, cw)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "v"
        case 2, "^": # 6 ^
            p = d(p)
            p = d(p)
            p = d(p)
            p = l(p)
            p = l(p)
            p = rotate(p, cw)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "^"

        case 2, ">": # 5 <
            p = d(p)
            p = d(p)
            p = l(p)
            p = flip_y(p)
            return p, "<"
        case 5, ">": # 2 <
            p = u(p)
            p = u(p)
            p = r(p)
            p = flip_y(p)
            return p, "<"

        case 3, ">": # 2 ^
            p = u(p)
            p = r(p)
            p = rotate(p, cw)
            p = flip_x(p)
            return p, "^"
        case 2, "v": # 3 <
            p = d(p)
            p = l(p)
            p = rotate(p, ccw)
            p = flip_y(p)
            return p, "<"

def next_point(me, direction, teleport):
    p = step(me, direction)
    if p in grid:
        return p, direction
    else:
        teleported = teleport(me, direction)
        if grid[teleported[0]] == "#":
            return me, direction
        else:
            return teleported

def move(me, direction, steps, teleport):
    for i in range(steps):
        p, new_direction = next_point(me, direction, teleport)
        if grid[p] == "#":
            return me, new_direction
        else:
            me, direction = p, new_direction
    return me, direction

def left(direction):
    match direction:
        case ">": return "^"
        case "^": return "<"
        case "<": return "v"
        case "v": return ">"

def right(direction):
    return left(left(left(direction)))

def password(p, direction):
    x, y = p
    match direction:
        case ">": di = 0
        case "v": di = 1
        case "<": di = 2
        case "^": di = 3
    return 1000 * y + 4 * x + di

def run(path, teleport):
    me = start
    direction = ">"
    while path:
        action = path.pop(0)
        if action == "L":
            direction = left(direction)
        elif action == "R":
            direction = right(direction)
        else:
            me, direction = move(me, direction, action, teleport)

        x, y = me

    return me, direction

path_one = [p for p in path]
path_two = [p for p in path]

p, direction = run(path_one, teleport_one)
print("Part 1:", password(p, direction))

p, direction = run(path_two, teleport_two)
print("Part 2:", password(p, direction))
