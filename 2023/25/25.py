import networkx
from collections import defaultdict
from itertools import combinations

graph = networkx.Graph()

with open("input") as f:
    for line in f.readlines():
        a, b = line.split(": ")
        for bs in b.split():
            graph.add_edge(a, bs)

for a, b in networkx.minimum_edge_cut(graph):
    graph.remove_edge(a, b)

a, b = networkx.connected_components(graph)

print("Part 1:", len(a) * len(b))
