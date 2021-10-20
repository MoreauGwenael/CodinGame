import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

laby = []

width, height = [int(i) for i in input().split()]

laby.append(list('#'*(width+2)))
for i in range(height):
    laby.append(['#'] + list(input()) + ['#'])
laby.append(list('#'*(width+2)))

side = input()

if side == "R":
    laby = [e[::-1] for e in laby]

start = (None, None)
for i in range(height):
    for j in range(width):
        if laby[i+1][j+1] not in '0#':
            start = (i+1, j+1)
pos_x, pos_y = start

direction = None
current_cell = laby[start[0]][start[1]]
if current_cell == '>':
    if side == "R": direction = "L"
    else: direction = "R"
elif current_cell == 'v':
    direciton = "D"
elif current_cell == '<':
    if side == "R": direction = "R"
    else: direction = "L"
else:
    direction = "U"

trapped = False

if direction == "U":
    if laby[pos_x][pos_y-1] != "#":
        direction = "L"
    elif laby[pos_x-1][pos_y] != "#":
        direction = "U"
    elif laby[pos_x][pos_y+1] != "#":
        direction = "R"
    elif laby[pos_x+1][pos_y] != "#":
        direction = "D"
    else:
        trapped = True

elif direction == "L":
    if laby[pos_x+1][pos_y] != "#":
        direction = "D"
    elif laby[pos_x][pos_y-1] != "#":
        direction = "L"
    elif laby[pos_x-1][pos_y] != "#":
        direction = "U"
    elif laby[pos_x][pos_y+1] != "#":
        direction = "R"
    else:
        trapped = True

elif direction == "D":
    if laby[pos_x][pos_y+1] != "#":
        direction = "R"
    elif laby[pos_x+1][pos_y] != "#":
        direction = "D"
    elif laby[pos_x][pos_y-1] != "#":
        direction = "L"
    elif laby[pos_x-1][pos_y] != "#":
        direction = "U"
    else:
        trapped = True

else:
    if laby[pos_x-1][pos_y] != "#":
        direction = "U"
    elif laby[pos_x][pos_y+1] != "#":
        direction = "R"
    elif laby[pos_x+1][pos_y] != "#":
        direction = "D"
    elif laby[pos_x][pos_y-1] != "#":
        direction = "L"
    else:
        trapped = True

if trapped:
    laby[start[0]][start[1]] = '0'
    if side == "R":
        laby = [e[::-1] for e in laby]
    print('\n'.join(''.join(e[1:-1]) for e in laby[1:-1]))

else:
    if direction == "L":
        pos_y -= 1
    elif direction == "U":
        pos_x -= 1
    elif direction == "R":
        pos_y += 1
    else:
        pos_x += 1
    
    while (pos_x, pos_y) != start:
        laby[pos_x][pos_y] = str(int(laby[pos_x][pos_y]) + 1)

        if direction == "U":
            if laby[pos_x][pos_y-1] != "#":
                direction = "L"
            elif laby[pos_x-1][pos_y] != "#":
                direction = "U"
            elif laby[pos_x][pos_y+1] != "#":
                direction = "R"
            else:
                direction = "D"

        elif direction == "L":
            if laby[pos_x+1][pos_y] != "#":
                direction = "D"
            elif laby[pos_x][pos_y-1] != "#":
                direction = "L"
            elif laby[pos_x-1][pos_y] != "#":
                direction = "U"
            else:
                direction = "R"

        elif direction == "D":
            if laby[pos_x][pos_y+1] != "#":
                direction = "R"
            elif laby[pos_x+1][pos_y] != "#":
                direction = "D"
            elif laby[pos_x][pos_y-1] != "#":
                direction = "L"
            else:
                direction = "U"

        else:
            if laby[pos_x-1][pos_y] != "#":
                direction = "U"
            elif laby[pos_x][pos_y+1] != "#":
                direction = "R"
            elif laby[pos_x+1][pos_y] != "#":
                direction = "D"
            else:
                direction = "L"
        
        if direction == "L":
            pos_y -= 1
        elif direction == "U":
            pos_x -= 1
        elif direction == "R":
            pos_y += 1
        else:
            pos_x += 1

    laby[start[0]][start[1]] = '1'

    if side == "R":
        laby = [e[::-1] for e in laby]

    print('\n'.join(''.join(e[1:-1]) for e in laby[1:-1]))
