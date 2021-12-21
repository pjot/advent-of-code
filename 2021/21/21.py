from functools import cache

def parse(file):
    with open(file) as f:
        player_1 = (int(f.readline().strip().split(' ').pop()), 0)
        player_2 = (int(f.readline().strip().split(' ').pop()), 0)
    return player_1, player_2

def die():
    while True:
        for i in range(100):
            yield i + 1

def next_position(position, roll):
    return (position + roll - 1) % 10 + 1

def play(player, d):
    roll = next(d) + next(d) + next(d)

    position, score = player
    position = next_position(position, roll)

    return position, score + position

def one(player_1, player_2):
    d = die()
    casts = 0
    while True:
        player_1 = play(player_1, d)
        casts += 3
        if player_1[1] >= 1000:
            return casts * player_2[1]

        player_2 = play(player_2, d)
        casts += 3
        if player_2[1] >= 1000:
            return casts * player_1[1]

rolls = [
    3, 4, 5,
    4, 5, 6,
    5, 6, 7,
    4, 5, 6,
    5, 6, 7,
    6, 7, 8,
    5, 6, 7,
    6, 7, 8,
    7, 8, 9,
]

@cache
def two(player_1, player_2, turn):
    wins = {
        1: 0,
        2: 0,
    }
    for roll in rolls:
        if turn == 1:
            position, score = player_1
        else:
            position, score = player_2

        position = next_position(position, roll)
        score = score + position
        if score >= 21:
            wins[turn] += 1
        else:
            sub_wins = two(
                (position, score) if turn == 1 else player_1,
                (position, score) if turn == 2 else player_2,
                2 if turn == 1 else 1
            )
            wins[1] += sub_wins[1]
            wins[2] += sub_wins[2]

    return wins

player_1, player_2 = parse('input.txt')

print('Part 1:', one(player_1, player_2))

scores = two(player_1, player_2, 1)
print('Part 2:', max(scores.values()))
