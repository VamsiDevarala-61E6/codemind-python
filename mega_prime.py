def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return c==2
n=int(input())
t=n
f=0
while(n!=0):
    x=n%10
    if prime(x)==True:
        f=f+1
    n=n//10
s=str(t)
l=len(s)

if l==f and prime(t)==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")