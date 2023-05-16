def rev(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r
n=int(input())
sq=n*n
rn=rev(n)
rsq=rn*rn
print(rev(rsq)==sq)