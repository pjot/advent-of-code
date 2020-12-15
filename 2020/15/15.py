def iterate(ns, until):
    said = {n: t for t, n in enumerate(ns)}
    turn = len(ns)
    last = ns.pop()

    while turn < until:
        if last in said:
            said[last], last = turn - 1, turn - said[last] - 1
        else:
            said[last] = turn - 1
            last = 0
        turn += 1

    return last

print('Part 1:', iterate([0, 6, 1, 7, 2, 19, 20], 2020))
print('Part 2:', iterate([0, 6, 1, 7, 2, 19, 20], 30000000))
