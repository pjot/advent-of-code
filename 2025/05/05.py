def parse(file):
    ingredients = []
    fresh = []
    with open(file) as f:
        i, j = f.read().split("\n\n")
        for line in i.splitlines():
            a, b = line.split("-")
            fresh.append((int(a), int(b)))

        for line in j.splitlines():
            line = line.strip()
            ingredients.append(int(line))
    return ingredients, fresh


def in_range(n, ranges):
    for a, b in ranges:
        if a <= n <= b:
            return True
    return False


def merge_ranges(ranges):
    ranges = sorted(ranges)
    out = [ranges.pop(0)]
    while ranges:
        a, b = ranges.pop(0)
        if a <= out[-1][1]:
            out[-1] = (out[-1][0], max(b, out[-1][1]))
        else:
            out.append((a, b))
    return out


def count(ranges):
    cnt = 0
    for a, b in ranges:
        cnt += b - a + 1
    return cnt


ingredients, fresh = parse("input")
fresh_count = 0
for i in ingredients:
    if in_range(i, fresh):
        fresh_count += 1
print("Part 1:", fresh_count)
print("Part 2:", count(merge_ranges(fresh)))
