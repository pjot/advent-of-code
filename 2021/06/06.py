from collections import defaultdict

def parse(file):
    state = defaultdict(int)
    with open(file) as f:
        fishes = [int(i) for i in f.readline().strip().split(',')]

    for f in fishes:
        state[f] += 1

    return state

def iterate(fishes):
    new_state = defaultdict(int)
    for k, v in fishes.items():
        if k == 0:
            new_state[6] += v
            new_state[8] += v
        else:
            new_state[k - 1] += v
    return new_state

def count(fishes):
    return sum(v for v in fishes.values())

fishes = parse('input.txt')

for d in range(256):
    if d == 80:
        print("Part 1:", count(fishes))
    fishes = iterate(fishes)

print("Part 2:", count(fishes))
