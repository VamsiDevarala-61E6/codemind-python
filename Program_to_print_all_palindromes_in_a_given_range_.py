def pali(n):
    t=n
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    if t==r:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if pali(i)==True:
        print(i,end=" ")