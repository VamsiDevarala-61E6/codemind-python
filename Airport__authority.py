n=int(input())
l=[]
for i in range(n):
    k=int(input())
    l.append(k)
t=int(input())
c=0
for i in l:
    if i<=t:
        c=c+1
    else:
        c=c+2
print(c)