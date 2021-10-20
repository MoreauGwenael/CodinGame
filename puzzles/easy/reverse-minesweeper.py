import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def check_mines(grid, x, y):
    total = 0

    if x != 0:
        if grid[x-1][y] == 'x': total += 1
        if y != 0:
            if grid[x-1][y-1] == 'x': total += 1
        if y != w-1:
            if grid[x-1][y+1] == 'x': total += 1

    if x != h-1:
        if grid[x+1][y] == 'x': total += 1
        if y != 0:
            if grid[x+1][y-1] == 'x': total += 1
        if y != w-1:
            if grid[x+1][y+1] == 'x': total += 1

    if y != 0:
        if grid[x][y-1] == 'x': total += 1

    if y != w-1:
        if grid[x][y+1] == 'x': total += 1

    return total
        

w = int(input())
h = int(input())
minesweeper = []
for i in range(h):
    minesweeper.append(list(input()))

for i in range(w):
    for j in range(h):
        if minesweeper[j][i] != 'x':
            nb = check_mines(minesweeper, j, i)
            if nb != 0:
                minesweeper[j][i] = str(nb)

for i in range(w):
    for j in range(h):
        if minesweeper[j][i] == 'x':
            minesweeper[j][i] = '.'

print('\n'.join(''.join(e) for e in minesweeper))
