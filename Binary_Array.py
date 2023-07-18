n=int(input())
ls=list(map(int,input().split()))
f=0
for i in ls:
    if i==1 or i==0:
        f=1
    else:
        f=0
print(f==1)