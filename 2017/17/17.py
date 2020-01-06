from collections import deque


def run(n):
    steps = 301
    ring = deque([0])
    for i in range(1, n):
        ring.rotate(-steps)
        ring.append(i)
    return ring


ring = run(2018)
print('Part 1:', ring[0])


ring = run(50000000)
p = ring.index(0)
print('Part 2:', ring[p + 1])