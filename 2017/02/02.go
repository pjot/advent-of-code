package main

import "fmt"
import "io/ioutil"
import "strconv"
import "strings"

type Row []int

func parse(file string) []Row {
	rows := []Row{}
	data, _ := ioutil.ReadFile(file)
	for _, line := range strings.Split(string(data), "\n") {
		if len(line) == 0 {
			continue
		}
		row := []int{}
		for _, n := range strings.Split(line, "\t") {
			i, _ := strconv.Atoi(n)
			row = append(row, i)
		}
		rows = append(rows, row)
	}
	return rows
}

func minMax(row Row) (int, int) {
	min := 99999999999
	max := 0
	for _, n := range row {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}
	return min, max
}

func checkSum(rows []Row) int {
	s := 0
	for _, row := range rows {
		min, max := minMax(row)
		s += (max - min)
	}
	return s
}

func checkSumTwo(rows []Row) int {
	s := 0
	for _, row := range rows {
		s += rowSum(row)
	}
	return s
}

func rowSum(row Row) int {
	for a := 0; a < len(row); a++ {
		for b := a + 1; b < len(row); b++ {
			if row[a]%row[b] == 0 {
				return int(row[a] / row[b])
			}
			if row[b]%row[a] == 0 {
				return int(row[b] / row[a])
			}
		}
	}
	return 0
}

func main() {
	rows := parse("input")
	fmt.Println("Part 1:", checkSum(rows))
	fmt.Println("Part 2:", checkSumTwo(rows))
}
