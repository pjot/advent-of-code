package main

import "fmt"
import "math"

func divisors(n int) []int {
	ds := []int{}
	limit := int(math.Sqrt(float64(n))) + 1
	for i := 1; i < limit; i++ {
		if n%i == 0 {
			ds = append(ds, i)
			if n/i != i {
				ds = append(ds, n/i)
			}
		}
	}
	return ds
}

func firstAbove(n, increment int) int {
	for i := 1; i < 10000000; i++ {
		p := 0
		for _, n := range divisors(i) {
			p += n * increment
		}
		if p >= n {
			return i
		}
	}
	return 0
}

func divisors2(n int) []int {
	i := 1
	ds := []int{}
	for {
		if n%i == 0 {
			ds = append(ds, n/i)
		}
		i++
		if i > 50 || i*i > n {
			return ds
		}
	}
	return ds
}

func firstAbove2(n, increment int) int {
	for i := 1; i < 10000000; i++ {
		p := 0
		for _, n := range divisors2(i) {
			p += n * increment
		}
		if p >= n {
			return i
		}
	}
	return 0
}

func main() {
	fmt.Println("Part 1:", firstAbove(29000000, 10))
	fmt.Println("Part 2:", firstAbove2(29000000, 11))
}
