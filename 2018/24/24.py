from dataclasses import dataclass
from itertools import count

@dataclass
class Group:
    id: int
    kind: str
    units: int
    hp: int
    initiative: int
    damage: int
    damage_type: str
    immunities: list[str]
    weaknesses: list[str]

    @property
    def effective_power(self):
        return self.units * self.damage

    @property
    def identifier(self):
        return f'{self.kind}-{self.id}'

    def can_attack(self, other):
        return self.kind != other.kind

    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.identifier == other.identifier



def parse(file):
    groups = []

    with open(file) as f:
        reading = ''
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith('Immune'):
                reading = 'immune'
                counter = count()
                next(counter)
            elif line.startswith('Infection'):
                reading = 'infection'
                counter = count()
                next(counter)
            else:
                words = line.split(' ')
                units = int(words[0])
                hp = int(words[4])
                initiative = int(words[-1])
                damage_type = words[-5]
                damage = int(words[-6])

                traits = line.split('(').pop().split(')')[0]
                trait_words = traits.replace(',', '').replace(';', '').split(' ')

                immunities = []
                weaknesses = []

                kind = ''
                for w in trait_words:
                    if w == 'weak':
                        kind = 'weak'
                    elif w == 'immune':
                        kind = 'immune'
                    elif w == 'to':
                        pass
                    else:
                        if kind == 'weak':
                            weaknesses.append(w)
                        if kind == 'immune':
                            immunities.append(w)

                groups.append(Group(
                    next(counter), reading,
                    units, hp, initiative,
                    damage, damage_type,
                    immunities, weaknesses
                ))

    return groups

def say(groups):
    print('Immune system:')
    immune_groups = [g for g in groups if g.kind == 'immune']
    if immune_groups:
        for group in immune_groups:
            print(f'Group {group.id} contains {group.units} units')
    else:
        print('No groups remain')

    print('Infection:')
    infection_groups = [g for g in groups if g.kind == 'infection']
    if infection_groups:
        for group in infection_groups:
            print(f'Group {group.id} contains {group.units} units')
    else:
        print('No groups remain')

def sort_for_target_selection(groups):
    return sorted(
        groups,
        key=lambda g: (g.effective_power, g.initiative),
        reverse=True
    )

def attack_points(attacker, defender):
    if attacker.damage_type in defender.immunities:
        return 0
    if attacker.damage_type in defender.weaknesses:
        return 2 * attacker.effective_power
    return attacker.effective_power

def select_targets(groups):
    targets = {}
    groups = sort_for_target_selection(groups)
    for attacker in groups:
        taken = set([t.identifier for t in targets.values()])
        highest_damage = 0
        target = False
        for defender in groups:
            if not attacker.can_attack(defender):
                continue
            if defender.identifier in taken:
                continue

            if not target:
                target = defender

            damage = attack_points(attacker, defender)
            if damage > highest_damage:
                highest_damage = damage
                target = defender
            elif damage == highest_damage:
                if defender.effective_power > target.effective_power:
                    target = defender
                elif defender.effective_power == target.effective_power:
                    if defender.initiative > target.initiative:
                        target = defender

        if target:
            targets[attacker.identifier] = target

    return targets

def attack_order(groups):
    return sorted(
        groups,
        key=lambda g: g.initiative,
        reverse=True
    )

def is_alive(group, groups):
    for alive in groups:
        if group == alive:
            return True
    return False

def kill(group, groups):
    return [g for g in groups if g != group]

def hurt(group, units, groups):
    for g in groups:
        if g == group:
            g.units -= units

def get(identifier, groups):
    for group in groups:
        if group.identifier == identifier:
            return group

def iterate(groups):
    print()
    say(groups)
    print()

    targets = select_targets(groups)
    attackers = attack_order(groups)
    for attacker in attackers:
        updated_attacker = get(attacker.identifier, groups)

        target = targets.get(attacker.identifier)
        if target is None:
            continue

        damage = attack_points(attacker, target)
        lost_units = damage // target.hp

        if lost_units >= target.units:
            lost_units = target.units
            groups = kill(target, groups)
        else:
            hurt(target, lost_units, groups)

        print(f'{attacker} attacks {target}, killing {lost_units} units')
    print()
    return groups

def is_finished(groups):
    kinds = set(g.kind for g in groups)
    return len(kinds) == 1

def units_left(groups):
    return sum(g.units for g in groups)

groups = parse('input.txt')
while not is_finished(groups):
    groups = iterate(groups)

say(groups)
print()
print('Part 1:', units_left(groups))
