import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
p_beg = []
p_end = []
for i in range(n):
    beg, end = map(int, input().split())
    p_beg.append(beg)
    p_end.append(end)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

current = 0
painted = True

while current < l and len(p_beg) != 0:
    if current < min(p_beg):
        print(current, min(p_beg))
        painted = False
    current = p_end[p_beg.index(min(p_beg))]

    new_beg = []
    new_end = []
    for i in range(len(p_beg)):
        if p_end[i] > current:
            if p_beg[i] < current:
                new_beg.append(current)
            else:
                new_beg.append(p_beg[i])
            new_end.append(p_end[i])
    p_beg = new_beg
    p_end = new_end

if current < l:
    print(current, l)
    painted = False

if painted:
    print("All painted")
