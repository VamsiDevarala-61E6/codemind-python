def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    return c==0
t=int(input())
for _ in range(t):
    n=int(input())
    i=n
    j=n
    while(True):
        if prime(i):
            fp=i
            break
        i=i+1
    while(True):
        if prime(j):
            bp=j
            break
        j=j-1
    if n-bp>fp-n:
        print(fp)
    else:
        print(bp)