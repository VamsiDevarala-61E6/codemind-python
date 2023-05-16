def rev(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r
def dia(n):
    t=rev(n)
    s=0
    c=0
    while(t!=0):
        x=(t%10)
        c=c+1
        s=s+x**c
        t=t//10
    print(s==n)
n=int(input())

dia(n)