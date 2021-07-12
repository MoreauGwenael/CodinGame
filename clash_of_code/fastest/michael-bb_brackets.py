import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()

a = []
r = True
for i in t:
    if i in '([':
        a.append(i)
    elif i == ')':
        if len(a) > 0 and a[-1] == '(':
            a.pop()
        else:
            r = False
    elif i == ']':
        if len(a) > 0 and a[-1] == '[':
            a.pop()
        else:
            r = False
print(str(len(a) == 0 and r).upper())
