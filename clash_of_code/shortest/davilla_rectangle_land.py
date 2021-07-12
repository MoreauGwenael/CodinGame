G,I=abs,input
a,b=map(int,I().split())
c,d=map(int,I().split())
f=G(a-c)
h=G(b-d)
e=min(f,h)
I(round(.4*(h-e)+.3*(f-e)+.5*e,2))
