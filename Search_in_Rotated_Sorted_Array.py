n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l:
    if i==k:
        print(l.index(i))
        break
else:
    print(-1)
        