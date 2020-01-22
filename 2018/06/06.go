package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

type Point struct {
	x, y int
}
type Grid map[Point]string

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
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

func parseFile(fileName string) Grid {
	g := make(Grid)
	data, _ := ioutil.ReadFile(fileName)
	for i, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		p := strings.Split(line, ", ")
		x, _ := strconv.Atoi(p[0])
		y, _ := strconv.Atoi(p[1])
		g[Point{x, y}] = strconv.Itoa(i)
	}
	return g
}

func distance(a, b Point) int {
	return abs(a.x-b.x) + abs(a.y-b.y)
}

func closestPoint(grid Grid, point Point) string {
	closest := []string{}
	minDistance := 99999

	for p, v := range grid {
		d := distance(p, point)
		if d == minDistance {
			closest = append(closest, v)
		}
		if d < minDistance {
			minDistance = d
			closest = []string{v}
		}
	}
	if len(closest) > 1 {
		return "."
	}
	return closest[0]
}

func distanceGrid(grid Grid) Grid {
	g := make(Grid)
	min, max := bounds(grid)
	for y := min.y; y <= max.y; y++ {
		for x := min.x; x <= max.x; x++ {
			p := Point{x, y}
			closest := closestPoint(grid, p)
			if closest != "." {
				g[p] = closest
			}
		}
	}
	return g
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

func contains(strs []string, s string) bool {
	for _, v := range strs {
		if v == s {
			return true
		}
	}
	return false
}

func values(grid Grid) []string {
	vs := []string{}
	for _, v := range grid {
		if !contains(vs, v) {
			vs = append(vs, v)
		}
	}
	return vs
}

func onEdge(grid Grid) []string {
	edges := []string{}
	min, max := bounds(grid)
	for x := min.x; x <= max.x; x++ {
		p1 := Point{x, min.y}
		v1 := grid[p1]
		if v1 != "." && !contains(edges, v1) {
			edges = append(edges, v1)
		}
		p2 := Point{x, max.y}
		v2 := grid[p2]
		if v2 != "." && !contains(edges, v2) {
			edges = append(edges, v2)
		}
	}
	for y := min.y; y <= max.y; y++ {
		p1 := Point{min.x, y}
		v1 := grid[p1]
		if v1 != "." && !contains(edges, v1) {
			edges = append(edges, v1)
		}
		p2 := Point{max.x, y}
		v2 := grid[p2]
		if v2 != "." && !contains(edges, v2) {
			edges = append(edges, v2)
		}
	}
	return edges
}

func draw(grid Grid) {
	min, max := bounds(grid)
	for y := min.y; y <= max.y; y++ {
		for x := min.x; x <= max.x; x++ {
			p := Point{x, y}
			v, ok := grid[p]
			if ok {
				fmt.Print(v)
			} else {
				fmt.Print(closestPoint(grid, p))
			}
		}
		fmt.Println()
	}
}

func size(grid Grid, k string) int {
	s := 0
	for _, v := range grid {
		if v == k {
			s++
		}
	}
	return s
}

func biggestArea(grid Grid) int {
	maxSize := 0
	exclude := onEdge(grid)
	vs := values(grid)
	for _, v := range vs {
		if contains(exclude, v) {
			continue
		}
		maxSize = max(maxSize, size(grid, v))
	}
	return maxSize
}

func distanceSum(grid Grid, p Point) int {
	s := 0
	for k, _ := range grid {
		s += distance(k, p)
	}
	return s
}

func pointsBelow(grid Grid, n int) int {
	cnt := 0
	min, max := bounds(grid)
	for y := min.y; y <= max.y; y++ {
		for x := min.x; x <= max.x; x++ {
			p := Point{x, y}
			if distanceSum(grid, p) < n {
				cnt++
			}
		}
	}
	return cnt
}

func main() {
	grid := parseFile("input")
	dg := distanceGrid(grid)
	fmt.Println("Part 1:", biggestArea(dg))
	fmt.Println("Part 2:", pointsBelow(grid, 10000))
}
