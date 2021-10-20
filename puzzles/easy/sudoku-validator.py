import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

grid = []
for i in range(9):
    grid.append(list(map(int, input().split())))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

is_ok = True
for i in range(9):
    if set(grid[i]) != set(range(1, 10)):
        is_ok = False

    if set([grid[j][i] for j in range(9)]) != set(range(1, 10)):
        is_ok = False
    
for i in range(3):
    for j in range(3):
        sub_grid = []
        for k in range(3):
            sub_grid += grid[3*i+k][3*j:3*j+3]
        if set(sub_grid) != set(range(1, 10)):
            is_ok = False

print(str(is_ok).lower())
