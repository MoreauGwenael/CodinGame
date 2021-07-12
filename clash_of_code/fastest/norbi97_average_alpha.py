import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a={}
for i in range(n):
    s = input()
    cc=sum(ord(c)for c in s if c.isalpha())//len([c for c in s if c.isalpha()])
    if cc not in a:
        a[cc]=s

print(a[min(a.keys())][0]+a[max(a.keys())][-1])
