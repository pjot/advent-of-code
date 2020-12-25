def transform(subject, loop_size):
    n = subject
    for _ in range(loop_size - 1):
        n = (n * subject) % 20201227
    return n

def loop_size(key):
    l = 1
    start = 1
    while True:
        current = start * 7 % 20201227
        if current == key:
            return l
        start = current
        l += 1
    

card_key = 1526110
door_key = 20175123

card_loop = loop_size(card_key)
door_loop = loop_size(door_key)

print('Part 1:', transform(door_key, card_loop))
