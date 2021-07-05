import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input().upper()
letters = []
result = []
for i in range(h):
    letters.append(input())
    result.append("")
for i in t:
    for j in range(h):
        if ord(i) > 64 and ord(i) < 91:
            result[j] += letters[j][(ord(i)-65)*l:(ord(i)-65)*l+l]
        else:
            result[j] += letters[j][26*l:26*l+l]
for i in range(len(result)):
    print(result[i])
