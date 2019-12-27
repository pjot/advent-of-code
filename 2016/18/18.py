def next_row(row):
    n = ''
    r = {i: c for i, c in enumerate(row)}
    for i in range(len(row)):
        a = r.get(i - 1, '.')
        b = r.get(i, '.')
        c = r.get(i + 1, '.')
        abc = a + b + c
        if abc in ['^^.', '.^^', '^..', '..^']:
            n += '^'
        else:
            n += '.'
    return n


def safe_tiles(row, rows):
    safe = row.count('.')
    for i in range(rows - 1):
        row = next_row(row)
        safe += row.count('.')
    return safe


r = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
print('Part 1:', safe_tiles(r, 40))
print('Part 2:', safe_tiles(r, 400000))

