I=input
n,m=map(int,I().split())
a=[]
for i in range(n):s,t=map(int,I().split());a.append((m-t)/s)
I(a.index(min(a)))
