def sq(n):
    p=0
    while(n!=0):
        x=n%10
        s=x*x
        p=p+s
        n=n//10
    return p
n=int(input())
t=sq(n)
f=0
while(t!=0):
    t=sq(t)
    if t<10:
        break
print(t==1 or t==2)