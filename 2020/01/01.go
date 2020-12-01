package main

import "io/ioutil"
import "fmt"
import "strconv"
import "strings"

func one(lines []int) int {
	for a := 0; a < len(lines); a++ {
		for b := a + 1; b < len(lines); b++ {
			if lines[a]+lines[b] == 2020 {
				return lines[a] * lines[b]
			}
		}
	}
	return 0
}

func two(lines []int) int {
	for a := 0; a < len(lines); a++ {
		for b := a + 1; b < len(lines); b++ {
			for c := b + 1; c < len(lines); c++ {
				if lines[a]+lines[b]+lines[c] == 2020 {
					return lines[a] * lines[b] * lines[c]
				}
			}
		}
	}
	return 0
}

func main() {
	data, _ := ioutil.ReadFile("input.txt")

	lines := []int{}
	for _, s := range strings.Split(string(data), "\n") {
		if i, err := strconv.Atoi(s); err == nil {
			lines = append(lines, i)
		}
	}

	fmt.Println("Part 1:", one(lines))
	fmt.Println("Part 2:", two(lines))
}
