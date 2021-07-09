for i in range(1,int(input())+1):
 r=""if i%5else"Foo"
 if not i%7:r+="Bar"
 print(r if r else i)
