for _ in range(int(input())):
 a,b=map(int,input().split());b=b*(9/5)+32
 if a<b:print("Lower")
 elif a>b:print("Higher")
 else:print("Same")
 