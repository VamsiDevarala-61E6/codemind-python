def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
t=n
r=0
while(n!=0):
    r=r*10+n%10
    n=n//10
if prime(t) and prime(r):
    print("circular prime")
elif prime(t) and prime(r)!=True:
    print("prime but not a circular prime")
else:
    print("not prime")