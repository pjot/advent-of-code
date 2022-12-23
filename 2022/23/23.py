from collections import defaultdict, deque

def parse(file):
    elves = set()
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    elves.add((x, y))
    return elves

def count_empty(elves):
    xs = [e[0] for e in elves]
    ys = [e[1] for e in elves]
    dx = 1 + max(xs) - min(xs)
    dy = 1 + max(ys) - min(ys)
    return dx * dy - len(elves)

def neighbours(p, direction):
    x, y = p
    match direction:
        case "N": return {(x-1, y-1), (x, y-1), (x+1, y-1)}
        case "S": return {(x-1, y+1), (x, y+1), (x+1, y+1)}
        case "W": return {(x-1, y-1), (x-1, y), (x-1, y+1)}
        case "E": return {(x+1, y-1), (x+1, y), (x+1, y+1)}

def all_neighbours(p):
    x, y = p
    return {
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    }

def move(p, direction):
    x, y = p
    match direction:
        case "N": return x, y-1
        case "S": return x, y+1
        case "W": return x-1, y
        case "E": return x+1, y

elves = parse("input.txt")
directions = deque(["N", "S", "W", "E"])
current_round = 0
while True:
    current_round += 1

    props = defaultdict(set)
    for p in elves:
        if all_neighbours(p).isdisjoint(elves):
            continue

        for direction in directions:
            if neighbours(p, direction).isdisjoint(elves):
                props[move(p, direction)].add(p)
                break

    changes = [
        (old, new) for new, old in props.items() if len(old) == 1
    ]
    if not changes:
        break
    for old, new in changes:
        elves -= old
        elves.add(new)

    directions.rotate(-1)

    if current_round == 10:
        print("Part 1:", count_empty(elves))

print("Part 2:", current_round)
