import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

parts = [0]
for i in b:
    if i == '1':
        parts[len(parts) - 1] += 1
    else:
        parts += [0]

best = 0
last = parts[0]
for i in parts[1:]:
    best = max(best, last + i)
    last = i

print(best + 1)
