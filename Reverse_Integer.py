def rev(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r
n=int(input())
if n>0:
    print(rev(n))
else:
    x=-1*n
    t=rev(x)
    print(-1*t)