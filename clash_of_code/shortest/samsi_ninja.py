m,a,n=map(int,input().split())
print(max(0,sum(m*i for i in range(n+1))-a))