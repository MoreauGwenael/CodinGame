import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
cars = {}
for i in range(n):
    inputs = input().split()
    plate = inputs[0]
    radarname = inputs[1]
    timestamp = int(inputs[2])
    if plate not in cars.keys():
        cars[plate] = timestamp
    else:
        cars[plate] = int(13 / ((timestamp - cars[plate]) / 3600000))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

plates = list(cars.keys())
plates.sort()
for plate in plates:
    if cars[plate] > 130:
        print(plate, cars[plate])
