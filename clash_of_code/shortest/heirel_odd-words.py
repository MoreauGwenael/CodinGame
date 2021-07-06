print(sum(sum(ord(c)*c.isalpha()for c in w)%2for w in input().split()))
