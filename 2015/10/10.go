package main

import "fmt"
import "strconv"

func iterate(ns []int) []int {
	o := []int{}
	l := ns[0]
	cnt := 0
	for _, c := range ns {
		if c == l {
			cnt++
		} else {
			o = append(o, cnt)
			o = append(o, l)
			l = c
			cnt = 1
		}
	}
	o = append(o, cnt)
	o = append(o, l)
	return o
}

func parse(s string) []int {
	o := []int{}
	for _, c := range s {
		i, _ := strconv.Atoi(string(c))
		o = append(o, i)
	}
	return o
}

func main() {
	a := parse("1113122113")
	for i := 0; i < 40; i++ {
		a = iterate(a)
	}
	fmt.Println("Part 1:", len(a))
	for i := 0; i < 10; i++ {
		a = iterate(a)
	}
	fmt.Println("Part 2:", len(a))
}
