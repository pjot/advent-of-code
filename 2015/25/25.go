package main

import "fmt"

func next(r, c int) (int, int) {
	if r == 1 {
		return c + 1, 1
	} else {
		return r - 1, c + 1
	}
}

func hash(h int) int {
	return (h * 252533) % 33554393
}

func hashAt(row, column, h int) int {
	r := 1
	c := 1
	for {
		if r == row && c == column {
			return h
		}
		r, c = next(r, c)
		h = hash(h)
	}
}

func main() {
	fmt.Println("Part 1:", hashAt(2947, 3029, 20151125))
}
