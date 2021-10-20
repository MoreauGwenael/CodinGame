import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

labels_top = input().split()

connectors = []
for i in range(h - 2):
    connectors.append(input().split('|')[1:-1])

labels_bottom = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(len(labels_top)):
    position = i
    new_position = position
    for j in range(len(connectors)):
        if position != 0:
            if connectors[j][position - 1] == '--':
                new_position -= 1
        if position != len(labels_top) - 1:
            if connectors[j][position] == '--':
                new_position += 1
        position = new_position
    print(labels_top[i] + labels_bottom[position])
