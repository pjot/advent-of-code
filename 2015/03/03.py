with open("input.txt") as f:
    path = f.readline()

deltas = {
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0),
}

s_x, s_y = 0, 0
r_x, r_y = 0, 0
x, y = 0, 0
first_visited = {(0, 0)}
second_visited = {(0, 0)}
for i, c in enumerate(path):
    dx, dy = deltas[c]
    x, y = x + dx, y + dy
    first_visited.add((x, y))

    if i % 2 == 0:
        dx, dy = deltas[c]
        s_x, s_y = s_x + dx, s_y + dy
        second_visited.add((s_x, s_y))
    else:
        dx, dy = deltas[c]
        r_x, r_y = r_x + dx, r_y + dy
        second_visited.add((r_x, r_y))

print("Part 1:", len(first_visited))
print("Part 2:", len(second_visited))