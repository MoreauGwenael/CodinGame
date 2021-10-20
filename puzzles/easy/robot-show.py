import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
bots = list(map(int, input().split()))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max(l - min(bots), max(bots)))
