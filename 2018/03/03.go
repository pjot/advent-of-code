package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

type StringSet struct {
	_items map[string]bool
}

func (s *StringSet) contains(st string) bool {
	return s._items[st]
}

func (s *StringSet) add(st string) {
	s._items[st] = true
}

func (s *StringSet) len() int {
	return len(s._items)
}

func (s *StringSet) remove(st string) {
	delete(s._items, st)
}

func (s *StringSet) items() []string {
	ret := []string{}
	for k, _ := range s._items {
		ret = append(ret, k)
	}
	return ret
}

func newStringSet() *StringSet {
	s := new(StringSet)
	s._items = make(map[string]bool)
	return s
}

type Point struct {
	x, y int
}

type Grid map[Point][]string

func parseFile(file string) Grid {
	g := make(Grid)
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		p := strings.Split(line, " ")

		coords := strings.Trim(p[2], ":")
		c := strings.Split(coords, ",")
		x0, _ := strconv.Atoi(c[0])
		y0, _ := strconv.Atoi(c[1])

		dim := p[3]
		d := strings.Split(dim, "x")
		x1, _ := strconv.Atoi(d[0])
		y1, _ := strconv.Atoi(d[1])

		claimer := p[0]

		for x := x0; x < x0+x1; x++ {
			for y := y0; y < y0+y1; y++ {
				g[Point{x, y}] = append(g[Point{x, y}], claimer)
			}
		}
	}
	return g
}

func moreThanTwo(grid Grid) int {
	s := 0
	for _, claims := range grid {
		if len(claims) > 1 {
			s++
		}
	}
	return s
}

func uniqueClaims(grid Grid) *StringSet {
	unique := newStringSet()
	for _, claims := range grid {
		for _, c := range claims {
			unique.add(c)
		}
	}
	return unique
}

func alwaysAlone(grid Grid) string {
	claimers := uniqueClaims(grid)
	seen := newStringSet()
	for _, claims := range grid {
		if len(claims) != 1 {
			for _, k := range claims {
				seen.add(k)
			}
		}
	}
	for _, k := range claimers.items() {
		if !seen.contains(k) {
			return k
		}
	}
	return ""
}

func main() {
	grid := parseFile("input")
	fmt.Println("Part 1:", moreThanTwo(grid))
	fmt.Println("Part 2:", alwaysAlone(grid))
}
