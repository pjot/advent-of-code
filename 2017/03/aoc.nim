import tables

type
    Point = object
        x, y: int

    Direction = enum
        north, west, south, east

    Part = enum
        one, two

    Grid = Table[Point, int]

proc neighbourSum(grid: Grid, p: Point): int =
    let neighbours = [
        Point(x: p.x - 1, y: p.y - 1),
        Point(x: p.x, y: p.y - 1),
        Point(x: p.x + 1, y: p.y - 1),

        Point(x: p.x - 1, y: p.y),
        Point(x: p.x + 1, y: p.y),

        Point(x: p.x - 1, y: p.y + 1),
        Point(x: p.x, y: p.y + 1),
        Point(x: p.x + 1, y: p.y + 1),
    ]
    var sum = 0
    for n in neighbours:
        sum += grid.getOrDefault(n, 0)
    return sum

proc step(p: Point, direction: Direction): Point =
    case direction:
        of north:
            return Point(x: p.x, y: p.y - 1)
        of west:
            return Point(x: p.x - 1, y: p.y)
        of south:
            return Point(x: p.x, y: p.y + 1)
        of east:
            return Point(x: p.x + 1, y: p.y)

proc turn(direction: Direction): Direction =
    case direction:
        of north:
            return west
        of west:
            return south
        of south:
            return east
        of east:
            return north

proc manhattan(p: Point): int =
    return (abs p.x) + (abs p.y)

proc solve(part: Part): int =
    var
        p = Point(x: 0, y: 0)
        grid = Grid()
        d = east
        steps = 1
        value = 1
    let input = 325489

    grid[p] = 1

    while true:
        for _ in 1 .. steps div 2:
            p = p.step(d)

            if part == one:
                inc value
                grid[p] = value
                if grid[p] >= input:
                    return manhattan p

            if part == two:
                grid[p] = grid.neighbourSum p
                if grid[p] >= input:
                    return grid[p]

        d = turn d
        inc steps

echo "Part 1: ", solve one
echo "Part 2: ", solve two