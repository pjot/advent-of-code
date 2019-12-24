package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type Point struct {
	x, y int
}
type Grid map[Point]string

func parseFile(fileName string) Grid {
	data, _ := ioutil.ReadFile(fileName)
	grid := make(Grid)
	for y, line := range strings.Split(string(data), "\n") {
		for x, char := range strings.Split(line, "") {
			grid[Point{x, y}] = char
		}
	}
	return grid
}

func neighbours(point Point) []Point {
	x := point.x
	y := point.y
	return []Point{
		Point{x + 1, y},
		Point{x - 1, y},
		Point{x, y + 1},
		Point{x, y - 1},
	}
}

func newValue(value string, bugs int) string {
	if value == "." && (bugs == 1 || bugs == 2) {
		return "#"
	}
	if value == "#" && bugs == 1 {
		return "#"
	}
	return "."
}

func iterateSingle(grid Grid) Grid {
	new := make(Grid)
	for point, value := range grid {
		bugs := 0
		for _, n := range neighbours(point) {
			if val, ok := grid[n]; ok {
				if val == "#" {
					bugs++
				}
			}
		}
		new[point] = newValue(value, bugs)
	}
	return new
}

func biodiversity(grid Grid) int {
	multiplier := 1
	value := 0
	for y := 0; y < 5; y++ {
		for x := 0; x < 5; x++ {
			if grid[Point{x, y}] == "#" {
				value += multiplier
			}
			multiplier *= 2
		}
	}
	return value
}

func firstRepeating(grid Grid) int {
	seen := make(map[int]bool)
	for {
		grid = iterateSingle(grid)
		bd := biodiversity(grid)
		if _, ok := seen[bd]; ok {
			return bd
		}
		seen[bd] = true
	}
}

func partOne() int {
	grid := parseFile("input.map")
	return firstRepeating(grid)
}

func main() {
	fmt.Println("Part 1:", partOne())
}
