n=int(input())
ls=list(map(int,input().split()))
av=sum(ls)//n
c=0
for i in ls:
    if i>=av:
        c+=1
print(c)