import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dice = []

for i in range(3):
    # One line out of three in the string describing the arrangement of the numbers.
    dice += list(map(int, list(input().split()[0])))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Output one of "right-handed", "left-handed" and "degenerate".
status = None
if dice[0] + dice[-1] != 7 or dice[1] + dice[3] != 7 or dice[2] + dice[4] != 7:
    status = "degenerate"

else:
    status = "left-handed"

    if dice[0] == 1:
        if dice[1] == 3 and dice[4] == 2 or "23" in ''.join(map(str, dice[1:5])):
            status = "right-handed"
    if dice[0] == 2:
        if dice[1] == 1 and dice[4] == 2 or "31" in ''.join(map(str, dice[1:5])):
            status = "right-handed"
    if dice[0] == 3:
        if dice[1] == 2 and dice[4] == 1 or "12" in ''.join(map(str, dice[1:5])):
            status = "right-handed"

    if dice[-1] == 1:
        if dice[1] == 2 and dice[4] == 3 or "32" in ''.join(map(str, dice[1:5])):
            status = "right-handed"
    if dice[-1] == 2:
        if dice[1] == 3 and dice[4] == 1 or "13" in ''.join(map(str, dice[1:5])):
            status = "right-handed"
    if dice[-1] == 3:
        if dice[1] == 1 and dice[4] == 2 or "21" in ''.join(map(str, dice[1:5])):
            status = "right-handed"

print(status)
