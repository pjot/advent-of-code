from collections import defaultdict


def parse(file):
    dependencies = []
    with open(file) as f:
        for line in f.readlines():
            p = line.strip().split(' ')
            dependencies.append((p[1], p[7]))
    return dependencies

def possible(dependencies, letters):
    p = []
    for l in letters:
        can_use = all(
            b != l for _, b in dependencies
        )
        if can_use:
            p.append(l)
    return p

def duration(l):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(l) + 60

def word(deps):
    w = ''
    letters = set(
        [d[0] for d in deps] +
        [d[1] for d in deps]    
    )
    while letters:
        poss = possible(deps, letters)
        poss.sort()
        n = poss[0]
        w += n
        letters.remove(n)
        deps = [
            (a, b) for a, b in deps
            if a != n
        ]
    return w

def time(deps):
    t = 0
    letters = set(
        [d[0] for d in deps] +
        [d[1] for d in deps]    
    )
    cnt = 5
    workers = [0] * cnt
    working_on = [None] * cnt
    while letters or any(w > 0 for w in workers):
        poss = possible(deps, letters)
        poss.sort()
        for i in range(cnt):
            if workers[i] > 0:
                workers[i] -= 1

            if workers[i] == 0:
                if working_on[i] is not None:
                    deps = [
                        (a, b) for a, b in deps
                        if a != working_on[i]
                    ]
                if poss:
                    n = poss.pop(0)
                    workers[i] = duration(n)
                    working_on[i] = n
                    letters.remove(n)
        t += 1
    return t

dependencies = parse('input')

print('Part 1:', word(dependencies[:]))
print('Part 2:', time(dependencies[:]))