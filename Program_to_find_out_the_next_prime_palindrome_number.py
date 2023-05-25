def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def pali(n):
    t=n
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return t==r
n=int(input())
i=n+1
while(True):
    if prime(i)==True and pali(i)==True:
        print(i)
        break
    i=i+1
        