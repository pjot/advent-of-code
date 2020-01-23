package main

import "fmt"
import "io/ioutil"
import "strings"

type Mapping map[string]string
type State map[int]string

func parseFile(fileName string) (State, Mapping) {
	state := make(State)
	for i := -5; i < 0; i++ {
		state[i] = "."
	}
	mapping := make(Mapping)
	data, _ := ioutil.ReadFile(fileName)
	for i, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		if i == 0 {
			p := strings.Split(line, " ")
			for k, c := range p[2] {
				state[k] = string(c)
			}
		}
		if i > 1 {
			p := strings.Split(line, " ")
			mapping[p[0]] = p[2]
		}
	}
	return state, mapping
}

func extract(state State, i int) string {
	s := ""
	for j := -2; j < 3; j++ {
		v, ok := state[i+j]
		if !ok {
			v = "."
		}
		s += v
	}
	return s
}

func iterate(state State, mapping Mapping) State {
	newState := make(State)
	for i := -5; i < len(state)-4; i++ {
		neighbourhood := extract(state, i)
		newValue, ok := mapping[neighbourhood]
		if !ok {
			newValue = "."
		}
		newState[i] = newValue
	}
	return newState
}

func draw(state State, iteration int) {
	fmt.Print(fmt.Sprintf("%2d:", iteration))
	for i := -5; i < len(state); i++ {
		fmt.Print(state[i])
	}
	fmt.Println(" ", score(state))
}

func score(state State) int {
	s := 0
	for k, v := range state {
		if v == "#" {
			s += k
		}
	}
	return s
}

func lateScore(rounds int) int {
	return rounds * 67
}

func main() {
	state, mapping := parseFile("input")
	for i := 1; i < 21; i++ {
		state = iterate(state, mapping)
	}
	fmt.Println("Part 1:", score(state))
	fmt.Println("Part 2:", lateScore(50000000000))
}
