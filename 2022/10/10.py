class CPU:
    operations = []
    signal_strengths = []
    screen = []
    cycle = x = 1

    def __init__(self, file):
        self.operations = []
        with open(file) as f:
            for line in f.readlines():
                parts = line.strip().split()

                arg = None
                op = parts[0]

                if op == "addx":
                    arg = int(parts[1])

                self.operations.append((op, arg))

    def update(self):
        # Part 1
        if self.cycle % 40 == 20:
            self.signal_strengths.append(self.cycle * self.x)

        # Part 2
        position = (self.cycle - 1) % 40
        if self.x - 1 <= position <= self.x + 1:
            self.screen[self.cycle - 1] = "@"
        else:
            self.screen[self.cycle - 1] = " "

        # Increase cycle
        self.cycle += 1

    def run(self):
        self.cycle = 1
        self.x = 1
        self.screen = ["_"] * 40 * 6
        for op, arg in self.operations:
            if op == "noop":
                self.update()

            if op == "addx":
                self.update()
                self.update()

                self.x += arg

    def display(self):
        screen = "".join(self.screen)
        for line in range(6):
            start = 40 * line
            end = 40 * (line + 1)
            print(screen[start:end])

cpu = CPU("input.txt")
cpu.run()

print("Part 1:", sum(cpu.signal_strengths))
print("Part 2:")
cpu.display()
