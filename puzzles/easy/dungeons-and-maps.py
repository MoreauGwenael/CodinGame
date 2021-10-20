import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
maps = []
n = int(input())

for i in range(n):
    amap = []
    for j in range(h):
        amap.append(input())
    maps.append(amap)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

shortest_index = -1
shortest = w * h

for map_index in range(n):
    amap = maps[map_index]
    pos_row, pos_col = start_row, start_col
    path_len = 0
    visited_pos = []

    while amap[pos_row][pos_col] not in 'T.#' and (pos_row, pos_col) not in visited_pos:
        visited_pos.append((pos_row, pos_col))
        current_cell = amap[pos_row][pos_col]

        if current_cell == '^':
            if pos_row == 0:
                break
            pos_row -= 1
        elif current_cell == '>':
            if pos_col == w - 1:
                break
            pos_col += 1
        elif current_cell == 'v':
            if pos_row == h - 1:
                break
            pos_row += 1
        else:
            if pos_col == 0:
                break
            pos_col -= 1
            
        path_len += 1

    if amap[pos_row][pos_col] == 'T':
        if shortest > path_len:
            shortest = path_len
            shortest_index = map_index

if shortest_index == -1:
    print("TRAP")
else:
    print(shortest_index)
