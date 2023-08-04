def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    return c==0
n=int(input())
r=0
k=n
while(n!=0):
    r=r*10+n%10
    n=n//10
if prime(k) and prime(r):
    print("circular prime")
elif prime(k):
    print("prime but not a circular prime")
else:
    print("not prime")