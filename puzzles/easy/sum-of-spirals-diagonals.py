import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
current = 1
result = 1

offset = n-1
count = 0

while current != n**2:
    if count == 4:
        offset -= 2
        count = 0
    
    current += offset
    result += current
    count += 1

print(result)
