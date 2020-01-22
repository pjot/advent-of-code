package main

import "fmt"
import "gopkg.in/karalabe/cookiejar.v1/collections/deque"

func rotate(d *deque.Deque, n int) {
	p := 0
	if n < 0 {
		p = -n
	} else {
		p = n
	}
	for i := 0; i < p; i++ {
		v := 0
		if n > 0 {
			v = d.PopRight().(int)
			d.PushLeft(v)
		} else {
			v = d.PopLeft().(int)
			d.PushRight(v)
		}
	}
}

func print(d *deque.Deque) {
	ds := []int{}
	for d.Size() > 0 {
		ds = append(ds, d.PopRight().(int))
	}
	fmt.Println(ds)
}

func highScoreAfter(players, n int) int {
	scores := make(map[int]int)
	marbles := deque.New()
	marbles.PushLeft(0)
	for i := 1; i <= n; i++ {
		if i%23 == 0 {
			rotate(marbles, -7)
			points := marbles.PopLeft().(int)
			scores[i%players] += points + i
			rotate(marbles, 1)
		} else {
			rotate(marbles, 1)
			marbles.PushLeft(i)
		}
	}
	for marbles.Right() != 0 {
		rotate(marbles, 1)
	}
	highest := 0
	for _, score := range scores {
		if score > highest {
			highest = score
		}
	}
	return highest
}

func main() {
	fmt.Println("Part 1:", highScoreAfter(419, 72164))
	fmt.Println("Part 2:", highScoreAfter(419, 72164*100))
}
