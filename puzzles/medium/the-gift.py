import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
budgets = []
for i in range(n):
    budgets.append(int(input()))
budgets.sort()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if sum(budgets) < c:
    print("IMPOSSIBLE")
else:
    contributions = []
    while c != 0:
        if c/n > budgets[0]:
            contributions.append(budgets[0])
            c -= budgets[0]
            budgets.pop(0)
        else:
            contributions.append(c//n)
            c -= c//n
            budgets.pop(0)
        n -= 1
    print('\n'.join(list(map(str, contributions))))
