I,J=input,int
a=J(I())
b=list(map(J,I().split()))
for i in range(J(I())):
 for i in range(a-1):
  if b[i]>b[i+1]:b[i],b[i+1]=b[i+1],b[i]
print(*b)
