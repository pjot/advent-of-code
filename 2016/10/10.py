from collections import defaultdict


instructions = []
with open('input') as f:
    for l in f.readlines():
        instructions.append(l.strip())


def bot():
    return {
        'hi': None,
        'lo': None,
        'chips': [],
    }


bots = defaultdict(bot)
outputs = {}
for i in instructions:
    p = i.split(' ')
    if i.startswith('value'):
        a = int(p[1])
        b = int(p[5])
        bots[b]['chips'].append(a)
    if i.startswith('bot'):
        b = int(p[1])
        bots[b]['lo'] = (p[5], int(p[6]))
        bots[b]['hi'] = (p[10], int(p[11]))

while any([len(b['chips']) == 2 for b in bots.values()]):
    for b in bots:
        bot = bots[b]
        if 61 in bot['chips'] and 17 in bot['chips']:
            print('Part 1:', b)
        if len(bot['chips']) == 2:
            hi_l, hi = bot['hi']
            lo_l, lo = bot['lo']
            if hi_l == 'bot':
                bots[hi]['chips'].append(max(bot['chips']))
            else:
                outputs[hi] = max(bot['chips'])

            if lo_l == 'bot':
                bots[lo]['chips'].append(min(bot['chips']))
            else:
                outputs[lo] = min(bot['chips'])

            bots[b]['chips'] = []
            continue

print('Part 2:', outputs[0] * outputs[1] * outputs[2])