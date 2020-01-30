package main

import "fmt"
import "io/ioutil"
import "strings"
import "math/rand"

type Replacements map[string][]string

func contains(rs []string, s string) bool {
	for _, r := range rs {
		if r == s {
			return true
		}
	}
	return false
}

func molecules(s string, replacements Replacements) []string {
	results := []string{}
	for i, c := range s {
		cc := string(c)
		rs, ok := replacements[cc]
		before := string(s[0:i])
		after := string(s[i+1:])
		if ok {
			for _, r := range rs {
				str := before + r + after
				if !contains(results, str) {
					results = append(results, str)
				}
			}
		}
	}
	return results
}

func shuffle(strs []string) []string {
	rand.Shuffle(len(strs), func(a, b int) {
		strs[a], strs[b] = strs[b], strs[a]
	})
	return strs
}

func countSteps(s string, replacements Replacements) int {
	count := 0
	mol := s
	froms := []string{}
	for from, _ := range replacements {
		froms = append(froms, from)
	}
	for len(mol) > 1 {
		start := mol
		for _, from := range froms {
			vs := replacements[from]
			for _, to := range vs {
				for {
					if strings.Contains(mol, to) {
						count++
						mol = strings.Replace(mol, to, from, 1)
					} else {
						break
					}
				}
			}
		}
		if start == mol {
			froms = shuffle(froms)
			mol = s
			count = 0
		}
	}
	return count
}

func parse(file string) (Replacements, string) {
	rs := make(Replacements)
	unit := ""
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		if strings.Contains(line, "=>") {
			p := strings.Split(line, " => ")
			f := p[0]
			t := p[1]
			rs[f] = append(rs[f], t)
		} else {
			unit = line
		}
	}
	return rs, unit
}

func main() {
	replacements, str := parse("input")

	res := molecules(str, replacements)
	fmt.Println("Part 1:", len(res))
	fmt.Println("Part 2:", countSteps(str, replacements))
}
