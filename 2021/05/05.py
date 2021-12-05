from collections import defaultdict

def parse(file):
    moves = []
    with open(file) as f:
        for line in f.readlines():
            first, second = line.strip().split(' -> ')
            x1, y1 = first.split(',')
            x2, y2 = second.split(',')
            moves.append(
                (int(x1), int(y1), int(x2), int(y2)),
            )
    return moves

def sign(n):
    if n == 0:
        return 0
    return int(abs(n) / n)

def solve(moves, skip_diagonals=False):
    board = defaultdict(int)

    for x1, y1, x2, y2 in moves:
        if skip_diagonals and x1 != x2 and y1 != y2:
            continue

        x, y = x1, y1
        dx = sign(x2 - x1)
        dy = sign(y2 - y1)

        while x != x2 or y != y2:
            board[(x, y)] += 1
            x += dx
            y += dy
        board[(x, y)] += 1

    return len([v for v in board.values() if v > 1])

moves = parse('input.txt')

print('Part 1:', solve(moves, True))
print('Part 2:', solve(moves, False))
