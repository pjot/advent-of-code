def parse(file):
    numbers = []
    boards = []
    with open(file) as f:
        numbers = [int(n) for n in f.readline().split(',')]
        while True:
            f.readline()
            board = {}
            for y in range(5):
                line = f.readline().strip()
                if line == '':
                    return numbers, boards
                row = [int(n) for n in line.split()]
                for x in range(5):
                    board[(x, y)] = row[x]
            boards.append(board)

def is_bingo(line):
    return line == ['X', 'X', 'X', 'X', 'X']

def winner(b):
    for x in range(5):
        rows = [b[x, 0], b[x, 1], b[x, 2], b[x, 3], b[x, 4]]
        columns = [b[0, x], b[1, x], b[2, x], b[3, x], b[4, x]]
        if is_bingo(rows) or is_bingo(columns):
            return b

def score(board, n):
    return sum(b for b in board.values() if b != 'X') * n

def mark(board, n):
    for k in board.keys():
        if board[k] == n:
            board[k] = 'X'
    return board

def one(numbers, boards):
    for n in numbers:
        for board in boards:
            mark(board, n)
            if winner(board):
                return score(board, n)

def two(numbers, boards):
    for n in numbers:
        for board in boards:
            mark(board, n)

        if len(boards) == 1 and winner(boards[0]):
            return score(board, n)

        boards = [b for b in boards if not winner(b)]

numbers, boards = parse('input.txt')
print('Part 1:', one(numbers, boards))
print('Part 2:', two(numbers, boards))
