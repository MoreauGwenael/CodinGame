import sys
import math

def checkValue(arg, spreadsheet, i):
    if arg[0] == '$':
        ref = int(arg[1:])
        if ref < i:
            try:
                arg1 = int(spreadsheet[ref])
                return arg1
            except:
                return int(findValue(cellsInput[ref], spreadsheet, ref))
        else:
            return int(findValue(cellsInput[ref], spreadsheet, ref))
    else:
        try:
            return int(arg)
        except:
            return arg

def findValue(cell, spreadsheet, iteration):
    try:
        spreadsheet[iteration] - 2
        return spreadsheet[iteration]
    except:
        pass
    
    operation = cell[0]
    arg1 = cell[1]
    arg2 = cell[2]
    i = iteration

    if operation == 'SUB' and arg1 == arg2:
        return 0

    if arg1 == arg2:
        arg1 = checkValue(arg1, spreadsheet, i)
        arg2 = arg1
    else:
        arg1 = checkValue(arg1, spreadsheet, i)
        arg2 = checkValue(arg2, spreadsheet, i)
    
    if operation == 'VALUE':
        return arg1
    elif operation == 'ADD':
        return arg1 + arg2
    elif operation == 'SUB':
        return arg1 - arg2
    else:
        return arg1 * arg2


n = int(input())
cellsInput = [[] for i in range(n)]
spreadsheet = ['?' for i in range(n)]

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    cell = [operation, arg_1, arg_2]
    cellsInput[i] = cell
    if operation == 'VALUE' and arg_1[0] != '$':
        spreadsheet[i] = int(arg_1)

for i in range(n):
    spreadsheet[i] = findValue(cellsInput[i], spreadsheet, i)

print('\n'.join(str(e) for e in spreadsheet))
