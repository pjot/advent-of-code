import sets

type
    Moon = object
        x, y, z: int
        u, v, w: int

    System = array[4, Moon]

proc update(m: Moon, others: seq[Moon]): Moon =
    result.u = m.u
    result.v = m.v
    result.w = m.w

    for o in others:
        if o.x > m.x: inc result.u
        if o.y > m.y: inc result.v
        if o.z > m.z: inc result.w

        if o.x < m.x: dec result.u
        if o.y < m.y: dec result.v
        if o.z < m.z: dec result.w

    result.x = m.x + result.u 
    result.y = m.y + result.v
    result.z = m.z + result.w

proc update(s: System): System =
    [
        update(s[0], @[s[1], s[2], s[3]]),
        update(s[1], @[s[0], s[2], s[3]]),
        update(s[2], @[s[1], s[0], s[3]]),
        update(s[3], @[s[1], s[2], s[0]]),
    ]

func potential(m: Moon): int =
    (abs m.x) + (abs m.y) + (abs m.z)

func kinetic(m: Moon): int =
    (abs m.u) + (abs m.v) + (abs m.w)

func energy(m: Moon): int =
    m.potential * m.kinetic

func energy(system: System): int =
    for moon in system:
        result.inc moon.energy

func run(system: System, steps: int): System =
    result = system
    for _ in 0 ..< steps:
        result = update(result)

var system = [
    Moon(x: 17, y: -7, z: -11),
    Moon(x: 1, y: 4, z: -1),
    Moon(x: 6, y: -2, z: -6),
    Moon(x: 19, y: 11, z: 9),
]

echo "Part 1: ", system.run(1000).energy