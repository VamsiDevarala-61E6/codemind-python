def rsum(n):
    t=n
    r=0
    while n!=0:
        r=r*10+n%10
        n=n//10
    return t+r
def pali(n):
    t=n
    r=0
    while n!=0:
        r=r*10+n%10
        n=n//10
    return t==r
n=int(input())
while True:
    x=rsum(n)
    if pali(x):
        print(x)
        break
    else:
        n=rsum(x)
        