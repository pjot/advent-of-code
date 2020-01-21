package main

import "fmt"
import "io/ioutil"
import "strconv"
import "strings"

func parseFile(fileName string) []int {
	data, _ := ioutil.ReadFile(fileName)
	frequencies := []int{}
	for _, s := range strings.Split(string(data), "\n") {
		if i, err := strconv.Atoi(s); err == nil {
			frequencies = append(frequencies, i)
		}
	}
	return frequencies
}

func sum(numbers []int) int {
	s := 0
	for _, i := range numbers {
		s += i
	}
	return s
}

func firstDuplicate(numbers []int) int {
	sums := make(map[int]bool)
	i := 0
	c := 0
	l := len(numbers)
	for {
		c += numbers[i%l]
		if sums[c] {
			return c
		}
		sums[c] = true
		i++
	}
}

func main() {
	numbers := parseFile("input")
	fmt.Println("Part 1:", sum(numbers))
	fmt.Println("Part 2:", firstDuplicate(numbers))
}
