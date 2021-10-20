import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, t1, t2, t3 = [int(i) for i in input().split()]
fraction = (t3 - t2) / (t2 - t1)
first_positions = {}
second_positions = {}
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    for j in range(w):
        if first_picture_row[j] != '.':
            first_positions[first_picture_row[j]] = (i, j)
        if second_picture_row[j] != '.':
            second_positions[second_picture_row[j]] = (i, j)

third_positions = {}
for i in first_positions.keys():
    x = math.floor((second_positions[i][0] - first_positions[i][0]) * fraction)
    y = math.floor((second_positions[i][1] - first_positions[i][1]) * fraction)
    third_positions[i] = (second_positions[i][0] + x, second_positions[i][1] + y)

final_picture = [['.' for i in range(w)] for j in range(h)]
asteroids = list(third_positions.keys())
asteroids.sort(reverse=True)
for i in asteroids:
    x, y = third_positions[i]
    if x >= 0 and x < h and y >= 0 and y < w:
        final_picture[x][y] = i
print('\n'.join(''.join(i) for i in final_picture))
