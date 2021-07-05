import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

n = int(input())  # the number of cards for player 1
p1 = []
p2 = []
for i in range(n):
    cardp_1 = input()[:-1]  # the n cards of player 1
    p1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()[:-1]  # the m cards of player 2
    p2.append(cardp_2)
pat = False
b1 = []
b2 = []
turns = 0

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

while len(p1) and len(p2) and not pat:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if not len(b1):
        turns += 1
    if values.index(c1) > values.index(c2):
        if len(b1):
            for i in b1:
                p1.append(i)
            b1 = []
        p1.append(c1)
        if len(b2):
            for i in b2:
                p1.append(i)
            b2 = []
        p1.append(c2)
    elif values.index(c1) < values.index(c2):
        if len(b1):
            for i in b1:
                p2.append(i)
            b1 = []
        p2.append(c1)
        if len(b2):
            for i in b2:
                p2.append(i)
            b2 = []
        p2.append(c2)
    else:
        b1.append(c1)
        b2.append(c2)
        for i in range(3):
            if len(p1):
                b1.append(p1.pop(0))
            else:
                pat = True
            if len(p2):
                b2.append(p2.pop(0))
            else:
                pat = True
        if not len(p1) or not len(p2):
            pat = True

if pat:
    print("PAT")
elif not len(p2):
    print(1, turns)
else:
    print(2, turns)
