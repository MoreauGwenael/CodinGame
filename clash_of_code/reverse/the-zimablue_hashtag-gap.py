import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h, w = [int(i) for i in input().split()]
b = -1
a = -1
for i in range(h):
    line = input()
    if '#' in line and b == -1:
        b = i
        c = line.index('#')
    elif '#' in line:
        a = i
        d = line.index('#')
        break
if abs(c-d) == 1:
    print(a-b)
else:
    print(a-b,'/',abs(d-c))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
