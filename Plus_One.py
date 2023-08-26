n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s*10+i
k=s+1
v=str(k)
p=[]
for j in v:
    p.append(j)
for j in p:
    print(j,end=" ")
    