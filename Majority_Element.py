n=int(int(input()))
l=list(map(int,input().split()))
s=set(l)
mc=0
mq=0
for i in s:
    c=0
    for j in l:
        if i==j:
            c=c+1
    if c>mc:
        mc=c
        mq=i
print(mq)
    
            