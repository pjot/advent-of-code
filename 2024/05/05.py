from collections import defaultdict
from functools import cmp_to_key
import typing

Page = str
Update = list[Page]

class Rules:
    rules: dict[Page, set[Page]]

    def __init__(self):
        self.rules = defaultdict(set)

    def add(self, a: Page, b: Page):
        self.rules[a].add(b)

    def validate(self, update: Update) -> int:
        for i, c in enumerate(update):
            before = set(update[:i])

            if before & self.rules[c]:
                return 0

        return middle(update)

    def key_function(self) -> typing.Callable:
        def compare(a: Page, b: Page) -> int:
            if b in self.rules[a]:
                return 1
            if a in self.rules[b]:
                return -1
            return 0

        return cmp_to_key(compare)

def parse(file: str) -> tuple[Rules, list[Update]]:
    rules = Rules()
    updates = []
    with open(file) as f:
        for line in f.readlines():
            if "|" in line:
                a, b = line.strip().split("|")
                rules.add(a, b)
            if "," in line:
                updates.append(line.strip().split(","))
    return rules, updates

def middle(update: Update) -> int:
    m = len(update) // 2
    return int(update[m])


rules, updates = parse("input")

one = 0
invalid_updates = []
for update in updates:
    m = rules.validate(update)
    one += m
    if m == 0:
        invalid_updates.append(update)

two = 0
for update in invalid_updates:
    update.sort(key=rules.key_function())
    two += middle(update)

print("Part 1:", one)
print("Part 2:", two)

