import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
extensions = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    extensions[ext.upper()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    if len(fname.split('.')) == 1:
        print("UNKNOWN")
    elif fname.split('.')[-1].upper() in extensions.keys():
        print(extensions[fname.split('.')[-1].upper()])
    else:
        print("UNKNOWN")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
