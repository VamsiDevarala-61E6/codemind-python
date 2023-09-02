n=int(input())
l=list(map(int,input().split()))
m=1
for i in l:
    m=max(m,len(str(i)))
c=0
v=[]
for j in l:
    if(len(str(j))==m):
        v.append(j)
print(*v)
    