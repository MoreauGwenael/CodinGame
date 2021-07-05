n,m=int(input()),5527
for i in input().split():
 if abs(m)>abs(int(i)): m=int(i)
 elif m==int(i) and m<0: m=i
 elif abs(m)==abs(int(i)): m=abs(int(i))
if n==0: print(0)
else: print(m)
