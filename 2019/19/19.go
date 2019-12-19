package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseFile(fileName string) []int {
	data, _ := ioutil.ReadFile(fileName)
	program := []int{}
	for _, s := range strings.Split(string(data), ",") {
		trimmed := strings.Trim(s, "\n")
		if i, err := strconv.Atoi(trimmed); err == nil {
			program = append(program, i)
		}
	}
	return program
}

type Mode int

const (
	Position  = 0
	Immediate = 1
	Relative  = 2
)

type OpCode int

const (
	Add         = 1
	Multiply    = 2
	Input       = 3
	Output      = 4
	JumpIfTrue  = 5
	JumpIfFalse = 6
	LessThan    = 7
	Equals      = 8
	SetBase     = 9
	Halt        = 99
)

type Memory struct {
	data map[int]int
	base int
}

func (m *Memory) g(position int) int {
	if v, ok := m.data[position]; ok {
		return v
	}
	return 0
}

func (m *Memory) read(position int, mode Mode) int {
	switch mode {
	case Immediate:
		return m.g(position)
	case Position:
		return m.g(m.g(position))
	case Relative:
		return m.g(m.base + m.g(position))
	}
	return 0
}

func (m *Memory) write(position int, value int, mode Mode) {
	switch mode {
	case Immediate:
		m.data[position] = value
	case Position:
		m.data[m.g(position)] = value
	case Relative:
		m.data[m.base+m.g(position)] = value
	}
}

func parseInstruction(instruction int) (OpCode, Mode, Mode, Mode) {
	opCode := OpCode(instruction % 100)
	modeA := Mode((instruction % 1000) / 100)
	modeB := Mode((instruction % 10000) / 1000)
	modeC := Mode((instruction % 100000) / 10000)
	return opCode, modeA, modeB, modeC
}

func Computer(program []int) (chan int, chan int) {
	m := make(map[int]int)
	for i, val := range program {
		m[i] = val
	}
	memory := Memory{
		data: m,
		base: 0,
	}
	in := make(chan int)
	out := make(chan int)
	go run(memory, in, out)
	return in, out
}

func run(
	m Memory,
	in chan int,
	out chan int,
) {
	position := 0
	for {
		instruction := m.read(position, Immediate)
		opCode, modeA, modeB, modeC := parseInstruction(instruction)

		switch opCode {
		case Halt:
			close(out)
			return
		case Add:
			a := m.read(position+1, modeA)
			b := m.read(position+2, modeB)
			m.write(position+3, a+b, modeC)
			position += 4
		case Multiply:
			a := m.read(position+1, modeA)
			b := m.read(position+2, modeB)
			m.write(position+3, a*b, modeC)
			position += 4
		case Input:
			m.write(position+1, <-in, modeA)
			position += 2
		case Output:
			out <- m.read(position+1, modeA)
			position += 2
		case JumpIfTrue:
			a := m.read(position+1, modeA)
			if a != 0 {
				position = m.read(position+2, modeB)
			} else {
				position += 3
			}
		case JumpIfFalse:
			a := m.read(position+1, modeA)
			if a == 0 {
				position = m.read(position+2, modeB)
			} else {
				position += 3
			}
		case LessThan:
			a := m.read(position+1, modeA)
			b := m.read(position+2, modeB)
			if a < b {
				m.write(position+3, 1, modeC)
			} else {
				m.write(position+3, 0, modeC)
			}
			position += 4
		case Equals:
			a := m.read(position+1, modeA)
			b := m.read(position+2, modeB)
			if a == b {
				m.write(position+3, 1, modeC)
			} else {
				m.write(position+3, 0, modeC)
			}
			position += 4
		case SetBase:
			a := m.read(position+1, modeA)
			m.base += a
			position += 2
		}
	}
}

func check(x, y int) bool {
	program := parseFile("input.intcode")
	in, out := Computer(program)
	in <- x
	in <- y
	return <-out == 1
}

func countAffected() int {
	affected := 0
	for x := 0; x < 50; x++ {
		for y := 0; y < 50; y++ {
			if check(x, y) {
				affected++
			}
		}
	}
	return affected
}

func findEdge(x, y int) int {
	for {
		if check(x, y) {
			return x
		}
		x++
	}
}

func findFit(size int) (int, int) {
	x, y := size, size
	for {
		x = findEdge(x, y)
		if check(x+size-1, y-size+1) {
			return x, y - size + 1
		}
		y++
	}
}

func main() {
	fmt.Println("Part 1:", countAffected())

	x, y := findFit(100)
	fmt.Println("Part 2:", x*10000+y)
}
