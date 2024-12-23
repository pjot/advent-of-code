import networkx as nx

graph = nx.Graph()
with open("input") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        a, b = line.split("-")
        graph.add_edge(a, b)

one = 0
two = ""
largest = 0
for c in nx.enumerate_all_cliques(graph):
    if len(c) == 3 and any([n.startswith("t") for n in c]):
        one += 1

    if len(c) > largest:
        largest = len(c)
        two = ",".join(sorted(c))

print("Part 1:", one)
print("Part 2:", two)

