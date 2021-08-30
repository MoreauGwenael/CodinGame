import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

numbers = [""]*20
l, h = [int(i) for i in input().split()]
for i in range(h):
    numeral = input()
    for j in range(20):
        numbers[j] += numeral[:l] + '\n'
        numeral = numeral[l:]

s1 = int(input())
number_1 = 0
for i in range(s1 // h):
    digit = ""
    for j in range(h):
        digit += input() + "\n"
    number_1 += numbers.index(digit) * (20 ** (s1 // h - i - 1))

s2 = int(input())
number_2 = 0
for i in range(s2 // h):
    digit = ""
    for j in range(h):
        digit += input() + "\n"
    number_2 += numbers.index(digit) * (20 ** (s2 // h - i - 1))

operation = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if operation == '*':
    number = number_1 * number_2
elif operation == '/':
    number = number_1 // number_2
elif operation == '+':
    number = number_1 + number_2
else:
    number = number_1 - number_2

result = ""
if number == 0:
    result = numbers[0]
while number != 0:
    result = numbers[number % 20] + result
    number = number // 20

print(result)
