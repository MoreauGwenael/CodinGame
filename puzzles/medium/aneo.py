import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def is_green(ig_speed, ig_distance, ig_duration):
    return math.floor((ig_distance*3.6/ig_speed)/ig_duration)%2==0

speed = int(input())
light_count = int(input())
lights = []
for i in range(light_count):
    lights.append([int(j) for j in input().split()])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

ok = False
while not ok:
    ok = True
    for i in lights:
        if not is_green(speed, i[0], i[1]):
            ok = False
    if ok == False:
        speed -= 1

print(speed)
