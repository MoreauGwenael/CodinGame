import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
laby = []
for i in range(h):
    laby.append(list(map(int, input().split())))
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

top = {1: "BOTTOM", 3: "BOTTOM", 4: "LEFT", 5: "RIGHT", 7: "BOTTOM", 9: "BOTTOM", 10: "LEFT", 11: "RIGHT"}
left = {1: "BOTTOM", 2: "RIGHT", 5: "BOTTOM", 6: "RIGHT", 8: "BOTTOM", 9: "BOTTOM", 13: "BOTTOM"}
right = {1: "BOTTOM", 2: "LEFT", 4: "BOTTOM", 6: "LEFT", 7: "BOTTOM", 8: "BOTTOM", 12: "BOTTOM"}

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    
    if pos == "TOP":
        next = top[laby[yi][xi]]
    elif pos == "LEFT":
        next = left[laby[yi][xi]]
    else:
        next = right[laby[yi][xi]]
    
    if next == "BOTTOM":
        yi += 1
    elif next == "LEFT":
        xi -= 1
    else:
        xi += 1
    
    print(xi, yi)
