import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def path(nodes, current):
    if current not in nodes.keys():
        return 1
    mx = 0
    for i in nodes[current]:
        mx = max(mx, path(nodes, i))
    return mx + 1

n = int(input())  # the number of relationships of influence
nodes = {}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in nodes.keys():
        nodes[x] = []
    nodes[x].append(y)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

mx = 0
for i in nodes.keys():
    mx = max(mx, path(nodes, i))

# The number of people involved in the longest succession of influences
print(mx)
