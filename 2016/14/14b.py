import hashlib


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


def triplet(s):
    s = {
        i: c for i, c in enumerate(s)
    }
    for i in range(len(s)):
        a = s.get(i, 'r')
        b = s.get(i+1, 't')
        c = s.get(i+2, 's')
        if a == b and b == c:
            return b
    return False


def quintuple(s):
    for i in range(len(s) - 4):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        d = s[i+3]
        e = s[i+4]
        if a == b and b == c and c == d and d == e:
            return a
    return False


def index_of_64(salt):
    i = 0
    keys = set()
    candidates = {}
    while True:
        hash = md5(salt + str(i))
        t = triplet(hash)
        if i == 39:
            print(hash, t)
        if t:
            candidates[i] = t
        q = quintuple(hash)
        if q:
            for c, t in candidates.items():
                if 0 <= i - c <= 1000 and t == q and i != c:
                    if c not in keys:
                        print('found', len(keys) + 1, c, md5(salt + str(c)), hash)
                    keys.add(c)
                    if len(keys) > 70:
                        return
        i += 1

        


salt = 'yjdafjpo'
#salt = 'abc'
index_of_64(salt)
#print('Part 1:', index_of_64(salt))
#print(triplets('asdhgdksjhgdrrralskjdh'))