import functools

def parse(file):
    rows = []
    with open(file) as f:
        for line in f.readlines():
            conditions, groups = line.split()
            groups = [int(g) for g in groups.split(",")]
            rows.append((conditions, tuple(groups)))
    return rows

def could_match(condition, candidate):
    for p, c in zip(condition, candidate):
        if p not in {c, "?"}:
            return False
    return True

@functools.lru_cache(maxsize=None)
def matches(condition, groups):
    if not groups:
        if "#" in condition:
            return 0
        return 1

    count = 0
    max_dots = len(condition) - sum(groups) - len(groups) + 2
    end = "#" * groups[0] + "."

    for dots in range(max_dots):
        possible = "." * dots + end

        if could_match(condition, possible):
            count += matches(
                condition[len(possible):],
                groups[1:]
            )

    return count

def one(rows):
    return sum(matches(p, g) for p, g in rows)

def two(data):
    s = 0
    for condition, groups in rows:
        p = "?".join([condition] * 5)
        s += matches(p, groups * 5)

    return s

rows = parse("input")
print("Part 1:", one(rows))
print("Part 2:", two(rows))
