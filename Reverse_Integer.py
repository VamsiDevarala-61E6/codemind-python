n=int(input())
if n>0:
    t=n
    r=0
    while n!=0:
        x=n%10
        r=(r*10)+x
        n=n//10
    print(r)
else:
    n=-1*n
    t=n
    r=0
    while n!=0:
        x=n%10
        r=(r*10)+x
        n=n//10
    print(-r)
    