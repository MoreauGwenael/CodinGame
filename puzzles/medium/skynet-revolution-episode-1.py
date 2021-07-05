import sys
import math
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    
    def del_edge(self, from_node, to_node):
        self.distances[(from_node, to_node)] = 9999
        self.distances[(to_node, from_node)] = 9999

def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        
        if min_node is None:
            break
        
        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    
    return visited, path

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

g = Graph()
gw = []

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(n):
    g.add_node(i)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    g.add_edge(n1, n2, 1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gw.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    
    (distances, path) = dijsktra(g, si)
    low = 9999
    for i in range(e):
        if (distances[gw[i]] < low):
            low = distances[gw[i]]
            nearest = gw[i]
    fastpath = path[nearest]
    g.del_edge(fastpath, nearest)
    print(fastpath, nearest)
