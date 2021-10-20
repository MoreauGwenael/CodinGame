import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())
lights = []
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == 'C':
            lights.append((i, j))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

result = 0
for i in range(n):
    for j in range(n):
        is_bright = False
        for light in lights:
            if max(abs(light[0]-i), abs(light[1]-j)) < l:
                is_bright = True
        if not is_bright:
            result += 1

print(result)
