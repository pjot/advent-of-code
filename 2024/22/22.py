import itertools

Change = tuple[int, ...]
Changes = list[dict[Change, int]]

def parse(file: str) -> list[int]:
    secrets = []
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                secrets.append(int(line))
    return secrets

def generate(n: int) -> int:
    b = n * 64
    n ^= b
    n %= 16777216

    c = n // 32
    n ^= c
    n %= 16777216

    d = n * 2048
    n ^= d
    n %= 16777216
    return n

def last_digit(n: int) -> int:
    return int(str(n)[-1])

def changes(secrets: list[int]) -> tuple[Changes, int]:
    changes = []
    one = 0
    for s in secrets:
        values = [s]
        change_value: dict[Change, int] = {}
        for i in range(2000):
            s = generate(s)
            values.append(last_digit(s))
            if len(values) > 5:
                a, b, c, d, e = values[-5:]
                change = (b - a, c - b, d - c, e - d)
                if change_value.get(change) is None:
                    change_value[change] = e
        one += s
        changes.append(change_value)
    return changes, one

def bananas(deltas: Changes) -> int:
    best = 0
    attempts: list[Change] = []
    for attempt in itertools.product(range(-3, 4), repeat=4):
        total = sum(
            d.get(attempt, 0)
            for d in deltas
        )
        best = max(best, total)
    return best

secrets = parse("input")
deltas, one = changes(secrets)

print("Part 1:", one)
print("Part 2:", bananas(deltas))
