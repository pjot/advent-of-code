package main

import "io/ioutil"
import "fmt"
import "strings"

func parseLine(line string) (int, int, string, string) {
	var a, b int
	var letter, password string
	fmt.Sscanf(line, "%d-%d %1s: %s", &a, &b, &letter, &password)
	return a, b, letter, password
}

func main() {
	data, _ := ioutil.ReadFile("input.txt")

	one := 0
	two := 0
	for _, s := range strings.Split(string(data), "\n") {
		a, b, letter, password := parseLine(s)
		if len(password) == 0 {
			continue
		}

		cnt := strings.Count(password, letter)
		if a <= cnt && cnt <= b {
			one++
		}

		aa := string(password[a-1])
		bb := string(password[b-1])
		if (aa == letter) != (bb == letter) {
			two++
		}
	}
	fmt.Println("Part 1:", one)
	fmt.Println("Part 2:", two)
}
