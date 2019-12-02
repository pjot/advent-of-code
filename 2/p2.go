package main

import "io/ioutil"
import "fmt"
import "strconv"
import "strings"

func handlePosition (p []int, pos int) ([]int, int) {
    op_code := p[pos]

    if op_code == 99 {
        return p, -1
    }

    a_pos := p[pos + 1]
    a := p[a_pos]
    b_pos := p[pos + 2]
    b := p[b_pos]
    c_pos := p[pos + 3]

    switch op_code {
        case 1:
            p[c_pos] = a + b
        case 2:
            p[c_pos] = a * b
    }

    return p, pos + 4
}

func parseFile (fileName string) []int {
    data, _ := ioutil.ReadFile(fileName)
    program := []int{}
    for _, s := range strings.Split(string(data), ",") {
        i, err := strconv.Atoi(strings.Trim(s, "\n"))
        if err == nil {
            program = append(program, i)
        }
    }
    return program
}

func run (program []int) []int {
    position := 0
    for position >= 0 {
        program, position = handlePosition(program, position)
    }
    return program
}

func inputProgram (noun, verb int) []int {
    program := parseFile("program.intcode")
    program[1] = noun
    program[2] = verb
    return program
}

func runUntil (answer int) (int, int) {
    for noun := 0; noun < 100; noun++ {
        for verb := 0; verb < 100; verb++ {
            memory := inputProgram(noun, verb)
            result := run(memory)
            if result[0] == answer {
                return noun, verb
            }
        }
    }
    return 0, 0
}

func main () {
    noun, verb := runUntil(19690720)
    fmt.Println(100 * noun + verb)
}
