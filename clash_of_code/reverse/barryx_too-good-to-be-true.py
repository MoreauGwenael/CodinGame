import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
text = input()

r = ""
i = 0
j = 1
k = 0

while j < n+1:
    if text[i] == '.':
        r += " "
        i = j
        j += 1
    else:
        r += text[i]
        i += n
        if i >= len(text):
            r += " "
            i = j
            j += 1
print(r[:-1])
