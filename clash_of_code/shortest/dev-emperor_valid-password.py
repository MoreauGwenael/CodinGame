d=0
for i in range(int(input())):
 a=input().split();b,c=map(int,a[0].split('-'))
 if b<=a[2].count(a[1][0])<=c:d+=1
print(d)
