import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

operation = input()
shift = int(input())
rotors = []
for i in range(3):
    rotors.append(input())
message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if operation == "DECODE":
    rotors = rotors[::-1]
    for rotor in rotors:
        new_message = ""
        for letter in message:
            new_message += chr(rotor.index(letter) + 65)
        message = new_message
    new_message = ""
    for letter in message:
        new_message += chr((ord(letter) - 65 - shift) % 26 + 65)
        shift += 1
    message = new_message
else:
    new_message = ""
    for letter in message:
        new_message += chr((ord(letter) - 65 + shift) % 26 + 65)
        shift += 1
    message = new_message
    for rotor in rotors:
        new_message = ""
        for letter in message:
            new_message += rotor[ord(letter)-65]
        message = new_message

print(message)
