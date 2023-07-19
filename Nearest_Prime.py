def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    return c==0
t=int(input())
for _ in range(t):
    n=int(input())
    fp=n
    bp=n
    while(True):
        if prime(fp):
            f=fp
            break
        fp=fp+1
    while(True):
        if prime(bp):
            b=bp
            break
        bp=bp-1
    if f-n<n-b:
        print(f)
    else:
        print(b)