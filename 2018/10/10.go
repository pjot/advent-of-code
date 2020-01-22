package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

type Point struct {
	x, y, dx, dy int
}

func makeInt(s string) int {
	r, _ := strconv.Atoi(strings.Trim(s, " "))
	return r
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

func pointFromLine(line string) Point {
	p := strings.Split(line, "<")
	f := strings.Split(p[1], ",")
	x := makeInt(f[0])
	g := strings.Split(f[1], ">")
	y := makeInt(g[0])
	h := strings.Split(p[2], ",")
	dx := makeInt(h[0])
	dy := makeInt(strings.Trim(h[1], ">"))
	return Point{x, y, dx, dy}
}

func parseFile(fileName string) []Point {
	points := []Point{}
	data, _ := ioutil.ReadFile(fileName)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		points = append(points, pointFromLine(line))
	}
	return points
}

func update(points []Point) []Point {
	o := []Point{}
	for _, p := range points {
		o = append(o, Point{p.x + p.dx, p.y + p.dy, p.dx, p.dy})
	}
	return o
}

func size(points []Point) int {
	min, max := bounds(points)
	return (max.y - min.y) * (max.x - min.x)
}

func iterate(p []Point) ([]Point, int) {
	lastHeight := 9999999999999
	i := 0
	for {
		p2 := update(p)
		h := size(p2)
		if h > lastHeight {
			return p, i
		}
		p = p2
		lastHeight = h
		i++
	}
}

func bounds(points []Point) (Point, Point) {
	minimum := Point{999999, 999999, 0, 0}
	maximum := Point{-999999, -999999, 0, 0}
	for _, p := range points {
		minimum.x = min(p.x, minimum.x)
		minimum.y = min(p.y, minimum.y)
		maximum.x = max(p.x, maximum.x)
		maximum.y = max(p.y, maximum.y)
	}
	return minimum, maximum
}

func draw(points []Point) {
	min, max := bounds(points)
	for y := min.y; y < max.y+1; y++ {
		for x := min.x; x < max.x+1; x++ {
			char := " "
			for _, p := range points {
				if p.x == x && p.y == y {
					char = "#"
				}
			}
			fmt.Print(char)
		}
		fmt.Println()
	}
}

func main() {
	points := parseFile("input")
	finishedPoints, iterations := iterate(points)
	fmt.Println("Part 1:")
	draw(finishedPoints)
	fmt.Println("Part 2:", iterations)
}
