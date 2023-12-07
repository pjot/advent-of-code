from collections import Counter
from functools import cmp_to_key

def parse(file):
    with open(file) as f:
        hands = []
        for line in f.readlines():
            hand, bid = line.split()
            hands.append((hand, int(bid)))
    return hands

def value_one(card):
    return "23456789TJQKA".index(card)

def rank_one(cards):
    values = sorted(Counter(cards).values(), reverse=True)

    match values:
        case [1, 1, 1, 1, 1]:
            return 1
        case [2, 1, 1, 1]:
            return 2
        case [2, 2, 1]:
            return 3
        case [3, 1, 1]:
            return 4
        case [3, 2]:
            return 5
        case [4, 1]:
            return 6
        case [5]:
            return 7

def value_two(card):
    return "J23456789TJQKA".index(card)

def rank_two(hand):
    highest = 0
    for c in "AKQT98765432":
        h = hand.replace("J", c)
        highest = max(highest, rank_one(h))

    return highest

def sort_using(hands, rank, value):
    def compare(a, b):
        a, b = a[0], b[0]
        r = rank(a) - rank(b)

        if r != 0:
            return r

        for card_a, card_b in zip(a, b):
            if card_a == card_b:
                continue
            return value(card_a) - value(card_b)

    return sorted(hands, key=cmp_to_key(compare))

def winnings(hands):
    per_hand = []
    for ranking, (_, bid) in enumerate(hands):
        per_hand.append((ranking + 1) * bid)
    return sum(per_hand)

hands = parse("input")
one = sort_using(hands, rank_one, value_one)
two = sort_using(hands, rank_two, value_two)

print("Part 1:", winnings(one))
print("Part 2:", winnings(two))
