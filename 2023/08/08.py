import math

def parse(file):
    with open(file) as f:
        lines = f.readlines()
        sequence = lines[0].strip()

        directions = {}
        for line in lines[2:]:
            a, _, b, c = line.split()
            directions[a] = {
                "L": b.replace("(", "").replace(",", ""),
                "R": c.replace(")", ""),
            }

    return sequence, directions

def walk(node, sequence, directions, done):
    steps = 0
    while True:
        for s in sequence:
            node = directions[node][s]
            steps += 1
            if done(node):
                return steps

def one(sequence, directions):
    def done(node):
        return node == "ZZZ"

    return walk("AAA", sequence, directions, done)

def two(sequence, directions):
    def done(node):
        return node.endswith("Z")

    def is_start(k):
        return k.endswith("A")

    starts = filter(is_start, directions.keys())

    loops = [
        walk(start, sequence, directions, done)
        for start in starts
    ]

    return math.lcm(*loops)

inputs = parse("input")
print("Part 1:", one(*inputs))
print("Part 2:", two(*inputs))
