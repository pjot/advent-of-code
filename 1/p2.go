package main

import "io/ioutil"
import "fmt"
import "strconv"
import "strings"
import "math"


func iterate (m int) int {
    return int(math.Floor(float64(m) / 3.0)) - 2
}

func fuelForMass (m int) int {
    total := 0
    for m > 0 {
        m = iterate(m)
        if m > 0 {
            total += m
        }
    }
    return total
}

func main () {
    data, _ := ioutil.ReadFile("masses.txt")

    fuel := 0
    for _, s := range strings.Split(string(data), "\n") {
        i, err := strconv.Atoi(s)
        if err == nil {
            fuel += fuelForMass(i)
        }
    }

    fmt.Println("total fuel", fuel)
}
