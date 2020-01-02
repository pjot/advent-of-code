def length(maze):
    pos = 0
    l = len(maze)
    steps = 0
    while pos < l:
        next_pos = pos + maze[pos]
        maze[pos] += 1
        pos = next_pos
        steps += 1
    return steps


def length_two(maze):
    pos = 0
    l = len(maze)
    steps = 0
    while pos < l:
        next_pos = pos + maze[pos]
        maze[pos] += 1 if maze[pos] < 3 else -1
        pos = next_pos
        steps += 1
    return steps


def get_maze():
    maze = []
    with open('input') as f:
        for l in f.readlines():
            maze.append(int(l.strip()))
    return maze


print('Part 1:', length(get_maze()))
print('Part 2:', length_two(get_maze()))