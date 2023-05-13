import math
def sqr(n):
    s=int(math.sqrt(n))
    d=s*s
    v=d-n
    if v==0:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if sqr(i)==True:
        s=s+i
print(s)