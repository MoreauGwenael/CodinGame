import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = input()
r = ""
for i in m:
    r += chr(ord(i) + len(m))
print(r)