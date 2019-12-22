def deck_of_size(n):
    return list(range(n))


def deal_into_stack(deck):
    return list(reversed(deck))


def cut_to_n(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    size = len(deck)
    new = [0] * size
    pos = 0
    for c in deck:
        new[pos] = c
        pos = (pos + n) % size
    return new


def parse_file(file):
    instructions = []
    with open(file) as f:
        for line in f.readlines():
            if line.startswith('cut'):
                n = int(line.strip().split(' ').pop())
                instructions.append(('CUT', n))
            if line.startswith('deal with'):
                n = int(line.strip().split(' ').pop())
                instructions.append(('DEAL_WITH', n))
            if line.startswith('deal into'):
                instructions.append(('DEAL_INTO', None))
    return instructions


def perform(instructions, deck):
    for kind, n in instructions:
        if kind == 'CUT':
            deck = cut_to_n(deck, n)
        if kind == 'DEAL_WITH':
            deck = deal_with_increment(deck, n)
        if kind == 'DEAL_INTO':
            deck = deal_into_stack(deck)
    return deck


instructions = parse_file('input.txt')
d = deck_of_size(10007)
d = perform(instructions, d)
print('Part 1:', d.index(2019))