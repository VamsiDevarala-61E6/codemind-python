r,c=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    s+=sum(lst[i])
print(s)