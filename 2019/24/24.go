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

type RecursivePoint struct {
	x, y, level int
}

func recursiveNeighbours(point Point) []RecursivePoint {
	res := []RecursivePoint{}
	for _, n := range neighbours(point) {
		if n.x == 2 && n.y == 2 {
			continue
		}
		res = append(res, RecursivePoint{n.x, n.y, 0})
	}

	if point.x == 0 {
		res = append(res, RecursivePoint{1, 2, 1})
	}
	if point.y == 0 {
		res = append(res, RecursivePoint{2, 1, 1})
	}
	if point.y == 4 {
		res = append(res, RecursivePoint{2, 3, 1})
	}
	if point.x == 4 {
		res = append(res, RecursivePoint{3, 2, 1})
	}

	if point.x == 1 && point.y == 2 {
		for y := 0; y < 5; y++ {
			res = append(res, RecursivePoint{0, y, -1})
		}
	}
	if point.x == 2 && point.y == 1 {
		for x := 0; x < 5; x++ {
			res = append(res, RecursivePoint{x, 0, -1})
		}
	}
	if point.x == 3 && point.y == 2 {
		for y := 0; y < 5; y++ {
			res = append(res, RecursivePoint{4, y, -1})
		}
	}
	if point.x == 2 && point.y == 3 {
		for x := 0; x < 5; x++ {
			res = append(res, RecursivePoint{x, 4, -1})
		}
	}

	return res
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

func isBug(grids map[int]Grid, level int, p RecursivePoint) bool {
	grid, ok := grids[level+p.level]
	if !ok {
		return false
	}
	point := Point{p.x, p.y}
	value, ok := grid[point]
	if !ok {
		return false
	}
	return value == "#"
}

func iterateMultiple(grids map[int]Grid) map[int]Grid {
	new := make(map[int]Grid)
	for level, grid := range grids {
		new[level] = make(Grid)
		for point, value := range grid {
			if point.x == 2 && point.y == 2 {
				new[level][point] = "?"
				continue
			}
			bugs := 0
			for _, n := range recursiveNeighbours(point) {
				if isBug(grids, level, n) {
					bugs++
				}
			}
			new[level][point] = newValue(value, bugs)
		}
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

func emptyGrid() Grid {
	g := make(Grid)
	for x := 0; x < 5; x++ {
		for y := 0; y < 5; y++ {
			g[Point{x, y}] = "."
		}
	}
	return g
}

func countBugs(grids map[int]Grid) int {
	bugs := 0
	for _, grid := range grids {
		for _, value := range grid {
			if value == "#" {
				bugs++
			}
		}
	}
	return bugs
}

func partOne() int {
	grid := parseFile("input.map")
	return firstRepeating(grid)
}

func partTwo() int {
	grids := make(map[int]Grid)
	for level := -200; level < 201; level++ {
		grids[level] = emptyGrid()
	}
	grids[0] = parseFile("input2.map")

	for i := 0; i < 200; i++ {
		grids = iterateMultiple(grids)
	}
	return countBugs(grids)
}

func main() {
	fmt.Println("Part 1:", partOne())
	fmt.Println("Part 2:", partTwo())
}
