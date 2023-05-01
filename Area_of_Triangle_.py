a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
k=ar**0.5
print(f"{k:.2f}")