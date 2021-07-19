import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sky = []
for i in range(n):
    row = input().replace('+','x').replace('o','x')
    sky.append(row)
a = ''.join(sky)
if len(a) == a.count('#'):
    print("BLINDED")
elif not a.count('x'):
    print("SEARCH")
else:
    for i in range(n):
        a = sky[i]
        for j in range(len(a)):
            if a[j] == 'x':
                print('('+str(j+1)+','+str(i+1)+')')
