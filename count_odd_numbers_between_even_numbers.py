n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if ls[i]%2==0 and ls[i+2]%2==0:
        if ls[i+1]%2!=0:
            c+=1
print(c)