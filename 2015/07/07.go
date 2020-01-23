package main

import "fmt"
import "io/ioutil"
import "strings"
import "strconv"

func makeInt(s string) int {
    i, _ := strconv.Atoi(s)
    return i
}

type Operator string
const (
    AND     Operator = "ADD"
    NUMAND  Operator = "NUMAND"
    OR      Operator = "OR"
    NUMOR   Operator = "NUMOR"
    LSHIFT  Operator = "LSHIFT"
    RSHIFT  Operator = "RSHIFT"
    NOT     Operator = "NOT"
    ASSIGN  Operator = "ASSIGN"
)

type Node struct {
    operator Operator
    deps []string
    amount int
}

func node(operator Operator, deps []string, amount int) *Node {
    n := new(Node)
    n.operator = operator
    n.deps = deps
    n.amount = amount
    return n
}

type Network map[string]*Node

type Values map[string]int

func parse(file string) (Network, Values) {
    n := make(Network)
    v := make(Values)
    data, _ := ioutil.ReadFile(file)
    for _, line := range strings.Split(string(data), "\n") {
        if len(line) == 0 {
            continue
        }
        p := strings.Split(line, " ")
        switch {
        case p[1] == "AND":
            val, err := strconv.Atoi(p[0])
            if err == nil {
                n[p[4]] = node(NUMAND, []string{p[2]}, val)
            } else {
                n[p[4]] = node(AND, []string{p[0], p[2]}, 0)
            }
        case p[1] == "OR":
            val, err := strconv.Atoi(p[0])
            if err == nil {
                n[p[4]] = node(NUMOR, []string{p[2]}, val)
            } else {
                n[p[4]] = node(OR, []string{p[0], p[2]}, 0)
            }
        case p[1] == "LSHIFT":
            n[p[4]] = node(LSHIFT, []string{p[0]}, makeInt(p[2]))
        case p[1] == "RSHIFT":
            n[p[4]] = node(RSHIFT, []string{p[0]}, makeInt(p[2]))
        case p[0] == "NOT":
            n[p[3]] = node(NOT, []string{p[1]}, 0)
        case p[1] == "->":
            val, err := strconv.Atoi(p[0])
            if err == nil {
                v[p[2]] = val
            } else {
                n[p[2]] = node(ASSIGN, []string{p[0]}, 0)
            }
        }
    }
    return n, v
}

func hasAllValues(deps []string, values Values) bool {
    for _, d := range deps {
        if _, ok := values[d]; !ok {
             return false
        }
    }
    return true
}

func evaluate(n *Node, values Values) int {
    switch n.operator {
        case AND:
            return values[n.deps[0]] & values[n.deps[1]]
        case NUMAND:
            return values[n.deps[0]] & n.amount
        case OR:
            return values[n.deps[0]] | values[n.deps[1]]
        case NUMOR:
            return values[n.deps[0]] | n.amount
        case LSHIFT:
            return values[n.deps[0]] << n.amount
        case RSHIFT:
            return values[n.deps[0]] >> n.amount
        case NOT:
            return 65535 ^ values[n.deps[0]]
        case ASSIGN:
            return values[n.deps[0]]
    }
    return 0
}

func iterate(network Network, values Values) Values {
    for k, node := range network {
        if _, ok := values[k]; ok {
            continue
        }
        if hasAllValues(node.deps, values) {
            values[k] = evaluate(node, values)
        }
    }
    return values
}

func signalOn(n string, net Network, vals Values) int {
    for {
        vals = iterate(net, vals)
        v, ok := vals[n]
        if ok {
            return v
        }
    }
    return -1
}

func partOne() int {
    net, vals := parse("input")
    return signalOn("a", net, vals)
}

func partTwo(n int) int {
    net, vals := parse("input")
    vals["b"] = n
    return signalOn("a", net, vals)
}

func main() {
    one := partOne()
    fmt.Println("Part 1:", one)
    fmt.Println("Part 2:", partTwo(one))
}
