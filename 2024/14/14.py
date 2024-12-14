HEIGHT = 103
WIDTH = 101

Point = tuple[int, int]
Robot = tuple[Point, Point]

def parse(file: str) -> list[Robot]:
    robots = []
    with open("input") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            pp, vv = line.split()
            p = [int(n) for n in pp.split("=")[1].split(",")]
            v = [int(n) for n in vv.split("=")[1].split(",")]
            robots.append((
                (p[0], p[1]),
                (v[0], v[1]),
            ))
    return robots

def move(r: Robot) -> Robot:
    p, v = r

    x, y = p
    vx, vy = v

    x += vx
    y += vy

    x = x % WIDTH
    y = y % HEIGHT

    return (x, y), v

def safety_factor(robots: list[Robot]) -> int:
    a = b = c = d = 0
    y_mid = (HEIGHT - 1) // 2
    x_mid = (WIDTH - 1) // 2

    for p, _ in robots:
        x, y = p
        if x < x_mid and y < y_mid:
            a += 1
        if x < x_mid and y > y_mid:
            b += 1
        if x > x_mid and y < y_mid:
            c += 1
        if x > x_mid and y > y_mid:
            d += 1

    return a * b * c * d

def is_tree(robots: list[Robot]) -> bool:
    x = y = 0
    for p, _ in robots:
        if p[0] == 34:
            x += 1
        if p[1] == 32:
            y += 1

    return x + y > 50

robots = parse("input")
for n in range(1, 10000):
    robots = [move(r) for r in robots]
    if n == 100:
        print("Part 1:", safety_factor(robots))
    if is_tree(robots):
        print("Part 2:", n)
        break
