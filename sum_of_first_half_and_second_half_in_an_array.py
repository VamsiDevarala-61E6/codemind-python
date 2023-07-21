n=int(input())
l=list(map(int,input().split()))
h=n//2
s=0
for i in range(h):
    s+=l[i]
v=0
for j in range(h,n):
    v+=l[j]
print(s)
print(v)
    