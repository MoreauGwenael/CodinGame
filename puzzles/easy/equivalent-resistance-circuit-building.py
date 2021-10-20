import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def serie(sentence, resistances):
    result = 0
    opens = 0
    circuit = sentence.split()
    subcircuit = []
    for i in circuit:
        if i in resistances.keys() and opens == 0:
            result += resistances[i]
        else:
            subcircuit.append(i)
            if i in '([':
                opens += 1
            elif i in ')]':
                opens -= 1
            if opens == 0 and i == ']':
                result += parallel(' '.join(subcircuit[1:-1]), resistances)
                subcircuit = []
            elif opens == 0 and i == ')':
                result += serie(' '.join(subcircuit[1:-1]), resistances)
                subcircuit = []
    return result

def parallel(sentence, resistances):
    result = 0
    opens = 0
    circuit = sentence.split()
    subcircuit = []
    for i in circuit:
        if i in resistances.keys() and opens == 0:
            result += 1 / resistances[i]
        else:
            subcircuit.append(i)
            if i in '([':
                opens += 1
            elif i in ')]':
                opens -= 1
            if opens == 0 and i == ']':
                result += 1 / parallel(' '.join(subcircuit[1:-1]), resistances)
                subcircuit = []
            elif opens == 0 and i == ')':
                result += 1 / serie(' '.join(subcircuit[1:-1]), resistances)
                subcircuit = []
    result = 1 / result
    return result


n = int(input())
resistances = {}
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    resistances[name] = r
circuit_full = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if circuit_full[0] == '(':
    print(float(round(serie(circuit_full[2:-2], resistances), 1)))
else:
    print(float(round(parallel(circuit_full[2:-2], resistances), 1)))
