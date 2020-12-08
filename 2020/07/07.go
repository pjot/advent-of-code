package main

import "fmt"
import "regexp"
import "io/ioutil"
import "strings"

//import "strconv"

var parentRegex = regexp.MustCompile("([a-z]+ [a-z]+) bags contain")
var childrenRegex = regexp.MustCompile("([0-9]+ [a-z]+ [a-z]+) bag")

type Record struct {
	bag   string
	count int
}

type Tree map[string][]string

func parents(tree Tree, bag string, seen map[string]bool) map[string]bool {
	for _, c := range tree[bag] {
		seen[c] = true
		for s, _ := range parents(tree, c, seen) {
			seen[s] = true
		}
	}
	return seen
}

func main() {
	data, _ := ioutil.ReadFile("small.txt")
	tree := make(Tree)
	for _, s := range strings.Split(string(data), "\n") {
		if len(s) == 0 {
			continue
		}
		parent := parentRegex.FindStringSubmatch(s)[1]
		tree[parent] = []string{}
		for _, match := range childrenRegex.FindAllStringSubmatch(s, -1) {
			parts := strings.SplitN(match[1], " ", 2)
			//count, _ := strconv.Atoi(parts[0])
			bag := parts[1]
			tree[parent] = append(tree[parent], bag)
		}
	}
	fmt.Println(tree)

}
