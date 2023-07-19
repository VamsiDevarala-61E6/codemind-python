def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    return c==0
n=int(input())
x=n
y=n
while(True):
    if prime(x):
        fp=x
        break
    x+=1
while(True):
    if prime(y):
        bp=y
        break
    y=y-1
if fp-n<n-bp:
    print(fp-n)
else:
    print(n-bp)