codes = []
with open("input") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            codes.append(line)

numeric_keypad = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
                 "0": (1, 3), "A": (2, 3),
}

directional_keypad = {
                 "^": (1, 0), "A": (2, 0),
    "<": (0, 1), "v": (1, 1), ">": (2, 1),
}

def travel(a, b, keypad):
    ax, ay = keypad[a]
    bx, by = keypad[b]

    dx = bx - ax
    dy = by - ay

    return dx, dy

def direction_travel(dx, dy):
    moves = ""
    if dx < 0:
        moves += "<" * abs(dx)
    if dy > 0:
        moves += "v" * dy
    if dx > 0:
        moves += ">" * dx
    if dy < 0:
        moves += "^" * abs(dy)
    return moves

def move(x, y, d):
    if d == "<":
        return x - 1, y
    if d == ">":
        return x + 1, y
    if d == "^":
        return x, y - 1
    if d == "v":
        return x, y + 1

def moves_to_moves(moves):
    code = moves
    curr = "A"
    all_moves = ""
    for c in code:
        de = travel(curr, c, directional_keypad)
        if curr == "<" and c == "^":
            m = ">^"
        elif curr == "^" and c == "<":
            m = "v<"
        else:
            m = direction_travel(*de)
        all_moves += m + "A"
        curr = c
    return all_moves

def code_to_moves(code):
    curr = "A"
    all_moves = ""
    for c in code:
        de = travel(curr, c, numeric_keypad)
        if curr in "0A" and c in "147":
            dx, dy = de
            moves = abs(dy) * "^" + abs(dx) * "<"
        elif curr in "147" and c in "0A":
            dx, dy = de
            moves = abs(dx) * ">" + abs(dy) * "v"
        else:
            moves = direction_travel(*de)
        all_moves += moves + "A"
        curr = c
    return all_moves

def numbers(code):
    n = ""
    for c in code:
        if c in "1234567890":
            n += c
    return int(n)

def resolve(code):
    numeric = numbers(code)

    moves = code_to_moves(code)
    moves = moves_to_moves(moves)
    moves = moves_to_moves(moves)
    return len(moves), numeric

s = 0
for code in codes:
    a, b = resolve(code)
    s += a * b

print("Part 1:", s)
