n=int(input())
l=list(map(int,input().split()))
v=0
for i in l:
    if l.count(i)==1:
        v=v+1
        print(i,end=" ")
if v==0:
    print("-1")
