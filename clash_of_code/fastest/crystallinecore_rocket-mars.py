import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dist, t, s, v = [int(i) for i in input().split()]

d=0
for i in range(t):
    d+=s
    s+=v
print(str(d>=dist).lower(), d)
