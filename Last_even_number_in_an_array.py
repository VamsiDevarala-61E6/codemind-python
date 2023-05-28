n=int(input())
l=list(map(int,input().split()))
v=[]
for i in l:
    if i%2==0:
        v.append(i)
print(v[-1])