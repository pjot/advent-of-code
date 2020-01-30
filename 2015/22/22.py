import random

def possible_actions(mana, active):
    actions = [
        {
            'name': 'm',
            'cost': 53,
            'instant_damage': 4,
        },
        {
            'name': 'd',
            'cost': 73,
            'instant_damage': 2,
            'instant_heal': 2,
        },
        {
            'name': 's',
            'cost': 113,
            'duration': 6,
            'armor': 7,
        },
        {
            'name': 'p',
            'cost': 173,
            'duration': 6,
            'damage': 3,
        },
        {
            'name': 'r',
            'cost': 229,
            'duration': 5,
            'mana': 101,
        },
    ]
    active_names = [a['name'] for a in active]
    return [
        a for a in actions
        if a['cost'] <= mana and a['name'] not in active_names
    ]

def play_round(best, per_round_hp_loss=0):
    p_hp = 50
    p_armor = 0
    p_mana = 500
    spent_mana = 0

    b_hp = 71
    b_damage = 10

    effects = []
    used_spells = []

    for i in range(50):
        if spent_mana > best:
            return 'too-much-mana', spent_mana, used_spells

        p_hp -= per_round_hp_loss
        if b_hp < 1:
            return 'won', spent_mana, used_spells
        if p_hp < 1:
            return 'lost', spent_mana, used_spells

        for e in effects:
            p_armor = max(p_armor, e.get('armor', 0))
            p_mana += e.get('mana', 0)
            b_hp -= e.get('damage', 0)
            e['duration'] -= 1

        effects = [e for e in effects if e['duration'] > 0]

        if b_hp < 1:
            return 'won', spent_mana, used_spells
        if p_hp < 1:
            return 'lost', spent_mana, used_spells

        actions = possible_actions(p_mana, effects)
        if len(actions) == 0:
            return 'noop', spent_mana, used_spells

        random.shuffle(actions)
        action = actions.pop()
        used_spells.append(action['name'])

        p_mana -= action['cost']
        spent_mana += action['cost']

        if 'duration' in action:
            effects.append(action.copy())
        else:
            b_hp -= action.get('instant_damage', 0)
            p_hp += action.get('instant_heal', 0)

        if b_hp < 1:
            return 'won', spent_mana, used_spells
        if p_hp < 1:
            return 'lost', spent_mana, used_spells

        for e in effects:
            p_armor = max(p_armor, e.get('armor', 0))
            p_mana += e.get('mana', 0)
            b_hp -= e.get('damage', 0)
            e['duration'] -= 1

        effects = [e for e in effects if e['duration'] > 0]

        if b_hp < 1:
            return 'won', spent_mana, used_spells
        if p_hp < 1:
            return 'lost', spent_mana, used_spells

        if p_armor >= b_damage:
            p_armor -= b_damage
            damage = 1
        else:
            damage = b_damage - p_armor
            p_armor = 0

        p_hp -= damage

        if b_hp < 1:
            return 'won', spent_mana, used_spells
        if p_hp < 1:
            return 'lost', spent_mana, used_spells


print('Part 1')
best = 999999
for i in range(250000):
    outcome, spent_mana, spells = play_round(best=best)
    if outcome == 'won' and spent_mana < best:
        best = spent_mana
        print('new best', best, spells)


print('Part 2')
best = 99999999
for i in range(2500000):
    outcome, spent_mana, spells = play_round(best=best, per_round_hp_loss=1)
    if outcome == 'won' and spent_mana < best:
        best = spent_mana
        print('new best', best, spells)
