package main

import "fmt"
import "strconv"
import "io/ioutil"
import "strings"

func sumInFile(file string) int {
	s := 0
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		s += numberSum(line)
	}
	return s
}

func numberSum(s string) int {
	sum := 0
	n := false
	curr := ""
	for i, c := range s {
		chr := string(c)
		switch chr {
		case "0", "1", "2", "3", "4", "5", "6", "7", "8", "9":
			if !n {
				if string(s[i-1]) == "-" {
					curr = "-"
				}
			}
			curr += chr
			n = true
		default:
			if n {
				num, _ := strconv.Atoi(curr)
				sum += num
				n = false
				curr = ""
			}
		}
	}
	return sum
}

func main() {
	fmt.Println("Part 1:", sumInFile("input"))
}
