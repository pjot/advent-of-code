package main

import "fmt"

type Thing struct {
	cost, damage, armor int
}

type Player struct {
	attack, armor, life int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func fight(items []Thing) (bool, int) {
	me := Player{0, 0, 100}
	cost := 0
	for _, t := range items {
		me.attack += t.damage
		me.armor += t.armor
		cost += t.cost
	}
	cpu := Player{8, 1, 104}
	for {
		d1 := max(me.attack-cpu.armor, 1)
		cpu.life -= d1
		if cpu.life <= 0 {
			return true, cost
		}

		d2 := max(cpu.attack-me.armor, 1)
		me.life -= d2
		if me.life <= 0 {
			return false, cost
		}
	}
	return false, cost
}

func main() {
	rings := []Thing{
		Thing{25, 1, 0},
		Thing{50, 2, 0},
		Thing{100, 3, 0},
		Thing{20, 0, 1},
		Thing{40, 0, 2},
		Thing{80, 0, 3},
		Thing{0, 0, 0},
		Thing{0, 0, 0},
	}
	weapons := []Thing{
		Thing{8, 4, 0},
		Thing{10, 5, 0},
		Thing{25, 6, 0},
		Thing{40, 7, 0},
		Thing{74, 8, 0},
	}
	armors := []Thing{
		Thing{13, 0, 1},
		Thing{31, 0, 2},
		Thing{53, 0, 3},
		Thing{75, 0, 4},
		Thing{102, 0, 5},
		Thing{0, 0, 0},
	}

	lowestWin := 999999
	highestLoss := 0
	for w := 0; w < len(weapons); w++ {
		for a := 0; a < len(armors); a++ {
			for r1 := 0; r1 < len(rings); r1++ {
				for r2 := r1 + 1; r2 < len(rings); r2++ {
					things := []Thing{
						weapons[w],
						armors[a],
						rings[r1],
						rings[r2],
					}
					win, cost := fight(things)
					if win && cost < lowestWin {
						lowestWin = cost
					}
					if !win && cost > highestLoss {
						highestLoss = cost
					}
				}
			}
		}
	}
	fmt.Println("Part 1:", lowestWin)
	fmt.Println("Part 2:", highestLoss)
}
