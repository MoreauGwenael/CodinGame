import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
n = int(input())
laby = []
for i in range(h):
    line = input()
    if 'O' in line:
        beg_x, beg_y = i, line.index('O')
        line = line.replace('O', '.')
    laby.append(list(line))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

x, y = beg_x, beg_y
direction = 0
loop = [(x, y, direction)]
turn = 0
looped = False

while turn < n and not looped:
    can_move = False
    while not can_move:
        if direction == 0:
            if laby[x-1][y] == '.':
                can_move = True
            else:
                direction = 1
        if direction == 1:
            if laby[x][y+1] == '.':
                can_move = True
            else:
                direction = 2
        if direction == 2:
            if laby[x+1][y] == '.':
                can_move = True
            else:
                direction = 3
        if direction == 3:
            if laby[x][y-1] == '.':
                can_move = True
            else:
                direction = 0
    
    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    else:
        y -= 1
    
    if (x, y, direction) in loop:
        looped = True
        loop_index = loop.index((x, y, direction))
    else:
        loop.append((x, y, direction))

if not looped:
    print(y, x)

else:
    loop_len = len(loop) - loop_index
    loop_end = (n - loop_index) % loop_len
    print(loop[loop_end + loop_index][1], loop[loop_end + loop_index][0])
