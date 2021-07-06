v=0
I=input
exec("a,b,c=I().split();x,y=a.split('-');v+=int(x)<=c.count(b[0])<=int(y);"*int(I()))
I(v)