r,s=map(int,open(0))
t=[s]
y=[0]
for x in range(r):
 print(*t)
 t=[l+k for l,k in zip(t+y,y+t)]
