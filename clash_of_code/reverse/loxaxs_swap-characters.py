import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
r = ""
for i in range(len(t)//2):
    r+=t[2*i+1]+t[2*i]
if len(t)%2:r+=t[-1]
print(r)
