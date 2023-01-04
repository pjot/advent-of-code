import strutils
import sets

type
    Node = object
        name: string
        weight: int
        children: seq[string]


proc parse(file: string): seq[Node] =
    let lines = splitlines (readfile file)
    for line in lines:
        var node = Node()
        node.weight = parseint(line.split("(")[1].split(")")[0])

        if "->" in line:
            let parts = line.split " -> "
        
            node.children = parts[1].split ", "
            node.name = parts[0].split[0]
        else:
            node.name = line.split[0]

        result.add(node)

proc parent(nodes: seq[Node], node: Node): Node =
    for n in nodes:
        if node.name in n.children:
            return n

    return node

proc top(nodes: seq[Node]): Node =
    var current = nodes[0]
    while true:
        let parent = nodes.parent current
        if parent == current:
            return current
        else:
            current = parent

proc weight(nodes: seq[Node], node: string): int =
    for n in nodes:
        if n.name == node:
            result.inc n.weight
            for child in n.children:
                result.inc nodes.weight child

proc target_weight(nodes: seq[Node], children: seq[string]): int =
    var seen = initHashSet[int]()
    for node in children:
        let weight = nodes.weight node
        if weight in seen:
            return weight
        seen.incl weight

proc get(nodes: seq[Node], node: string): Node =
    for n in nodes:
        if n.name == node:
            return n

proc is_balanced(nodes: seq[Node], children: seq[string]): bool =
    let target = nodes.target_weight children
    for node in children:
        let weight = nodes.weight node
        if weight != target:
            return false
    return true

proc correction(nodes: seq[Node], children: seq[string]): int =
    let target = nodes.target_weight children
    for node in children:
        let weight = nodes.weight node
        if weight != target:
            let unbalanced = nodes.get node
            if nodes.is_balanced unbalanced.children:
                return unbalanced.weight + target - weight 
            else:
                return nodes.correction unbalanced.children

let
    nodes = parse "input"
    top_node = top nodes

echo "Part 1: ", top_node.name
echo "Part 2: ", nodes.correction top_node.children
