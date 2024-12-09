class File:
    id: int
    start: int
    length: int

    def __init__(self, id: int, start: int, length: int):
        self.id = id
        self.start = start
        self.length = length

    def checksum(self):
        s = 0
        for i in range(self.start, self.start + self.length):
            s += i * self.id
        return s

class Space:
    start: int
    length: int

    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length

def parse(file):
    files = []
    spaces = []
    with open(file) as f:
        line = f.readlines()[0].strip()

        file_id = 0
        is_file = True
        position = 0
        for c in line:
            n = int(c)
            if is_file:
                files.append(File(file_id, position, n))
                file_id += 1
            else:
                spaces.append(Space(position, n))
            position += n

            is_file = not is_file

    return files, spaces

def backwards(files):
    for f in reversed(files):
        for i in range(f.start + f.length, f.start, -1):
            yield f.id, i

def one(files, spaces):
    disk = {}
    for f in files:
        for p in range(f.start, f.start + f.length):
            disk[p] = f.id

    for s in spaces:
        for ss in range(s.start, s.start + s.length):
            disk[ss] = "."

    back = backwards(files)
    for space in spaces:
        for p in range(space.start, space.start + space.length):
            file_id, position = next(back)
            if p > position:
                break
            disk[position - 1] = "."
            disk[p] = file_id

    blocks = [(p, v) for p, v in disk.items() if v != "."]
    s = 0
    for i, c in blocks:
        s += i * c
    return s

def two(files, spaces):
    for file in reversed(files):
        for space in spaces:
            if space.start > file.start:
                break
            if space.length >= file.length:
                file.start = space.start
                space.start += file.length
                space.length -= file.length
                break

    s = 0
    for f in files:
        s += f.checksum()
    return s

files, spaces = parse("input")
print("Part 1:", one(files, spaces))
print("Part 2:", two(files, spaces))
