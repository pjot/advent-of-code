package main

import "fmt"
import "io/ioutil"
import "strings"

func parseStars(fileName string) [][]string {
	data, _ := ioutil.ReadFile(fileName)
	output := [][]string{}
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) > 0 {
			stars := strings.Split(line, ")")
			output = append(output, stars)
		}
	}
	return output
}

func main() {
	for _, stars := range parseStars("sm.txt") {
		inner := stars[0]
		outer := stars[1]
		fmt.Println("i", inner, "o", outer)
	}
}
