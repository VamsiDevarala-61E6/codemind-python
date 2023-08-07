n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if l.count(i)==1:
        p.append(i)
if len(p)>0:
    print(max(p))
else:
    print("-1")