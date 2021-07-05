import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
grid2 = ["" for i in range(width)]
for i in range(height):
    grid.append(input())  # width characters, each either 0 or .
    for j in range(width):
        grid2[j] += grid[-1][j]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
for i in range(height):
    for j in range(width):
        if grid[i][j] == '0':
            result = str(j) + ' ' + str(i)
            if j != width-1:
                if '0' in grid[i][j+1::]:
                    result += ' ' + str(j+1+grid[i][j+1::].index('0')) + ' ' + str(i)
                else:
                    result += ' -1 -1'
            else:
                result += ' -1 -1'
            if i != height-1:
                if '0' in grid2[j][i+1::]:
                    result += ' ' + str(j) + ' ' + str(i+1+grid2[j][i+1::].index('0'))
                else:
                    result += ' -1 -1'
            else:
                result += ' -1 -1'
            print(result)
