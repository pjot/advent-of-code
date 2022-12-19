import collections

def parse(file):
    blueprints = {}
    with open(file) as f:
        for line in f.readlines():
            p = line.strip().split()

            id = int(p[1].replace(":", ""))
            ore_cost = int(p[6])
            clay_cost = int(p[12])
            obsidian_cost_ore = int(p[18])
            obsidian_cost_clay = int(p[21])
            geode_cost_ore = int(p[27])
            geode_cost_obsidian = int(p[30])

            blueprints[id] = (
                ore_cost, clay_cost,
                obsidian_cost_ore, obsidian_cost_clay,
                geode_cost_ore, geode_cost_obsidian
            )
    return blueprints

def add(a, b):
    return (
        a[0] + b[0],
        a[1] + b[1],
        a[2] + b[2],
        a[3] + b[3],
    )

def max_geodes(bp, time=24):
    horizon = collections.deque()
    horizon.append((time, (0, 0, 0, 0), (1, 0, 0, 0)))
    seen = set()

    ore_ore = bp[0]
    clay_ore = bp[1]
    obsidian_ore = bp[2]
    obsidian_clay = bp[3]
    geode_ore = bp[4]
    geode_obsidian = bp[5]

    best = 0
    while horizon:
        time_left, resources, robots = horizon.popleft()
        ore, clay, obsidian, geodes = resources
        ore_robots, clay_robots, obsidian_robots, geode_robots = robots

        best = max(best, geodes)

        if time_left == 0 or (resources, robots) in seen:
            continue

        seen.add((resources, robots))

        possible_geodes = (
            geodes +
            time_left * geode_robots +
            time_left * (time_left + 1) // 2
        )
        if possible_geodes <= best:
            continue

        updated_resources = add(resources, robots)

        ore_cost = max(ore_ore, clay_ore, obsidian_ore, geode_ore)
        if (
            ore >= ore_ore
            and ore_robots < ore_cost
            and ore + time_left * ore_robots < time_left * ore_cost
        ):
            horizon.append((
                time_left - 1,
                add(updated_resources, (-ore_ore, 0, 0, 0)),
                add(robots, (1, 0, 0, 0))
            ))

        if (
            ore >= clay_ore
            and clay_robots < obsidian_clay
            and clay + time_left * clay_robots < time_left * obsidian_clay
        ):
            horizon.append((
                time_left - 1,
                add(updated_resources, (-clay_ore, 0, 0, 0)),
                add(robots, (0, 1, 0, 0))
            ))

        if (
            ore >= obsidian_ore and clay >= obsidian_clay
            and obsidian_robots < geode_obsidian
            and obsidian + time_left * obsidian_robots < time_left * geode_obsidian
        ):
            horizon.append((
                time_left - 1,
                add(updated_resources, (-obsidian_ore, -obsidian_clay, 0, 0)),
                add(robots, (0, 0, 1, 0))
            ))

        if ore >= geode_ore and obsidian >= geode_obsidian:
            horizon.append((
                time_left - 1,
                add(updated_resources, (-geode_ore, 0, -geode_obsidian, 0)),
                add(robots, (0, 0, 0, 1))
            ))

        else:
            horizon.append((
                time_left - 1,
                updated_resources,
                robots
            ))

    return best

def quality_level(id, max_geodes):
    return id * max_geodes

blueprints = parse("input.txt")

total_quality = 0
for k, b in blueprints.items():
    total_quality += quality_level(k, max_geodes(b, 24))

print("Part 1:", total_quality)

a = max_geodes(blueprints[1], 32)
b = max_geodes(blueprints[2], 32)
c = max_geodes(blueprints[3], 32)

print("Part 2:", a * b * c)
