package main

import "fmt"
import "io/ioutil"
import "strconv"

func parse(file string) []int {
	numbers := []int{}
	data, _ := ioutil.ReadFile(file)
	for _, c := range string(data) {
		n, ok := strconv.Atoi(string(c))
		if ok == nil {
			numbers = append(numbers, n)
		}
	}
	return numbers
}

func checkSum(numbers []int, offset int) int {
	s := 0
	for i := 0; i < len(numbers); i++ {
		j := (i + offset) % len(numbers)
		if numbers[i] == numbers[j] {
			s += numbers[i]
		}
	}
	return s
}

func main() {
	numbers := parse("input")
	fmt.Println("Part 1:", checkSum(numbers, 1))
	fmt.Println("Part 2:", checkSum(numbers, int(len(numbers)/2)))
}
