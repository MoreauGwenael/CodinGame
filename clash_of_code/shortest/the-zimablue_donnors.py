a,b,c=[],[],[]
for i in range(int(input())):d,e,f=input().split();a.append(d);b.append(e);c.append(int(f))
d,e=input().split()
f,g=[],[]
for i in range(len(a)):
 if b[i]==d:f.append(a[i]);g.append(c[i])
for i in range(len(g)):g[i]=abs(g[i]-int(e))
if len(f):
 print("MOST COMPATIBLE DONOR :",f[g.index(min(g))])
 h=g.copy()
 h.sort()
 if len(f)>1:
  print("OTHER COMPATIBLE DONORS :")
  for i in h[1:]:
   print(f[g.index(i)])
else:
 if len(a):print("NO COMPATIBLE DONOR")
 else:print("NO DONOR AVAILABLE")
