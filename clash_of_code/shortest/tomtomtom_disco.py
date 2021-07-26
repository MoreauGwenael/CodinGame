x,y=0,0
for i in input().split():
 if i=="ts"and x>0:x-=1
 if i=="boom"and x<30:x+=1
 if i=="ding"and y>0:y-=1
 if i=="bing"and y<10:y+=1
print(x,y)
