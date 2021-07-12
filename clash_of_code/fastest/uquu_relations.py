import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
g = {}
for i in range(n):
    line = input()
    a,b,c = line[0], line[1], line[2]
    if b == "<": c,a = a,c
    if a not in g:
        g[a] = [c]
    else:
        g[a].append(c)
t = list(g.keys())
for i in g.keys():
    for j in g.values():
        if i in j:
            if i in t:
                t.pop(t.index(i))
t.sort()
print(' '.join(t))
