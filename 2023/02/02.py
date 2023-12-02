games = []
with open("input") as f:
    for line in f.readlines():
        p = line.split()
        game = int(p[1].replace(":", ""))

        results = " ".join(p[2:])
        rounds = []
        for s in results.split(";"):
            r = {"r": 0, "g": 0, "b": 0}

            for cube in s.split(","):
                n, color = cube.split()
                r[color[0]] = int(n)

            rounds.append((r["r"], r["g"], r["b"]))

        games.append((game, rounds))

def possible(rounds):
    for red, green, blue in rounds:
        if red > 12 or green > 13 or blue > 14:
            return False

    return True

def fewest(rounds):
    r = g = b = 0
    for red, green, blue in rounds:
        r = max(r, red)
        g = max(g, green)
        b = max(b, blue)

    return r * g * b

one = two = 0
for game, rounds in games:
    if possible(rounds):
        one += game

    two += fewest(rounds)

print("Part 1:", one)
print("Part 2:", two)
