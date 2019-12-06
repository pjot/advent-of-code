package main

import "fmt"
import "io/ioutil"
import "strings"

func parseFile(fileName string) [][]string {
	data, _ := ioutil.ReadFile(fileName)
	output := [][]string{}
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) > 0 {
			stars := strings.Split(line, ")")
			output = append(output, stars)
		}
	}
	return output
}

type Nodes map[string]string

func orbitCount(node string, nodes Nodes) int {
	orbits := 0
	for {
		orbits++
		next, ok := nodes[node]
		if !ok {
			break
		}
		node = next
	}
	return orbits
}

func related(node string, nodes Nodes) []string {
	output := []string{nodes[node]}
	for _, n := range nodes {
		if nodes[n] == node {
			output = append(output, n)
		}
	}
	return output
}

func find(nodes Nodes) int {
	p := nodes["YOU"]
	visited := make(map[string]bool)
	steps, _ := search(p, nodes, visited, 0)
	return steps
}

func search(current string, nodes Nodes, visited map[string]bool, steps int) (int, bool) {
	visited[current] = true
	if current == nodes["SAN"] {
		return steps, true
	}
	for _, r := range related(current, nodes) {
		_, seen := visited[r]
		if !seen {
			s, done := search(r, nodes, visited, steps+1)
			if done {
				return s, true
			}
		}
	}
	return steps, false
}

func allOrbits(nodes Nodes) int {
	orbits := 0
	for _, node := range nodes {
		orbits += orbitCount(node, nodes)
	}
	return orbits
}

func main() {
	nodes := make(Nodes)
	for _, stars := range parseFile("starmap.txt") {
		inner := stars[0]
		outer := stars[1]
		nodes[outer] = inner
	}

	fmt.Println("part 1:", allOrbits(nodes))
	fmt.Println("part 2:", find(nodes))
}
