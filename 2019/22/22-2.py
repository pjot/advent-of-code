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


def mod_inv(x, p):
    # googled mod inverse
    return pow(x, p-2, p)


def apply(instructions, a, b, size):
    for kind, n in instructions:
        # These can all be written as f(x) = ax + b (mod size)
        # but we will want the reverse
        if kind == 'CUT':
            # x' = x + n
            # applied in ax + b:
            # x = a(x' + n) + b = ax' + b + n
            # a' = a, b' = b + n
            b = b + n
        if kind == 'DEAL_WITH':
            # Most complicated!!
            # x' = n * x
            # want to do x = x' / n, googled to realize I need mod inverse.
            # if a = b * c (mod m) then a * mod_inv(b, m) = c (mod m)
            # x = x' * inv_mod(n, size)
            # x = (ax + b) * im(n, s) = ax * im(n, s) + b * im(n, s)
            # a' = a * im(n, s), b' = b * im(n ,s)
            a = mod_inv(n, size) * a
            b = mod_inv(n, size) * b
        if kind == 'DEAL_INTO':
            # reverse deck
            # x' = -x - 1
            # applied in ax + b:
            # x = a(-x - 1) + b = -ax + b - 1
            # a' = -a, b' = b - 1
            a = size - a
            b = size - b - 1
    return a % size, b % size


instructions = parse_file('input.txt')
cards = 119315717514047
n = 101741582076661

a, b = apply(
    reversed(instructions),
    1,
    0,
    cards
)

# Want to apply a, b #n times, which isnt doable
# However:
# f(x) = ax + b
# f(f(x)) = a(ax + b) + b = a^2x + ab + b
# f(f(f(x))) = a^2(ax + b) + ab + b = a^3x + a^2b + ab + b = a^3x + b(a^2 + a + 1)
# in general:
# f^n(x) = a^n * x + b * (a^0 + a^1 + a^2 ... a^n-1)
# where that sum is (a^n - 1) / (a - 1),
# although we still can't divide so we have to use mod_inv again
# meaning sum = (a^n - 1) * mod_inv(a - 1, #cards)

a_pow_n = pow(a, n, cards)
b_sum = (a_pow_n - 1) * mod_inv(a - 1, cards)

# f^n(2020) tells us where card 2020 came from (since we ran all this backwards)
original_card = (a_pow_n * 2020 + b * b_sum) % cards

print('Part 2:', original_card)