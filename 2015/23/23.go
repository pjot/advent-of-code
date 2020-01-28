package main

import "fmt"
import "strings"
import "io/ioutil"
import "strconv"

type Instruction struct {
	code, register string
	value          int
}

type Registers map[string]int

func parse(file string) []Instruction {
	instructions := []Instruction{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		p := strings.Split(line, " ")
		switch p[0] {
		case "inc", "tpl", "hlf":
			instructions = append(
				instructions,
				Instruction{
					p[0],
					p[1],
					0,
				},
			)
		case "jie", "jio":
			i, _ := strconv.Atoi(p[2])
			instructions = append(
				instructions,
				Instruction{
					p[0],
					strings.Trim(p[1], ","),
					i,
				},
			)
		case "jmp":
			i, _ := strconv.Atoi(p[1])
			instructions = append(
				instructions,
				Instruction{
					p[0],
					"",
					i,
				},
			)
		}
	}
	return instructions
}

func run(program []Instruction, registers Registers) Registers {
	p := 0
	for {
		if p >= len(program) {
			return registers
		}
		i := program[p]
		switch i.code {
		case "hlf":
			registers[i.register] /= 2
			p++
		case "tpl":
			registers[i.register] *= 3
			p++
		case "inc":
			registers[i.register]++
			p++
		case "jmp":
			p += i.value
		case "jie":
			if registers[i.register]%2 == 0 {
				p += i.value
			} else {
				p++
			}
		case "jio":
			if registers[i.register] == 1 {
				p += i.value
			} else {
				p++
			}
		}
	}
}

func main() {
	program := parse("input")
	registers := make(Registers)
	registers["a"] = 0
	registers["b"] = 0
	after := run(program, registers)
	fmt.Println("Part 1:", after["b"])

	registers["a"] = 1
	registers["b"] = 0
	after = run(program, registers)
	fmt.Println("Part 2:", after["b"])
}
