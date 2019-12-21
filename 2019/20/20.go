package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type Grid map[Point]string

type Point struct {
	x, y int
}

func parseFile(fileName string) (Grid, Point) {
	data, _ := ioutil.ReadFile(fileName)
	grid := make(Grid)
	y := 0
	x := 0
	width := 0
	height := 0
	for _, line := range strings.Split(string(data), "\n") {
		x = 0
		for _, chr := range strings.Split(line, "") {
			grid[Point{x, y}] = chr
			x++
			width = x
		}
		y++
		height = y
	}
	return grid, Point{width, height}
}

func neighbours(x, y int) [4]Point {
	return [4]Point{
		Point{x + 1, y},
		Point{x - 1, y},
		Point{x, y + 1},
		Point{x, y - 1},
	}
}

func levelDelta(p, dimensions Point, recurse bool) int {
	if !recurse {
		return 0
	}
	xInner := 4 < p.x && p.x < dimensions.x-4
	yInner := 4 < p.y && p.y < dimensions.y-4
	if xInner && yInner {
		return 1
	} else {
		return -1
	}
}

type PortalMap map[Point]Point

func isPortal(c string) bool {
	return !strings.Contains("AZ .#", c)
}

func portalsIn(grid Grid) PortalMap {
	portals := make(map[string][]Point)
	for point, chr := range grid {
		if !isPortal(chr) {
			continue
		}
		if _, ok := portals[chr]; !ok {
			portals[chr] = []Point{}
		}
		portals[chr] = append(portals[chr], point)
	}
	output := make(PortalMap)
	for v, p := range portals {
		if len(p) != 2 {
			fmt.Println("bad len", len(p), v, p)
		}
		output[p[0]] = p[1]
		output[p[1]] = p[0]
	}
	return output
}

type Triple struct {
	x, y, level int
}
type Visited map[Triple]bool

func traverseMaze(recurse bool) int {
	grid, dimensions := parseFile("input.map")
	var start Triple
	for p, v := range grid {
		if v == "A" {
			start = Triple{p.x, p.y, 0}
		}
	}

	visited := make(Visited)
	horizon := []Triple{start}
	portals := portalsIn(grid)

	distance := 0
	for len(horizon) > 0 {
		newHorizon := []Triple{}
		distance++
		for _, p := range horizon {
			visited[p] = true
			for _, n := range neighbours(p.x, p.y) {
				np := Triple{n.x, n.y, p.level}
				if _, ok := visited[np]; ok {
					continue
				}
				if _, ok := grid[n]; !ok {
					continue
				}
				if grid[n] == "Z" && p.level == 0 {
					return distance
				}
				if grid[n] == "." {
					newHorizon = append(newHorizon, np)
				}
				if port, ok := portals[n]; ok {
					delta := levelDelta(n, dimensions, recurse)
					if 0 <= p.level+delta && p.level+delta < 100 {
						nextPoint := Triple{
							port.x,
							port.y,
							p.level + delta}
						newHorizon = append(newHorizon, nextPoint)
					}
				}
			}
		}
		horizon = newHorizon
	}
	return distance
}

func main() {
	fmt.Println("Part 1:", traverseMaze(false))
	fmt.Println("Part 2:", traverseMaze(true))
}
