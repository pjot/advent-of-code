from collections import defaultdict

def parse(file: str) -> list[int]:
    secrets = []
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                secrets.append(int(line))
    return secrets

def next_number(n: int) -> int:
    p = 2 ** 24
    n = n ^ (n * 2 ** 6) % p
    n = n ^ (n // 2 ** 5) % p
    return n ^ (n * 2 ** 11) % p

def last_digit(n: int) -> int:
    return int(str(n)[-1])

changes = defaultdict(int)
one = 0
with open("input") as f:
    for line in f.readlines():
        seen = set()

        line = line.strip()
        if not line:
            continue

        s = int(line)
        values = [s]
        for i in range(2000):
            s = next_number(s)
            values.append(last_digit(s))

            if len(values) > 5:
                a, b, c, d, e = values[-5:]
                change = (b - a, c - b, d - c, e - d)
                if not change in seen:
                    changes[change] += e
                seen.add(change)

        one += s

print("Part 1:", one)
print("Part 2:", max(changes.values()))
