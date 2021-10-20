import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lines = []
n = int(input())
for i in range(n):
    lines.append(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for line in lines:
    stacks = []
    for container in line:
        container_int = ord(container)
        if container_int in stacks:
            continue
        best = 30
        for stack in stacks:
            if stack > container_int and stack - container_int < best:
                best = stack - container_int
        if best == 30:
            stacks.append(container_int)
        else:
            best_index = stacks.index(container_int + best)
            stacks[best_index] = container_int
    
    print(len(stacks))
