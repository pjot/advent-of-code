package main

import "fmt"

type Point struct {
	x, y int
}

type Grid map[Point]int

func hundred(i int) int {
	return (i % 1000) / 100
}

func powerLevel(p Point, serial int) int {
	rackId := p.x + 10
	var l = rackId * p.y
	l += serial
	l *= rackId
	l = hundred(l)
	return l - 5
}

func grid(serial int) Grid {
	g := make(Grid)
	for x := 0; x < 301; x++ {
		for y := 0; y < 301; y++ {
			point := Point{x, y}
			g[point] = powerLevel(point, serial)
		}
	}
	return g
}

func squareSum(grid Grid, a Point, size int) int {
	s := 0
	for x := a.x; x < a.x+size; x++ {
		for y := a.y; y < a.y+size; y++ {
			s += grid[Point{x, y}]
		}
	}
	return s
}

func largestPower(grid Grid, minSize, maxSize int) string {
	largest := Point{}
	value := 0
	size := 0
	for x := 0; x < 300-minSize; x++ {
		for y := 0; y < 300-minSize; y++ {
			for s := minSize; s <= maxSize; s++ {
				if x+s < 301 && y+s < 301 {
					point := Point{x, y}
					v := squareSum(grid, point, s)
					if v > value {
						largest = point
						value = v
						size = s
					}
				}
			}
		}
	}
	return fmt.Sprintf(
		"%d,%d,%d",
		largest.x,
		largest.y,
		size,
	)
}

func main() {
	grid := grid(8444)
	fmt.Println("Part 1:", largestPower(grid, 3, 3))
	fmt.Println("Part 2:", largestPower(grid, 12, 16))
}
