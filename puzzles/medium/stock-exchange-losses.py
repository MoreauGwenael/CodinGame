import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
values = list(map(int, input().split()))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

mx = values[0]
mn = values[0]
greatest = 0
for i in values:
    if i > mx:
        greatest = min(greatest, mn - mx)
        mx = i
        mn = i
    mn = min(mn, i)
greatest = min(greatest, mn - mx)

print(greatest)
