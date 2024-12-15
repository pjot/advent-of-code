import typing

Point = tuple[int, int]
Walls = set[Point]
BoxOne = Point
BoxTwo = tuple[Point, Point]
Parsed = tuple[Walls, Walls, set[BoxOne], set[BoxTwo], Point, Point, str]

def parse(file: str) -> Parsed:
    w1 = set()
    b1 = set()
    p1 = (0, 0)

    w2 = set()
    b2 = set()
    p2 = (0, 0)

    moves = ""
    with open(file) as f:
        reading_grid = True
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                reading_grid = False
                continue
            if reading_grid:
                for x, c in enumerate(line):
                    if c == "#":
                        w1.add((x, y))
                        w2.add((2 * x, y))
                        w2.add((2 * x + 1, y))
                    if c == "@":
                        p1 = x, y
                        p2 = 2 * x, y
                    if c == "O":
                        b1.add((x, y))
                        b2.add((
                            (2 * x, y),
                            (2 * x + 1, y),
                        ))

            else:
                moves += line

    return w1, w2, b1, b2, p1, p2, moves

def move(p: Point, d: str) -> Point:
    x, y = p
    if d == ">":
        return x + 1, y
    if d == "<":
        return x - 1, y
    if d == "^":
        return x, y - 1
    if d == "v":
        return x, y + 1
    return p

def can_move(
    walls: Walls,
    points: typing.Iterable[Point],
    direction: str,
) -> bool:
    for p in points:
        if move(p, direction) in walls:
            return False
    return True

def move_one(
    walls: Walls,
    boxes: set[BoxOne],
    player: Point,
    direction: str,
) -> tuple[set[BoxOne], Point]:
    candidate = move(player, direction)

    if candidate in walls:
        return boxes, player

    if candidate in boxes:
        b = candidate
        while b in boxes:
            b = move(b, direction)

        if b in walls:
            return boxes, player
        else:
            boxes.add(b)
            boxes.remove(candidate)
            return boxes, candidate

    return boxes, candidate

def move_two(
    walls: Walls,
    boxes: set[BoxTwo],
    player: Point,
    direction: str
) -> tuple[set[BoxTwo], Point]:
    candidate = move(player, direction)

    if candidate in walls:
        return boxes, player

    boxes_left = set(b[0] for b in boxes)
    boxes_right = set(b[1] for b in boxes)
    all_boxes = boxes_left | boxes_right

    if candidate not in all_boxes:
        return boxes, candidate

    if direction in "^v":
        horizon = {candidate}
        seen_boxes = set()
        while horizon:
            next_horizon = set()
            for point in horizon:
                while point in all_boxes:
                    if point in boxes_left:
                        seen_boxes.add((
                            point, move(point, ">")
                        ))
                        point = move(point, direction)
                        next_horizon.add(move(point, ">"))
                    else:
                        seen_boxes.add((
                            move(point, "<"), point
                        ))
                        point = move(point, direction)
                        next_horizon.add(move(point, "<"))

                    next_horizon.add(point)

            horizon = next_horizon

        points_to_move = []
        moved_boxes = set()
        for left, right in seen_boxes:
            points_to_move.append(left)
            points_to_move.append(right)

            moved_boxes.add((
                move(left, direction),
                move(right, direction),
            ))

        if can_move(walls, points_to_move, direction):
            boxes -= seen_boxes
            boxes |= moved_boxes
            return boxes, candidate
        else:
            return boxes, player

    if direction in "<>":
        b = candidate

        seen_boxes = set()
        while b in all_boxes:
            if direction == ">" and b in boxes_left:
                seen_boxes.add((
                    b, move(b, direction)
                ))
            elif direction == "<" and b in boxes_right:
                seen_boxes.add((
                    move(b, direction), b
                ))
            b = move(b, direction)

        if b not in walls:
            moved_boxes = set()
            for left, right in seen_boxes:
                moved_boxes.add((
                    move(left, direction),
                    move(right, direction)
                ))
            boxes -= seen_boxes
            boxes |= moved_boxes
            return boxes, candidate

        return boxes, player

    return boxes, player

def score(boxes: typing.Iterable[BoxOne]) -> int:
    s = 0
    for x, y in boxes:
        s += x + y * 100
    return s

w1, w2, b1, b2, p1, p2, moves = parse("input")

for m in moves:
    b1, p1 = move_one(w1, b1, p1, m)
    b2, p2 = move_two(w2, b2, p2, m)

print("Part 1:", score(b1))
print("Part 2:", score([l for l, _ in b2]))
