def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n=int(input())
n1=int(input())
i=1
while(1):
    if prime(n+n1+i)==True:
        print(i)
        break
    i=i+1