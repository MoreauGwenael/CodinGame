import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def word_valid(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        else:
            letters.pop(letters.index(letter))
    return True

def value(word):
    total = 0
    for letter in word:
        if letter in 'aeionrtlsu':
            total += 1
        elif letter in 'dg':
            total += 2
        elif letter in 'bcmp':
            total += 3
        elif letter in 'fhvwy':
            total += 4
        elif letter == 'k':
            total += 5
        elif letter in 'jx':
            total += 8
        else:
            total += 10
    return total

dictionnary = []
for i in range(int(input())):
    dictionnary.append(input())
letters = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

mx = 0
best_word = ""
for word in dictionnary:
    if word_valid(word, list(letters)):
        score = value(word)
        if score > mx:
            mx = score
            best_word = word

print(best_word)
