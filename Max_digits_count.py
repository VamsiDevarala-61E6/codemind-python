n=int(input())
l=list(map(int,input().split()))
m=1
for i in l:
    m=max(m,len(str(i)))
c=0
for j in l:
    if(len(str(j))==m):
        c+=1
print(c)
    