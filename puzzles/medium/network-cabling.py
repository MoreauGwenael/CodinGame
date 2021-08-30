import sys
import math
from statistics import median

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
houses_x = []
houses_y = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    houses_x.append(x)
    houses_y.append(y)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

height = int(median(houses_y))
lenght = max(houses_x) - min(houses_x)
result = lenght + sum([abs(height - i) for i in houses_y])

print(result)
