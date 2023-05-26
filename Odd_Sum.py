n=int(input())
l=list(map(int,input().split()))
s1=0
for i in l:
    if i%2!=0:
        s1+=i
print(s1)