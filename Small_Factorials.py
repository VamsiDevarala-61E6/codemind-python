t=int(input())
for _ in range(t):
    n=int(input())
    p=1
    for i in range(n,1,-1):
        p=p*i
    print(p)