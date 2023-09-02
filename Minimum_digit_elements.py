n=int(input())
l=list(map(int,input().split()))
m=len(str(l[0]))
for i in l:
    m=min(m,len(str(i)))
c=0
for j in l:
    if(len(str(j))==m):
        c+=1
print(c)
#print(*l)    