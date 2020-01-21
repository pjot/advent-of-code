package main

import "fmt"
import "strings"
import "io/ioutil"

func parseFile(file string) string {
	molecules := []string{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		molecules = append(molecules, line)
	}
	return molecules[0]
}

func once(str string) string {
	alphabet := "qwertyuiopasdfghjklzxcvbnm"
	for _, r := range alphabet {
		s := string(r)
		u := strings.ToUpper(s)

		str = strings.ReplaceAll(str, s+u, "")
		str = strings.ReplaceAll(str, u+s, "")
	}
	return str
}

func iterate(str string) int {
	a := str
	b := ""
	for a != b {
		b = a
		a = once(b)
	}
	return len(a)
}

func bestWithout(str string) int {
	alphabet := "qwertyuiopasdfghjklzxcvbnm"
	best := 99999999
	for _, l := range alphabet {
		s := string(l)
		without := strings.ReplaceAll(str, s, "")
		without = strings.ReplaceAll(without, strings.ToUpper(s), "")
		cnt := iterate(without)
		if cnt < best {
			best = cnt
		}
	}
	return best
}

func main() {
	molecule := parseFile("input")
	fmt.Println("Part 1:", iterate(molecule))
	fmt.Println("Part 2:", bestWithout(molecule))
}
