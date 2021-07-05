import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = math.radians(float(input().replace(',','.')))
lat = math.radians(float(input().replace(',','.')))
n = int(input())
liste = []
for i in range(n):
    defib = input().split(';')
    liste.append([defib[1], math.radians(float(defib[4].replace(',','.'))), math.radians(float(defib[5].replace(',','.')))])


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

distance = math.inf
for i in liste:
    tmpdistance = math.sqrt(math.pow((i[1]-lon)*math.cos((lat+i[2])/2),2)+math.pow(i[2]-lat,2))*6371
    if tmpdistance < distance:
        distance = tmpdistance
        location = i[0]
print(location)
