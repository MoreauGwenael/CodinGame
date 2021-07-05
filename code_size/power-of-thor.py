a,b,c,d=list(map(int,input().split()))
while True:
 s=""
 if b>d:s+='S';d+=1
 if b<d:s+='N';d-=1
 if a<c:s+='W';c-=1
 if a>c:s+='E';c+=1
 print(s)
