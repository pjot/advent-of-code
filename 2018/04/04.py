from collections import defaultdict, Counter


def parse(file):
    guards = defaultdict(int)
    guard_minutes = defaultdict(Counter)
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip())

    lines.sort()
    guard = None
    sleep = 0
    for line in lines:
        p = line.split(' ')
        minutes = int(p[1][:-1].split(':')[1])
        if p[2] == 'Guard':
            guard = int(p[3][1:])
        if p[2] == 'falls':
            sleep = minutes
        if p[2] == 'wakes':
            guards[guard] += minutes - sleep
            for m in range(sleep, minutes):
                guard_minutes[guard][m] += 1
    return guards, guard_minutes

guards, minutes = parse('input')
max_sleep = 0
guard = None
for g, sleep in guards.items():
    if sleep > max_sleep:
        max_sleep = sleep
        guard = g

max_minutes = 0
minute = None
for m, sleep in minutes[guard].items():
    if sleep > max_minutes:
        minute = m
        max_minutes = sleep

print('Part 1:', guard * minute)

ms = 0
mm = 0
gg = None
for g, mins in minutes.items():
    max_sleep = 0
    minute = 0
    for m, sleep in mins.items():
        if sleep > max_sleep:
            max_sleep = sleep
            minute = m

    if max_sleep > ms:
        ms = max_sleep
        mm = minute
        gg = g

print('Part 2:', gg * mm)