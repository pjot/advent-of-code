def bin16(n):
    return n & 0xFFFF


class Gen:
    def __init__(self, seed, n, multiple=0):
        self.seed = seed
        self.n = n
        self.multiple = multiple

    def one(self):
        self.seed = (self.seed * self.n) % 2147483647
        return self.seed
    
    def two(self):
        while True:
            n = self.one()
            if n % self.multiple == 0:
                return n


a = Gen(289, 16807)
b = Gen(629, 48271)

same = 0
for i in range(40000000):
    if bin16(a.one()) == bin16(b.one()):
        same += 1
print('Part 1:', same)


a = Gen(289, 16807, 4)
b = Gen(629, 48271, 8)
same = 0
for i in range(5000000):
    if bin16(a.two()) == bin16(b.two()):
        same += 1
print('Part 2:', same)
