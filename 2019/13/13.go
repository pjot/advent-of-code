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

type Computer struct {
	memory   map[int]int
	base     int
	position int
	outputs  chan int
	inputs   chan int
}

func NewComputer(program []int) (chan int, chan int) {
	memory := make(map[int]int)
	for i, val := range program {
		memory[i] = val
	}
	in := make(chan int, 1)
	out := make(chan int, 1)
	c := Computer{
		base:     0,
		position: 0,
		outputs:  out,
		inputs:   in,
		memory:   memory,
	}
	go c.run()
	return in, out
}

func (c *Computer) g(position int) int {
	if v, ok := c.memory[position]; ok {
		return v
	}
	return 0
}

func (c *Computer) read(position int, mode Mode) int {
	switch mode {
	case Immediate:
		return c.g(position)
	case Position:
		return c.g(c.g(position))
	case Relative:
		return c.g(c.base + c.g(position))
	}
	return 0
}

func (c *Computer) write(position int, value int, mode Mode) {
	switch mode {
	case Immediate:
		c.memory[position] = value
	case Position:
		c.memory[c.g(position)] = value
	case Relative:
		c.memory[c.base+c.g(position)] = value
	}
}

func parseInstruction(instruction int) (OpCode, Mode, Mode, Mode) {
	opCode := OpCode(instruction % 100)
	modeA := Mode((instruction % 1000) / 100)
	modeB := Mode((instruction % 10000) / 1000)
	modeC := Mode((instruction % 100000) / 10000)
	return opCode, modeA, modeB, modeC
}

func (c *Computer) run() {
	for {
		instruction := c.read(c.position, Immediate)
		opCode, modeA, modeB, modeC := parseInstruction(instruction)

		switch opCode {
		case Halt:
			close(c.outputs)
			return
		case Add:
			a := c.read(c.position+1, modeA)
			b := c.read(c.position+2, modeB)
			c.write(c.position+3, a+b, modeC)
			c.position += 4
		case Multiply:
			a := c.read(c.position+1, modeA)
			b := c.read(c.position+2, modeB)
			c.write(c.position+3, a*b, modeC)
			c.position += 4
		case Input:
			c.write(c.position+1, <-c.inputs, modeA)
			c.position += 2
		case Output:
			c.outputs <- c.read(c.position+1, modeA)
			c.position += 2
		case JumpIfTrue:
			a := c.read(c.position+1, modeA)
			if a != 0 {
				c.position = c.read(c.position+2, modeB)
			} else {
				c.position += 3
			}
		case JumpIfFalse:
			a := c.read(c.position+1, modeA)
			if a == 0 {
				c.position = c.read(c.position+2, modeB)
			} else {
				c.position += 3
			}
		case LessThan:
			a := c.read(c.position+1, modeA)
			b := c.read(c.position+2, modeB)
			if a < b {
				c.write(c.position+3, 1, modeC)
			} else {
				c.write(c.position+3, 0, modeC)
			}
			c.position += 4
		case Equals:
			a := c.read(c.position+1, modeA)
			b := c.read(c.position+2, modeB)
			if a == b {
				c.write(c.position+3, 1, modeC)
			} else {
				c.write(c.position+3, 0, modeC)
			}
			c.position += 4
		case SetBase:
			a := c.read(c.position+1, modeA)
			c.base += a
			c.position += 2
		}
	}
}

func countBlocks(program []int) int {
	_, out := NewComputer(program)
	outputs := []int{}
	for {
		output, ok := <-out
		if ok {
			outputs = append(outputs, output)
		} else {
			break
		}
	}
	blocks := 0
	for i := 2; i < len(outputs); i += 3 {
		if outputs[i] == 2 {
			blocks++
		}
	}
	return blocks
}

func joystick(pad int, ball int) int {
	if pad > ball {
		return -1
	}
	if ball > pad {
		return 1
	}
	return 0
}

func playGame(program []int) int {
	in, out := NewComputer(program)

	pad := 0
	ball := 0
	score := 0

	for {
		x, ok := <-out
		if !ok {
			return score
		}
		y := <-out
		tile := <-out

		if x == -1 && y == 0 {
			score = tile
		}

		switch tile {
		case 4:
			ball = x
			in <- joystick(pad, ball)
		case 3:
			pad = x
		}

	}
}

func main() {
	program := parseFile("game.intcode")

	fmt.Println("Part 1:", countBlocks(program))

	program[0] = 2
	fmt.Println("Part 2:", playGame(program))
}
