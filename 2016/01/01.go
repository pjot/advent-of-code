package main

import "fmt"
import "strings"
import "io/ioutil"
import "strconv"

type Step struct {
	direction string
	steps     int
}

type Point struct {
	x, y int
}

func parse(file string) []Step {
	steps := []Step{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(strings.Trim(string(data), "\n"), ", ") {
		if len(line) == 0 {
			continue
		}
		parts := strings.SplitN(line, "", 2)
		stepCount, _ := strconv.Atoi(parts[1])
		steps = append(steps, Step{parts[0], stepCount})
	}
	return steps
}

func turn(current, direction string) string {
	if direction == "R" {
		switch current {
		case "E":
			return "S"
		case "S":
			return "W"
		case "W":
			return "N"
		case "N":
			return "E"
		}
	} else {
		switch current {
		case "E":
			return "N"
		case "S":
			return "E"
		case "W":
			return "S"
		case "N":
			return "W"
		}
	}
	return ""
}

func follow(start Point, steps []Step) Point {
	direction := "E"
	for _, step := range steps {
		direction = turn(direction, step.direction)
		switch direction {
		case "E":
			start.x += step.steps
		case "W":
			start.x -= step.steps
		case "N":
			start.y += step.steps
		case "S":
			start.y -= step.steps
		}
	}
	return start
}

func contains(ps []Point, p Point) bool {
	for _, pp := range ps {
		if pp.x == p.x && pp.y == p.y {
			return true
		}
	}
	return false
}

func firstVisitTwice(start Point, steps []Step) Point {
	visited := []Point{}
	direction := "E"
	for _, step := range steps {
		direction = turn(direction, step.direction)
		for i := 0; i < step.steps; i++ {
			switch direction {
			case "E":
				start.x++
			case "W":
				start.x--
			case "N":
				start.y++
			case "S":
				start.y--
			}
			if contains(visited, start) {
				return start
			}
			visited = append(visited, start)
		}
	}
	return Point{-1, -1}
}

func main() {
	steps := parse("input.txt")
	end := follow(Point{0, 0}, steps)
	fmt.Println("Part 1:", end.x+end.y)

	vis := firstVisitTwice(Point{0, 0}, steps)
	fmt.Println("Part 2:", vis.x+vis.y)
}
