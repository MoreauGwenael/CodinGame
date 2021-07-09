a=input()
r=1
c=0
for k in[[j for j in range(len(a))if a.startswith(i,j)]for i in input().split()]:
 for l in k:r*=l;c=1
print(r if c else "NONE")
