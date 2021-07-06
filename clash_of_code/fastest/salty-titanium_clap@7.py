import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

a = 0
for i in range(1,n+1):
    if i%7==0:a+=1
    elif '7' in str(i):a+=1
    elif sum(int(i) for i in str(i))%7==0:a+=1
print(a)
