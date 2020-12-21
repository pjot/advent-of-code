from collections import defaultdict
import math

def right(tile):
    return ''.join(tile[9, y] for y in range(10))

def left(tile):
    return ''.join(tile[0, y] for y in range(10))

def top(tile):
    return ''.join(tile[x, 0] for x in range(10))

def bottom(tile):
    return ''.join(tile[x, 9] for x in range(10))

def rotate(tile):
    new = {}
    for (x, y), c in tile.items():
        new[y, 9 - x] = c
    return new

def flip(tile):
    new = {}
    for (x, y), c in tile.items():
        new[x, 9 - y] = c
    return new

def rotated(tile):
    return [
        tile,
        rotate(tile),
        rotate(rotate(tile)),
        rotate(rotate(rotate(tile)))
    ]

def variants(tile):
    return rotated(tile) + rotated(flip(tile))

def parse(file):
    tiles = {}
    full_tiles = {}
    with open(file) as f:
        tile_id = y = 0
        for line in f.readlines():
            line = line.strip()
            if line.startswith('T'):
                tile_id = int(line.replace('Tile ', '').replace(':', ''))
                tile = {}
                y = 0
            elif len(line) == 0:
                tiles[tile_id] = tile_edges(tile, y)
                full_tiles[tile_id] = tile
            else:
                for x, c in enumerate(line):
                    tile[x, y] = c
                y += 1
    return tiles, full_tiles, int(math.sqrt(len(tiles)))


def tile_edges(tile, dimension):
    e = defaultdict(str)
    for r in range(dimension):
        e['N'] += tile[r, 0]
        e['S'] += tile[r, dimension-1]
        e['W'] += tile[0, r]
        e['E'] += tile[dimension-1, r]

    return e

def h(s):
    ss = [s, ''.join(reversed(s))]
    return sorted(ss).pop()

def classify_tiles(tiles, corner_edges):
    corners = []
    edges = []
    inners = []
    for tile, e in tiles.items():
        corner_edge = 0
        for d in 'NSWE':
            edge = e[d]
            edge = h(edge)
            if edge in corner_edges:
                corner_edge += 1

        if corner_edge == 2:
            corners.append(tile)

        elif corner_edge == 1:
            edges.append(tile)

        else:
            inners.append(tile)

    return corners, edges, inners

def edge_counts(tiles):
    edge_counts = defaultdict(int)
    for tile, e in tiles.items():
        for direction in 'NSWE':
            edge = e[direction]
            edge_counts[h(edge)] += 1
    return edge_counts

def edges(tile):
    te = tiles[tile]
    return set(h(e) for e in te.values())

def check_tiles(curr, ts, prev=None):
    ce = edges(curr)
    for tile in ts:
        te = edges(tile)
        if len(ce & te) == 1:
            if prev:
                pe = edges(prev)
                if len(pe & te) != 1:
                    continue
            return tile

def first_corner(full_tiles, rows):
    top_left_corner = rows[0][0]
    right_of_top_left = rows[0][1]
    below_top_left = rows[1][0]

    for top_left in variants(full_tiles[top_left_corner]):
        right_edge = right(top_left)
        bottom_edge = bottom(top_left)

        for right_of in variants(full_tiles[right_of_top_left]):
            if right_edge != left(right_of):
                continue

            for below in variants(full_tiles[below_top_left]):
                if bottom_edge == top(below):
                    return top_left, right_of, below

def build_grid(tile_grid):
    grid = {}
    for (x_offset, y_offset), tile in tile_grid.items():
        x_offset *= 10
        y_offset *= 10
        for (x, y), c in tile.items():
            x += x_offset
            y += y_offset
            grid[x, y] = c
    return grid

def build_tile_grid(full_tiles, rows):
    tile_grid = {}
    tile_grid[0, 0], tile_grid[1, 0], tile_grid[0, 1] = first_corner(full_tiles, rows)

    for y in range(dimension):
        for x in range(dimension):
            if (x, y) in tile_grid:
                continue

            tile = rows[y][x]

            for variant in variants(full_tiles[tile]):
                if x == 0:
                    if bottom(tile_grid[x, y - 1]) == top(variant):
                        tile_grid[x, y] = variant
                        break
                else:
                    if right(tile_grid[x - 1, y]) == left(variant):
                        tile_grid[x, y] = variant
                        break

    return tile_grid

def without_borders(n):
    n1 = n + 1
    borders = int(n1 / 10) * 2
    if n1 % 10 != 0:
        borders += 1
    return n - borders

def build_image(grid):
    image = {}
    for (x, y), c in grid.items():
        if x % 10 == 0 or x % 10 == 9:
            continue
        if y % 10 == 0 or y % 10 == 9:
            continue
        image[without_borders(x), without_borders(y)] = c
    return image

def parse_sea_monster():
    sea_monster_raw = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #',
    ]
    sea_monster = set()
    for y, line in enumerate(sea_monster_raw):
        for x, c in enumerate(line): 
            if c == '#':
                sea_monster.add((x, y))
    return sea_monster

def sea_monster_points(sea_monster, x0, y0):
    for x, y in sea_monster:
        yield (x + x0, y + y0)

def sea_monsters_in_image(sea_monster, image):
    points = 0
    for x0, y0 in image.keys():
        if sea_monster_at(sea_monster, image, x0, y0):
            for point in sea_monster_points(sea_monster, x0, y0):
                points += 1
    return points

def sea_monster_at(sea_monster, image, x0, y0):
    for x, y in sea_monster:
        point = (x + x0, y + y0)
        if image.get(point, '.') == '.':
            return False
    return True

def build_rows(corner_tiles, edge_tiles, inner_tiles):
    def delete_tile(tile):
        if tile in edge_tiles:
            edge_tiles.remove(tile)
        if tile in inner_tiles:
            inner_tiles.remove(tile)
        if tile in corner_tiles:
            corner_tiles.remove(tile)

    def build_row(start, row_index, last_row=None):
        current = start
        row = [start]
        while len(row) < dimension:
            last_tile = None if row_index == 0 else last_row[len(row)]

            if row_index == 0 or row_index == dimension - 1 or len(row) == dimension - 1:
                tile = check_tiles(current, edge_tiles, last_tile)
                if not tile:
                    tile = check_tiles(current, corner_tiles, last_tile)
                current = tile
                row.append(tile)
                delete_tile(tile)
                continue
            else:
                tile = check_tiles(current, inner_tiles, last_tile)
                if not tile:
                    tile = check_tiles(current, edge_tiles, last_tile)
                current = tile
                row.append(tile)
                delete_tile(tile)
                continue

        return row

    def next_start(prev):
        se = edges(prev)
        for ts in [edge_tiles, corner_tiles]:
            for tile in ts:
                te = edges(tile)
                if len(se & te) == 1:
                    return tile

    start = corner_tiles.pop()
    rows = []
    row_index = 0
    row = None
    while len(rows) < dimension:
        row = build_row(start, row_index, row)
        rows.append(row)
        start = next_start(start)
        delete_tile(start)
        row_index += 1

    return rows


tiles, full_tiles, dimension = parse('input.txt')
corner_edges = set(edge for edge, cnt in edge_counts(tiles).items() if cnt == 1)
corner_tiles, edge_tiles, inner_tiles = classify_tiles(tiles, corner_edges)

corners = 1
for corner in corner_tiles:
    corners *= corner

print('Part 1:', corners)
rows = build_rows(corner_tiles, edge_tiles, inner_tiles)
tile_grid = build_tile_grid(full_tiles, rows)
grid = build_grid(tile_grid)
image = build_image(grid)

image_hashes = list(image.values()).count('#')

sea_monster = parse_sea_monster()
for variant in variants(image):
    found_sea_monster_points = sea_monsters_in_image(sea_monster, variant)
    if found_sea_monster_points:
        print('Part 2:', image_hashes - found_sea_monster_points)
