n=int(input())
ls=list(map(int,input().split()))
d=0
i=0
n1=n-1
k=0
while(k!=n):
    if ls[i]!=0:
        d=d+2**n1
    k=k+1
    n1=n1-1
    i=i+1
print(d)