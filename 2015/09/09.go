package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

type Distance struct {
	from, to string
}

func contains(pl []string, s string) bool {
	for _, v := range pl {
		if v == s {
			return true
		}
	}
	return false
}

func parse(file string) (map[Distance]int, []string) {
	distances := make(map[Distance]int)
	places := []string{}

	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		p := strings.Split(line, " ")
		d, _ := strconv.Atoi(p[4])

		d1 := Distance{p[0], p[2]}
		distances[d1] = d

		d2 := Distance{p[2], p[0]}
		distances[d2] = d

		if !contains(places, p[0]) {
			places = append(places, p[0])
		}
		if !contains(places, p[2]) {
			places = append(places, p[2])
		}
	}
	return distances, places
}

// Stolen from internet
func permutations(arr []string) [][]string {
	var helper func([]string, int)
	res := [][]string{}

	helper = func(arr []string, n int) {
		if n == 1 {
			tmp := make([]string, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

func main() {
	ds, places := parse("input")
	min := 9999999999999
	max := 0
	for _, perm := range permutations(places) {
		d := 0
		for i := 1; i < len(perm); i++ {
			d += ds[Distance{perm[i], perm[i-1]}]
		}
		if d < min {
			min = d
		}
		if d > max {
			max = d
		}
	}
	fmt.Println("Part 1:", min)
	fmt.Println("Part 2:", max)
}
