package main

import "fmt"

func next(pw []int) []int {
	for l := len(pw) - 1; l >= 0; l-- {
		if pw[l] < 26 {
			pw[l]++
			return pw
		} else {
			pw[l] = 1
		}
	}
	pw = append([]int{1}, pw...)
	return pw
}

func parse(s string) []int {
	pw := []int{}
	for _, c := range s {
		pw = append(pw, int(c)-96)
	}
	return pw
}

func unparse(pw []int) string {
	s := ""
	for _, i := range pw {
		s += string(i + 96)
	}
	return s
}

func hasBannedLetters(pw []int) bool {
	for _, i := range pw {
		switch i {
		case 9, 12, 15:
			return true
		}
	}
	return false
}

func hasIncreasingStraight(pw []int) bool {
	for i := 0; i < len(pw)-2; i++ {
		if pw[i]+1 == pw[i+1] && pw[i+1]+1 == pw[i+2] {
			return true
		}
	}
	return false
}

func hasTwoPairs(pw []int) bool {
	twos := 0
	curr := -1
	cnt := 0
	for _, c := range pw {
		if c == curr {
			cnt++
		} else {
			if cnt == 2 {
				twos++
			}
			cnt = 1
			curr = c
		}
	}
	if cnt == 2 {
		twos++
	}

	return twos > 1
}

func isSecure(pw []int) bool {
	if hasBannedLetters(pw) {
		return false
	}
	if !hasIncreasingStraight(pw) {
		return false
	}
	return hasTwoPairs(pw)
}

func nextPasswordAfter(pw []int) []int {
	for {
		pw = next(pw)
		if isSecure(pw) {
			return pw
		}
	}
}

func main() {
	pw := parse("cqjxjnds")

	pw = nextPasswordAfter(pw)
	fmt.Println("Part 1:", unparse(pw))

	pw = nextPasswordAfter(pw)
	fmt.Println("Part 2:", unparse(pw))
}
