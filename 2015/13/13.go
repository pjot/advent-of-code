package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

type Relation struct {
	a, b string
}

func contains(ns []string, n string) bool {
	for _, v := range ns {
		if v == n {
			return true
		}
	}
	return false
}

func parse(file string) (map[Relation]int, []string) {
	relations := make(map[Relation]int)
	people := []string{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		p := strings.Split(line, " ")
		a := p[0]
		b := strings.Trim(p[10], ".")
		sign := p[2]
		value, _ := strconv.Atoi(p[3])
		relation := Relation{a, b}
		if sign == "gain" {
			relations[relation] = value
		} else {
			relations[relation] = -value
		}
		if !contains(people, a) {
			people = append(people, a)
		}
	}
	return relations, people
}

// Stolen from internet
func permutations(arr []string) [][]string {
	var helper func([]string, int)
	res := [][]string{}

	helper = func(arr []string, n int) {
		if n == 1 {
			tmp := make([]string, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

func happiness(people []string, relations map[Relation]int) int {
	h := relations[Relation{people[len(people)-1], people[0]}]
	h += relations[Relation{people[0], people[len(people)-1]}]
	for i := 1; i < len(people); i++ {
		h += relations[Relation{people[i-1], people[i]}]
		h += relations[Relation{people[i], people[i-1]}]
	}
	return h
}

func highestHappiness(people []string, relations map[Relation]int) int {
	highest := 0
	for _, ps := range permutations(people) {
		curr := happiness(ps, relations)
		if curr > highest {
			highest = curr
		}
	}
	return highest
}

func main() {
	relations, people := parse("input")
	fmt.Println("Part 1:", highestHappiness(people, relations))

	for _, p := range people {
		relations[Relation{p, "me"}] = 0
		relations[Relation{"me", p}] = 0
	}
	people = append(people, "me")
	fmt.Println("Part 2:", highestHappiness(people, relations))
}
