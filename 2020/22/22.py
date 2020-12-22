from collections import deque
from copy import copy
from functools import lru_cache

def parse():
    with open('input.txt') as f:
        decks = {
            1: deque(),
            2: deque(),
        }

        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue

            if line.startswith('Player 1'):
                deck = 1
                continue

            if line.startswith('Player 2'):
                deck = 2
                continue
            
            decks[deck].append(int(line))

    return decks[1], decks[2]

def round(deck_1, deck_2):
    card_1 = deck_1.popleft()
    card_2 = deck_2.popleft()

    if card_1 > card_2:
        deck_1.append(card_1)
        deck_1.append(card_2)
    else:
        deck_2.append(card_2)
        deck_2.append(card_1)

    return deck_1, deck_2

def score(cards):
    s = 0
    for i, card in enumerate(reversed(cards)):
        s += (i + 1) * card
    return s

def pick(deck, n):
    old_deck = copy(deck)
    new_deck = deque()
    for _ in range(n):
        new_deck.append(old_deck.popleft())
    return new_deck

def recursive_round(deck_1, deck_2):
    card_1 = deck_1.popleft()
    card_2 = deck_2.popleft()

    if card_1 <= len(deck_1) and card_2 <= len(deck_2):
        _, winner = game(
            pick(deck_1, card_1),
            pick(deck_2, card_2),
        )
        if winner == 1:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    elif card_1 > card_2:
        deck_1.append(card_1)
        deck_1.append(card_2)
    else:
        deck_2.append(card_2)
        deck_2.append(card_1)

    return deck_1, deck_2

def game(deck_1, deck_2):
    seen = set()
    while deck_1 and deck_2:
        state = tuple(deck_1), tuple(deck_2)
        if state in seen:
            return deck_1, 1

        deck_1, deck_2 = recursive_round(deck_1, deck_2)

        seen.add(state)

    if deck_1:
        return deck_1, 1
    else:
        return deck_2, 2

deck_1, deck_2 = parse()
while deck_1 and deck_2:
    deck_1, deck_2 = round(deck_1, deck_2)

print('Part 1:', score(deck_1) + score(deck_2))

deck_1, deck_2 = parse()
winning_deck, _ = game(deck_1, deck_2)

print('Part 2:', score(winning_deck))
