'''
s = 67 * 100 + 100000
c = s + 17000

h = 0
for b in range(s, c + 1, 17):
    f = 1
    for d in range(2, b):
        for e in range(2, b):
            if d * e == b:
                f = 0

    if f == 0:
        h += 1
'''

# googled is_prime algorithm
def is_prime(n):
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True

B = 67 * 100 + 100000
c = B + 17000

h = 0
for b in range(B, c + 1, 17):
    if not is_prime(b):
        h += 1

print(h)
