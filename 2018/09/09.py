from collections import deque, defaultdict


def play(players, rounds):
    scores = defaultdict(int)
    marbles = deque([0])
    for m in range(1, 1 + rounds):
        if m % 23 == 0:
            p = m % players
            marbles.rotate(7)
            scores[p] += m + marbles.pop()
            marbles.rotate(-1)
            continue
        marbles.rotate(-1)
        marbles.append(m)
    return max(scores.values())

print('Part 1:', play(419, 72164))
print('Part 2:', play(419, 72164*100))