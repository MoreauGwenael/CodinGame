import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mn = input()

a = {1: ".----", 2: "..---", 3: "...--", 4: "....-", 5: ".....", 6: "-....", 7: "--...", 8: "---..", 9: "----.", 0: "-----"}

o = True
r = []
if len(mn) != 10: o = False
for i in mn:
    if i.isalpha(): o = False
    else: r.append(a[int(i)])
if o:
    print(' '.join(r))
else:
    print("Untransformable")
