Key = list[int]
Lock = list[int]

def parse(file: str) -> tuple[list[Key], list[Lock]]:
    locks = []
    keys = []
    with open("input") as f:
        for item in f.read().split("\n\n"):
            lines = item.strip().splitlines()

            thing = [0, 0, 0, 0, 0]
            for line in lines[1:-1]:
                for i, c in enumerate(line):
                    if c == "#":
                        thing[i] += 1

            if "#" in lines[0]:
                locks.append(thing)
            else:
                keys.append(thing)
    return keys, locks

def matches(key: Key, lock: Lock) -> int:
    for k, l in zip(key, lock):
        if k + l > 5:
            return 0
    return 1

keys, locks = parse("input")

fits = 0
for key in keys:
    for lock in locks:
        fits += matches(key, lock)

print("Part 1:", fits)
