n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
v=0
for i in l:
    if  i<a or i>b:
        v+=1
        print(i,end=" ")
if v==0:
    print(-1)

