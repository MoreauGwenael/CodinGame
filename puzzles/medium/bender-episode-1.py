import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

city = []
l, c = [int(i) for i in input().split()]
for i in range(l):
    city.append(list(input()))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(l):
    for j in range(c):
        if city[i][j] == '@':
            x, y = j, i
direction = 0
inversion = False
broker = False
direction_string = {0: "SOUTH", 1: "EAST", 2: "NORTH", 3: "WEST"}
blocked = False
moves = []
states = []
looped = False

while city[y][x] != '$':
    state = str(x) + '-' + str(y) + '-' + str(sum(i.count('X') for i in city)) + '-' + str(direction) + str(int(inversion)) + str(int(broker))
    if state in states and not blocked:
        looped = True
        break
    elif not blocked:
        states.append(state)

    if direction == 0:
        nx, ny = x, y + 1
    elif direction == 1:
        nx, ny = x + 1, y
    elif direction == 2:
        nx, ny = x, y - 1
    else:
        nx, ny = x - 1, y
    
    if city[ny][nx] == 'X' and broker:
        city[ny][nx] = ' '

    next_pos = city[ny][nx]

    if next_pos in 'X#':
        if not blocked:
            if inversion:
                direction = 0
            else:
                direction = 3
            blocked = True
        if inversion:
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        continue
    
    moves.append(direction_string[direction])

    blocked = False

    if next_pos == 'T':
        for i in range(l):
            for j in range(c):
                if city[i][j] == 'T' and not (ny == i and nx == j):
                    tx, ty = j, i
        nx, ny = tx, ty
    x, y = nx, ny

    if next_pos == 'I':
        inversion = not inversion
    
    if next_pos == 'B':
        broker = not broker
    
    if next_pos == 'S':
        direction = 0
    if next_pos == 'E':
        direction = 1
    if next_pos == 'N':
        direction = 2
    if next_pos == 'W':
        direction = 3

if looped:
    print("LOOP")
else:
    print('\n'.join(moves))
