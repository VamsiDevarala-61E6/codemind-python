n=int(input())
ls=list(map(int,input().split()))
ind=0
for i in range(n-1,0,-1):
    if ls[i]%2!=0:
        ind=i
        break
print(ind)
        