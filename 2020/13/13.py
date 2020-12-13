with open('input.txt') as f:
    lines = f.readlines()
    time = int(lines[0])
    buses = [
        (int(l), i) for i, l in
        enumerate(lines[1].strip().split(',')) if l != 'x'
    ]

def next_bus(time, buses):
    for t in range(time, time+1000):
        for b, _ in buses:
            if t % b == 0:
                return b * (t - time)

'''
x % 17 = 0
x % 13 = 13 - 2
x % 19 = 19 - 3

x % 13 = 17n - 2 -> step = 17 -> find x'
x % 19 = x'm - 3 -> step = x' -> find x''
etc
'''
def first_consecutive(buses):
    ans = 1
    step = 1
    for bus, d in buses:
        x = ans
        diff = (bus - d) % bus
        while True:
            if x % bus == diff:
                step *= bus
                ans = x
                break
            x += step
    return ans

print('Part 1:', next_bus(time, buses))
print('Part 2:', first_consecutive(buses))
