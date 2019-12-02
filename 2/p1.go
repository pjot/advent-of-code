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

func main () {
    program := parseFile("program.intcode")
    program[1] = 12
    program[2] = 2
    fmt.Println(run(program)[0])
}
