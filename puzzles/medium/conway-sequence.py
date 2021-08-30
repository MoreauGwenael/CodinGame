import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = [int(input())]
l = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

iterations = 1
while iterations < l:
    serie = []
    number = r[0]
    times = 1
    for i in r[1:]:
        if  i == number:
            times += 1
        else:
            serie.append(times)
            serie.append(number)
            number = i
            times = 1
    serie.append(times)
    serie.append(number)
    r = serie
    iterations += 1

print(*r)
