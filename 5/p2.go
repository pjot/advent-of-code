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
	data []int
}

type Mode int

const Immediate = 1
const Position = 0

type OpCode int

const Add = 1
const Multiply = 2
const Input = 3
const Output = 4
const JumpIfTrue = 5
const JumpIfFalse = 6
const LessThan = 7
const Equals = 8
const Halt = 99

func (m *Memory) read(position int, mode Mode) int {
	switch mode {
	case Immediate:
		return m.data[position]
	case Position:
		return m.data[m.data[position]]
	}
	return 0
}

func (m *Memory) write(position int, value int) {
	m.data[m.data[position]] = value
}

func parseInstruction(instruction int) (OpCode, Mode, Mode) {
	opCode := OpCode(instruction % 100)
	modeA := Mode((instruction % 1000) / 100)
	modeB := Mode((instruction % 10000) / 1000)
	return opCode, modeA, modeB
}

func runProgram(memory Memory, input int) int {
	position := 0
	output := 0

	for {
		instruction := memory.read(position, Immediate)
		opCode, modeA, modeB := parseInstruction(instruction)

		switch opCode {
		case Halt:
			return output
		case Add:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			memory.write(position+3, a+b)
			position += 4
		case Multiply:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			memory.write(position+3, a*b)
			position += 4
		case Input:
			memory.write(position+1, input)
			position += 2
		case Output:
			output = memory.read(position+1, modeA)
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
				memory.write(position+3, 1)
			} else {
				memory.write(position+3, 0)
			}
			position += 4
		case Equals:
			a := memory.read(position+1, modeA)
			b := memory.read(position+2, modeB)
			if a == b {
				memory.write(position+3, 1)
			} else {
				memory.write(position+3, 0)
			}
			position += 4
		}
	}
}

func main() {
	program := parseFile("program.testcode")
	m := Memory{data: program}
	result := runProgram(m, 1)
	fmt.Println(result)
}
