package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

func parse(file string) []int {
	buckets := []int{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		i, _ := strconv.Atoi(line)
		buckets = append(buckets, i)
	}
	return buckets
}

func combinations(length int) [][]int {
	combs := [][]int{}
	max := 1
	for i := 0; i < length; i++ {
		max *= 2
	}
	fmtstr := "%0" + strconv.Itoa(length) + "b"
	for i := 1; i < max; i++ {
		s := fmt.Sprintf(fmtstr, i)
		l := []int{}
		for _, c := range s {
			if string(c) == "1" {
				l = append(l, 1)
			} else {
				l = append(l, 0)
			}
		}
		combs = append(combs, l)
	}
	return combs
}

func isAtLimit(buckets, combination []int, limit int) (bool, int) {
	s := 0
	active := 0
	for i := 0; i < len(buckets); i++ {
		if combination[i] == 1 {
			active++
			s += buckets[i]
			if s > limit {
				return false, 0
			}
		}
	}
	return s == limit, active
}

func main() {
	buckets := parse("input")
	counts := make(map[int]int)
	for _, combination := range combinations(len(buckets)) {
		atLimit, count := isAtLimit(buckets, combination, 150)
		if atLimit {
			counts[count]++
		}
	}
	min := 9999
	sum := 0
	for n, count := range counts {
		if n < min {
			min = n
		}
		sum += count
	}
	fmt.Println("Part 1:", sum)
	fmt.Println("Part 2:", counts[min])
}
