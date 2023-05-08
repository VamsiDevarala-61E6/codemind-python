def sq(n):
    p=0
    while(n!=0):
        x=n%10
        s=x*x
        p=p+s
        n=n//10
    return p
n=int(input())
while 1:
    if n<10:
        break
    n=sq(n) 
print(n==1 or n==7)