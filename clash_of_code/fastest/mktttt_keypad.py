import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = input()

d={(1,'R'):5,(1,'U'):11,(1,'L'):0,(1,'D'):0
  ,(2,'R'):3,(2,'U'):13,(2,'L'):1,(2,'D'):0
  ,(3,'R'):0,(3,'U'):15,(3,'L'):3,(3,'D'):0
  ,(4,'R'):11,(4,'U'):7,(4,'L'):0,(4,'D'):1
  ,(5,'R'):6,(5,'U'):8,(5,'L'):4,(5,'D'):2
  ,(6,'R'):0,(6,'U'):9,(6,'L'):9,(6,'D'):3
  ,(7,'R'):17,(7,'U'):0,(7,'L'):0,(7,'D'):5
  ,(8,'R'):9,(8,'U'):0,(8,'L'):7,(8,'D'):7
  ,(9,'R'):0,(9,'U'):0,(9,'L'):15,(9,'D'):9}

a=d[(n,s)]
if a==0:
    print("Nothing...")
else:
    print(a)
