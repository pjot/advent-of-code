package main

import "fmt"
import "strings"
import "io/ioutil"

type Point struct {
	x, y int
}
type Grid map[Point]int

func parse(file string) Grid {
	g := make(Grid)
	data, _ := ioutil.ReadFile(file)
	for y, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		for x, c := range strings.Trim(line, "\n") {
			s := string(c)
			if s == "#" {
				g[Point{x, y}] = 1
			} else {
				g[Point{x, y}] = 0
			}
		}
	}
	return g
}

func neighbours(p Point) []Point {
	return []Point{
		Point{p.x, p.y + 1},
		Point{p.x, p.y - 1},
		Point{p.x + 1, p.y},
		Point{p.x - 1, p.y},
		Point{p.x + 1, p.y + 1},
		Point{p.x - 1, p.y + 1},
		Point{p.x - 1, p.y - 1},
		Point{p.x + 1, p.y - 1},
	}
}

func iterate(grid Grid) Grid {
	g := make(Grid)
	for p, v := range grid {
		ns := 0
		for _, n := range neighbours(p) {
			nv, ok := grid[n]
			if ok && nv == 1 {
				ns++
			}
		}
		value := 0
		switch v {
		case 1:
			if ns == 2 || ns == 3 {
				value = 1
			}
		case 0:
			if ns == 3 {
				value = 1
			}
		}
		g[p] = value
	}
	return g
}

func activeAfter(grid Grid, iterations int) int {
	for i := 0; i < iterations; i++ {
		grid = iterate(grid)
	}
	a := 0
	for _, v := range grid {
		a += v
	}
	return a
}

func activeAfterLightUp(grid Grid, iterations int) int {
	grid = lightUpCorners(grid)
	for i := 0; i < iterations; i++ {
		grid = iterate(grid)
		grid = lightUpCorners(grid)
	}
	a := 0
	for _, v := range grid {
		a += v
	}
	return a
}

func lightUpCorners(grid Grid) Grid {
	max := 0
	for p, _ := range grid {
		if p.x > max {
			max = p.x
		}
	}
	grid[Point{0, 0}] = 1
	grid[Point{max, 0}] = 1
	grid[Point{0, max}] = 1
	grid[Point{max, max}] = 1
	return grid
}

func main() {
	g := parse("input")
	fmt.Println("Part 1:", activeAfter(g, 100))

	g = parse("input")
	fmt.Println("Part 2:", activeAfterLightUp(g, 100))
}
