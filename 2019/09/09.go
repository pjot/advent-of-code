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

type Memory struct {
	data map[int]int
    base int
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
        m.data[m.base + m.g(position)] = value
	}
}

func parseInstruction(instruction int) (OpCode, Mode, Mode, Mode) {
	opCode := OpCode(instruction % 100)
	modeA := Mode((instruction % 1000) / 100)
	modeB := Mode((instruction % 10000) / 1000)
	modeC := Mode((instruction % 100000) / 10000)
	return opCode, modeA, modeB, modeC
}

func runProgram(memory Memory, input int) []int {
	position := 0
	output := []int{}

	for {
		instruction := memory.read(position, Immediate)
		opCode, modeA, modeB, modeC := parseInstruction(instruction)

		switch opCode {
		case Halt:
			return output
		case Add:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			memory.write(position+3, a+b, modeC)
			position += 4
		case Multiply:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			memory.write(position+3, a*b, modeC)
			position += 4
		case Input:
			memory.write(position+1, input, modeA)
			position += 2
		case Output:
			output = append(output, memory.read(position+1, modeA))
			position += 2
		case JumpIfTrue:
			a := memory.read(position+1, modeA)
			if a != 0 {
				position = memory.read(position+2, modeB)
			} else {
				position += 3
			}
		case JumpIfFalse:
			a := memory.read(position+1, modeA)
			if a == 0 {
				position = memory.read(position+2, modeB)
			} else {
				position += 3
			}
		case LessThan:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			if a < b {
				memory.write(position+3, 1, modeC)
			} else {
				memory.write(position+3, 0, modeC)
			}
			position += 4
		case Equals:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			if a == b {
				memory.write(position+3, 1, modeC)
			} else {
				memory.write(position+3, 0, modeC)
			}
			position += 4
        case SetBase:
            a := memory.read(position+1, modeA)
            memory.base += a
            position += 2
		}
	}
}

func parse (p []int) map[int]int {
    o := make(map[int]int)
    for i, val := range p {
        o[i] = val
    }
    return o
}

func main() {
	program := parseFile("input.intcode")
    result := runProgram(Memory{data: parse(program)}, 1)
	fmt.Println("Part 1:", result)

	program2 := parseFile("input.intcode")
	result2 := runProgram(Memory{data: parse(program2)}, 2)
	fmt.Println("Part 2:", result2)
}
