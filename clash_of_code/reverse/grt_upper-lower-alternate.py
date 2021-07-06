import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = len(s) % 2
print("".join(c.upper() if i % 2 == a else c.lower() for i, c in enumerate(s)))
