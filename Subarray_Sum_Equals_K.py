n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+l[j]
        if s==k:
            c=c+1
print(c)