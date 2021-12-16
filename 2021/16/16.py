import functools

def hex_to_bin(h):
    return ''.join(
        str(bin(int(c, 16))).replace('0b', '').zfill(4)
        for c in h
    )

def pop(b, n):
    return b[:n], b[n:]

def pop_int(b, n):
    return int(b[:n], 2), b[n:]

def parse(b):
    version, b = pop_int(b, 3)
    type_id, b = pop_int(b, 3)

    if type_id == 4:
        values = ''
        while b[0] == '1':
            v, b = pop(b, 5)
            values += v[1:]
        v, b = pop(b, 5)
        values += v[1:]
        value = int(values, 2)
        return ('VAL', (version, type_id, value)), b

    else:
        length_type, b = pop_int(b, 1)

        if length_type == 0:
            length, b = pop_int(b, 15)
            inner_b, b = pop(b, length)
            subpackets = []
            while len(inner_b) and '1' in inner_b:
                packet, inner_b = parse(inner_b)
                subpackets.append(packet)
            return ('OP', (version, type_id, subpackets)), b

        elif length_type == 1:
            subpacket_count, b = pop_int(b, 11)
            subpackets = []
            for i in range(subpacket_count):
                packets, b = parse(b)
                subpackets.append(packets)
            return ('OP', (version, type_id, subpackets)), b

def operate(p):
    k, v = p
    if k == 'VAL':
        _, __, value = v
        return value

    _, type_id, subpackets = v
    subs = [operate(p) for p in subpackets]
    if type_id == 0:
        return sum(subs)
    if type_id == 1:
        return functools.reduce(lambda a, b: a * b, subs)
    if type_id == 2:
        return min(subs)
    if type_id == 3:
        return max(subs)
    if type_id == 5:
        return 1 if subs[0] > subs[1] else 0
    if type_id == 6:
        return 1 if subs[0] < subs[1] else 0
    if type_id == 7:
        return 1 if subs[0] == subs[1] else 0

def versions(p):
    k, v = p
    if k == 'OP':
        version, __, subs = v
        return version + sum(versions(s) for s in subs)
    if k == 'VAL':
        version, _, _ = v
        return version

with open('input.txt') as f:
    s = f.readline().strip()

s = hex_to_bin(s)
p, _ = parse(s)
print("Part 1:", versions(p))
print("Part 2:", operate(p))
