import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

columns = []
sub_columns = []
rows = []
sub_rows = []

w, h, count_x, count_y = [int(i) for i in input().split()]
for i in list(map(int, input().split())) + [w]:
    for j in columns:
        sub_columns.append(i-j)
    columns.append(i)

for i in list(map(int, input().split())) + [h]:
    for j in rows:
        sub_rows.append(i-j)
    rows.append(i)

columns += sub_columns
rows += sub_rows

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

total = 0

for i in columns:
    total += rows.count(i)

print(total)
