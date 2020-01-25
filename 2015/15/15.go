package main

import "fmt"
import "io/ioutil"
import "strings"

type Ingredient struct {
	name                                            string
	capacity, durability, flavor, texture, calories int
}

func parse(file string) []Ingredient {
	ingredients := []Ingredient{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		var name string
		var capacity, durability, flavor, texture, calories int
		fmt.Sscanf(
			line,
			"%s capacity %d, durability %d, flavor %d, texture %d, calories %d",
			&name, &capacity, &durability, &flavor, &texture, &calories,
		)
		ingredients = append(
			ingredients,
			Ingredient{
				name, capacity, durability,
				flavor, texture, calories,
			},
		)
	}
	return ingredients
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func highest(ing []Ingredient) (int, int) {
	m := 0
	m500 := 0
	for a := 0; a < 101; a++ {
		for b := 0; b+a < 101; b++ {
			for c := 0; a+b+c < 101; c++ {
				for d := 0; a+b+c+d < 101; d++ {
					weights := []int{a, b, c, d}
					ca := 0
					du := 0
					fl := 0
					te := 0
					cal := 0
					for i, weight := range weights {
						ca += ing[i].capacity * weight
						du += ing[i].durability * weight
						fl += ing[i].flavor * weight
						te += ing[i].texture * weight
						cal += ing[i].calories * weight
					}
					ca = max(ca, 0)
					du = max(du, 0)
					fl = max(fl, 0)
					te = max(te, 0)
					score := ca * du * fl * te
					if score > m {
						m = score
					}
					if score > m500 && cal == 500 {
						m500 = score
					}
				}
			}
		}
	}
	return m, m500
}

func main() {
	ing := parse("input")
	one, two := highest(ing)
	fmt.Println("Part 1:", one)
	fmt.Println("Part 2:", two)
}
