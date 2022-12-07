from pprint import pprint

def parse(file):
    files = {}
    directories = []
    cwd = "/"

    with open(file) as f:
        for line in f.readlines():
            parts = line.strip().split()

            if parts[0] == "$":
                if parts[1] == "cd":
                    if parts[2] == "/":
                        cwd = "/"
                    elif parts[2] == "..":
                        cwd, _ = cwd.rsplit("/", maxsplit=1)
                    else:
                        if not cwd.endswith("/"):
                            cwd += "/"
                        cwd += parts[2]

                    if cwd == "":
                        cwd = "/"

            elif parts[0] == "dir":
                directory = parts[1]
                if not cwd.endswith("/"):
                    directory = "/" + directory
                path = cwd + directory
                directories.append(path)

            else:
                size, file = parts
                if not cwd.endswith("/"):
                    file = "/" + file
                path = cwd + file
                files[path] = int(size)

    sizes = {}
    for directory in directories:
        directory = directory + "/"
        size = sum(
            s for file, s in files.items() if file.startswith(directory)
        )
        sizes[directory] = size

    return sizes, files


def one(directories):
    return sum(size for size in directories.values() if size <= 100000)

def two(directories, files):
    total_used = sum(s for s in files.values())
    unused = 70000000 - total_used
    needs = 30000000 - unused

    return min(size for size in directories.values() if size > needs)


directories, files = parse("input.txt")

print("Part 1:", one(directories))
print("Part 2:", two(directories, files))
