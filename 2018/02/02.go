package main

import "fmt"
import "io/ioutil"
import "strings"

func parseFile(fileName string) []string {
	data, _ := ioutil.ReadFile(fileName)
	names := []string{}
	for _, s := range strings.Split(string(data), "\n") {
		names = append(names, s)
	}
	return names
}

func checksumParts(s string) (int, int) {
	letters := make(map[rune]bool)
	for _, l := range s {
		letters[l] = true
	}
	two := 0
	three := 0
	for r, _ := range letters {
		cnt := 0
		for _, l := range s {
			if l == r {
				cnt++
			}
		}
		switch cnt {
		case 2:
			two = 1
		case 3:
			three = 1
		}
	}
	return two, three
}

func checksum(names []string) int {
	twos := 0
	threes := 0
	for _, n := range names {
		two, three := checksumParts(n)
		twos += two
		threes += three
	}
	return twos * threes
}

func differsByOne(a, b string) bool {
	d := 0
	for i := range a {
		if a[i] != b[i] {
			d++
		}
		if d > 1 {
			return false
		}
	}
	return d == 1
}

func common(a, b string) string {
	s := ""
	for i := range a {
		if a[i] == b[i] {
			s += string(a[i])
		}
	}
	return s
}

func commonInMatch(names []string) string {
	l := len(names) - 1
	for a := 0; a < l; a++ {
		for b := a + 1; b < l; b++ {
			if differsByOne(names[a], names[b]) {
				return common(names[a], names[b])
			}
		}
	}
	return ""
}

func main() {
	names := parseFile("input")
	fmt.Println("Part 1:", checksum(names))
	fmt.Println("Part 2:", commonInMatch(names))
}
