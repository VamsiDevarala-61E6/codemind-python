def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    return c==0
n=int(input())
l=list(map(int,input().split()))
v=[]
for i in l:
    if prime(i):
        v.append(i)
av=sum(v)/len(v)
print(f"{av:.2f}")