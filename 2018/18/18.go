package main

import "fmt"
import "io/ioutil"
import "strings"

type GridPoint string

const (
	Lumberyard GridPoint = "#"
	Trees      GridPoint = "|"
	OpenGround GridPoint = "."
)

type Point struct {
	x, y int
}
type Grid map[Point]GridPoint

func parse(file string) Grid {
	grid := make(Grid)
	data, _ := ioutil.ReadFile(file)
	for y, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		for x, c := range line {
			v := Lumberyard
			switch string(c) {
			case "#":
				v = Lumberyard
			case "|":
				v = Trees
			case ".":
				v = OpenGround
			}
			grid[Point{x, y}] = v
		}
	}
	return grid
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func bounds(grid Grid) (Point, Point) {
	minimum := Point{9999, 9999}
	maximum := Point{-9999, -9999}
	for k, _ := range grid {
		minimum.x = min(k.x, minimum.x)
		minimum.y = min(k.y, minimum.y)
		maximum.x = max(k.x, maximum.x)
		maximum.y = max(k.y, maximum.y)
	}
	return minimum, maximum
}

func draw(grid Grid) {
	min, max := bounds(grid)
	for y := min.y; y <= max.y; y++ {
		for x := min.x; x <= max.x; x++ {
			fmt.Print(grid[Point{x, y}])
		}
		fmt.Println()
	}
	fmt.Println()
}

func neighbourCounts(p Point, grid Grid) map[GridPoint]int {
	counts := make(map[GridPoint]int)
	possible := []Point{
		Point{p.x + 1, p.y},
		Point{p.x, p.y + 1},
		Point{p.x - 1, p.y},
		Point{p.x, p.y - 1},
		Point{p.x + 1, p.y + 1},
		Point{p.x - 1, p.y + 1},
		Point{p.x + 1, p.y - 1},
		Point{p.x - 1, p.y - 1},
	}
	for _, p := range possible {
		if v, ok := grid[p]; ok {
			counts[v]++
		}
	}
	return counts
}

func iterate(grid Grid) Grid {
	next := make(Grid)
	for p, v := range grid {
		count := neighbourCounts(p, grid)
		nextPoint := v
		switch v {
		case OpenGround:
			if count[Trees] > 2 {
				nextPoint = Trees
			}
		case Trees:
			if count[Lumberyard] > 2 {
				nextPoint = Lumberyard
			}
		case Lumberyard:
			if count[Lumberyard] == 0 || count[Trees] == 0 {
				nextPoint = OpenGround
			}
		}
		next[p] = nextPoint
	}
	return next
}

func value(grid Grid) int {
	lumberyards := 0
	trees := 0
	for _, v := range grid {
		switch v {
		case Lumberyard:
			lumberyards++
		case Trees:
			trees++
		}
	}
	return lumberyards * trees
}

func run(iterations int) int {
	// Optimization because the pattern starts to repeat
	a := 440
	b := 475
	period := b - a
	rounds := ((iterations - b) % period) + a
	if iterations > b {
		iterations = rounds
	}

	grid := parse("input")
	for i := 1; i < iterations+1; i++ {
		grid = iterate(grid)
	}
	return value(grid)
}

func main() {
	fmt.Println("Part 1:", run(10))
	fmt.Println("Part 2:", run(1000000000))
}
