import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
chevaux = []
for i in range(n):
    chevaux.append(int(input()))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

chevaux.sort()
result = chevaux[1] - chevaux[0]
for i in range(2, len(chevaux)):
    if chevaux[i] - chevaux[i-1] < result:
        result = chevaux[i] - chevaux[i-1]
print(result)
