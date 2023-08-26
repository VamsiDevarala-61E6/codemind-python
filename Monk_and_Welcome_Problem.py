n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
v=[]
for i in range(n):
    v.append(l[i]+l1[i])
print(*v)