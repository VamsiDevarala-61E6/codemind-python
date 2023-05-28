t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    k=n*(n+1)//2
    print(k-s)