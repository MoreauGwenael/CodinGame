import numpy
a,b=map(int,input().split())
c=[0]*b
e=[0]*b
for i in range(a):
 d=input()
 for j in range(0,len(d),6):
  if d[j]=='[':c[j//6]+=1
 for j in range(2,len(d),6):
  if d[j]=='[':e[j//6]+=1
f=[]
for i in range(b):
 f.append(e[i]-c[i])
print(sum(f))
print(numpy.prod(f))
