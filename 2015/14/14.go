package main

import "fmt"
import "io/ioutil"
import "strings"

type Reindeer struct {
	speed, stamina, rest int
	name                 string
}

func parse(file string) []Reindeer {
	reindeers := []Reindeer{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		var name string
		var speed, stamina, rest int
		if len(line) == 0 {
			continue
		}
		fmt.Sscanf(
			line,
			"%s can fly %d km/s for %d seconds, but then must rest for %d seconds.",
			&name, &speed, &stamina, &rest,
		)
		r := Reindeer{speed, stamina, rest, name}
		reindeers = append(reindeers, r)
	}
	return reindeers
}

func scores(reindeers []Reindeer, rounds int) map[string]int {
	scores := make(map[string]int)
	for _, r := range reindeers {
		scores[r.name] = distance(rounds, r.speed, r.stamina, r.rest)
	}
	return scores
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func divmod(a, b int) (int, int) {
	return a / b, a % b
}

func distance(time, speed, stamina, rest int) int {
	q, r := divmod(time, stamina+rest)
	return (q*stamina + min(r, stamina)) * speed
}

func highestScore(scores map[string]int) int {
	highest := 0
	for _, score := range scores {
		if score > highest {
			highest = score
		}
	}
	return highest
}

func winners(reindeers []Reindeer, round int) []string {
	scores := scores(reindeers, round)
	highest := highestScore(scores)
	winners := []string{}
	for reindeer, score := range scores {
		if score == highest {
			winners = append(winners, reindeer)
		}
	}
	return winners
}

func partOne(reindeers []Reindeer) int {
	max := 0
	for _, r := range reindeers {
		distance := distance(2504, r.speed, r.stamina, r.rest)
		if distance > max {
			max = distance
		}
	}
	return max
}

func partTwo(reindeers []Reindeer) int {
	points := make(map[string]int)
	for round := 1; round < 2504; round++ {
		winners := winners(reindeers, round)
		for _, winner := range winners {
			points[winner]++
		}
	}
	max := 0
	for _, score := range points {
		if score > max {
			max = score
		}
	}
	return max
}

func main() {
	reindeers := parse("input")
	fmt.Println("Part 1:", partOne(reindeers))
	fmt.Println("Part 2:", partTwo(reindeers))
}
