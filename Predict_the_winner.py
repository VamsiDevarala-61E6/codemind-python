n=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range(n):
    if(i%2==0):
        x+=l[i]
    else:
        y+=l[i]
a=abs(x-y)
if(a%4==0):
    print("X")
else:
    print("Y")