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
    memory map[int]int
    base int
    position int
    output int
    nextInput func() int
}

func NewComputer(program []int) Computer {
    memory := make(map[int]int)
    for i, val := range program {
        memory[i] = val
    }
    return Computer{
        base: 0,
        position: 0,
        output: 0,
        nextInput: func () int { return 0 },
        memory: memory,
    }
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
        c.memory[c.base + c.g(position)] = value
	}
}

func parseInstruction(instruction int) (OpCode, Mode, Mode, Mode) {
	opCode := OpCode(instruction % 100)
	modeA := Mode((instruction % 1000) / 100)
	modeB := Mode((instruction % 10000) / 1000)
	modeC := Mode((instruction % 100000) / 10000)
	return opCode, modeA, modeB, modeC
}

func (c *Computer) iterate() bool {
	for {
		instruction := c.read(c.position, Immediate)
		opCode, modeA, modeB, modeC := parseInstruction(instruction)

		switch opCode {
		case Halt:
			return true
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
			c.write(c.position+1, c.nextInput(), modeA)
			c.position += 2
		case Output:
			c.output = c.read(c.position+1, modeA)
			c.position += 2
            return false
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

func countBlocks (program []int) int {
    computer := NewComputer(program)
    outputs := []int{}
    done := false
    for {
        done = computer.iterate()
        if !done {
            outputs = append(outputs, computer.output)
        } else {
            break;
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

func playGame (program []int) int {
    computer := NewComputer(program)
    pad := 0
    ball := 0
    score := 0

    for {
        computer.nextInput = func() int { return joystick(pad, ball) }

        computer.iterate()
        x := computer.output

        computer.iterate()
        y := computer.output

        done := computer.iterate()
        tile := computer.output

        switch tile {
        case 4:
            ball = x
        case 3:
            pad = x
        }

        if x == -1 && y == 0 {
            score = tile
        }
        if done {
            return score
        }
    }
}

func main() {
	program := parseFile("game.intcode")

	fmt.Println("Part 1:", countBlocks(program))

    program[0] = 2
    fmt.Println("Part 2:", playGame(program))
}
