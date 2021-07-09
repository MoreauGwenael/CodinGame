import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sentence = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

a = []
for i in range(n): a.append("")
b = 0
for i in sentence:
    a[b]+=i
    b+=1
    b%=n
c = max(len(i) for i in a)
for i in range(n):
    if len(a[i]) != c: a[i]+="x"
print(*a)
