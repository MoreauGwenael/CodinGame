import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

y,m,d = map(int, input().split('/'))
t = sum(int(i) for i in str(y))
while len(str(t)) == 2:
    if str(t)[0] != str(t)[1]:
        t = sum(int(i) for i in str(t))
    else:
        break
if len(str(m)) == 2:
    if str(m)[0] != str(m)[1]:
        r = sum(int(i) for i in str(m))
    else:
        r = m
else:
    r = m
while len(str(r)) == 2:
    if str(r)[0] != str(r)[1]:
        r = sum(int(i) for i in str(r))
    else:
        break
if len(str(d)) == 2:
    if str(d)[0] != str(d)[1]:
        s = sum(int(i) for i in str(d))
    else:
        s = d
else:
    s = d
while len(str(s)) == 2:
    if str(s)[0] != str(s)[1]:
        s = sum(int(i) for i in str(s))
    else:
        break
u = t + r + s
while len(str(u)) == 2:
    if str(u)[0] != str(u)[1]:
        u = sum(int(i) for i in str(u))
    else:
        break
print(u)
