def part(p):
    lines = p.splitlines()[1:]
    maps = []
    for line in lines:
        dest, source, size = [int(n) for n in line.split()]
        maps.append((source, source + size, dest - source))
    return maps

def parse(file):
    with open("input") as f:
        parts = f.read().split("\n\n")
        seeds = [int(s) for s in parts[0].split(": ")[1].split()]

        transforms = [
            part(parts[p]) for p in range(1, 8)
        ]
        return seeds, transforms

def apply(source, maps):
    for start, finish, offset in maps:
        if start <= source <= finish:
            return source + offset
    return source

def apply_two(sources, maps):
    outputs = set()
    for start, end in sources:
        nexts = set()
        s1, s2 = start, end

        for first, last, offset in maps:
            r1, r2 = first, last

            # r s s r
            if r1 < s1 and s2 < r2:
                # s s
                nexts.add((s1 + offset, s2 + offset))

            # r s r s
            elif r1 < s1 < r2 < s2:
                # s r
                nexts.add((s1 + offset, r2 + offset))
                # r s
                if r2 != s2:
                    nexts.add((r2, s2))

            # s r s r
            elif s1 < r1 < s2 < r2:
                # s r
                if s1 != r1:
                    nexts.add((s1, r1))
                # r s
                nexts.add((r1 + offset, s2 + offset))

            # s r r s
            elif s1 < r1 < r2 < s2:
                # s r
                if s1 != r1:
                    nexts.add((s1, r1))
                # r r
                nexts.add((r1 + offset, r2 + offset))
                # r s
                if r2 != s2:
                    nexts.add((r2, s2))

            # r r s s
            # s s r r
            else:
                pass

        if nexts:
            outputs |= nexts
        else:
            # no overlap, pass along
            outputs.add((start, end))

    return outputs


seeds, transforms = parse("input")
one = float("inf")
for state in seeds:
    for transform in transforms:
        state = apply(state, transform)

    if state < one:
        one = state

two = float("inf")
for i in range(len(seeds) // 2):
    start = seeds[2 * i]
    size = seeds[2 * i + 1]

    state = [(start, start + size)]
    for transform in transforms:
        state = apply_two(state, transform)

    lowest = min(s[0] for s in state)

    if 0 < lowest < two:
        two = lowest

print("Part 1:", one)
print("Part 2:", two)
