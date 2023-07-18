n=int(input())
ls=list(map(int,input().split()))
l1=[]
l2=[]
for i in ls:
    if i%2!=0:
        l1.append(i)
    else:
        l2.append(i)
l3=l1+l2
for k in l3:
    print(k,end=" ")