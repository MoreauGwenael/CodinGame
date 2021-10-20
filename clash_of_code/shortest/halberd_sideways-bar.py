import math
d=[]
n=int(input())
for i in range(n):x=int(input());d+=[x]
k=math.gcd(max(d),min(d)) 
e=[k]
for c in d:e+=[c//k*"-"]
for c in e:print(c)
