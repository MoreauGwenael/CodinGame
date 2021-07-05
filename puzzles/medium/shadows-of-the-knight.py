import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
square = ((0, 0), (w, h))

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.

    if (bomb_dir == "U"): square = ((x,square[0][1]),(x,y))
    if (bomb_dir == "UR"): square = ((x,square[0][1]),(square[1][0],y))
    if (bomb_dir == "R"): square = ((x,y),(square[1][0],y))
    if (bomb_dir == "DR"): square = ((x,y),square[1])
    if (bomb_dir == "D"): square = ((x,y),(x,square[1][1]))
    if (bomb_dir == "DL"): square = ((square[0][0],y),(x,square[1][1]))
    if (bomb_dir == "L"): square = ((square[0][0],y),(x,y))
    if (bomb_dir == "UL"): square = (square[0],(x,y))
    
    x = math.floor((square[0][0]+square[1][0])/2)
    y = math.floor((square[0][1]+square[1][1])/2)
    
    print(x,y)
