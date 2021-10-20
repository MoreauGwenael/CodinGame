import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def get_nb_neighboor(grid, x, y, h, w):
    nb = 0
    if x != 0:
        nb += int(grid[x-1][y] == 'O')
        if y != 0:
            nb += int(grid[x-1][y-1] == 'O')
        if y != w:
            nb += int(grid[x-1][y+1] == 'O')
    if x != h:
        nb += int(grid[x+1][y] == 'O')
        if y != 0:
            nb += int(grid[x+1][y-1] == 'O')
        if y != w:
            nb += int(grid[x+1][y+1] == 'O')
    if y != 0:
        nb += int(grid[x][y-1] == 'O')
    if y != w:
        nb += int(grid[x][y+1] == 'O')
    return nb


h, w, n = [int(i) for i in input().split()]
alive = input()
dead = input()
game = []
for i in range(h):
    game.append(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

nb_alive = []
nb_dead = []
for i in range(9):
    if alive[i] == '1':
        nb_alive.append(i)
    if dead[i] == '1':
        nb_dead.append(i)

for i in range(n):
    new_grid = []
    for j in range(h):
        line = ""
        for k in range(w):
            if game[j][k] == 'O':
                if get_nb_neighboor(game, j, k, h - 1, w - 1) in nb_alive:
                    line += 'O'
                else:
                    line += '.'
            else:
                if get_nb_neighboor(game, j, k, h - 1, w - 1) in nb_dead:
                    line += 'O'
                else:
                    line += '.'
        new_grid.append(line)
    game = new_grid

print('\n'.join(game))
