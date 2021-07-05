import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

bytes = ''.join('{:07b}'.format(ord(x), 'b') for x in message)
if bytes[0] == '0':
    current = '0'
    result = "00"
else:
    current = '1'
    result = "0"
cnt = 1
for i in bytes[1:]:
    if i == current:
        cnt += 1
    else:
        result += " "+"0"*cnt
        cnt = 1
        if i == '0':
            current = '0'
            result += " 00"
        else:
            current = '1'
            result += " 0"
result += " "+"0"*cnt
print(result)
