import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a=[]
for i in input().split():
    h = int(i)
    a.append(h)
h=0
l=0
q=a[0]
for i in a[1:]:
    if i>q:h+=1
    else:l+=1
    q=i
print(h,l)
