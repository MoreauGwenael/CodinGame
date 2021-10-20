def z():return list(map(J,I().split(':')))
def x(a):return (a[0]*60+a[1])*60+a[2]
I,J=input,int
a=z()
b=z()
c=z()
a=x(a)-900
b=x(b)
c=x(c)+J(I())*J(I())*60
print("Yes"if a>b+c else"No")
