n=int(input())
s=0
p=1
t=n
while(n!=0):
    x=n%10
    s=s+x
    p=p*x
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")