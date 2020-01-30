import json

data = []
with open("input") as f:
    for line in f.readlines():
        data.append(json.loads(line))

def recursive_sum(obj, s=0):
    if isinstance(obj, list):
        s += sum(recursive_sum(o) for o in obj)
    if isinstance(obj, dict):
        s += sum(recursive_sum(o) for o in obj.values())
    if isinstance(obj, int):
        s += obj
    return s

def recursive_red_sum(obj, s=0):
    if isinstance(obj, list):
        s += sum(recursive_red_sum(o) for o in obj)
    if isinstance(obj, dict):
        if 'red' not in obj.values():
            s += sum(recursive_red_sum(o) for o in obj.values())
    if isinstance(obj, int):
        s += obj
    return s

print("Part 1:", recursive_sum(data))
print("Part 2:", recursive_red_sum(data))


