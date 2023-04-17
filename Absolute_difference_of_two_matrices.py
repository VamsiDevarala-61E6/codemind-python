r=int(input())
lst=[list(map(int,input().split())) for i in range(r)]
lst1=[list(map(int,input().split())) for i in range(r)]
res = []
for i in range(r):
    x = []
    for j in range(r):
        l=abs(lst[i][j]-lst1[i][j])
        x.append(l)
    res.append(x)
for i in res:
    print(*i)