def pali(n):
    r=0
    t=n
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r==t
n=int(input())
fp=n+1
bp=n-1
while(True):
    if pali(fp):
        fp=fp
        break
    fp=fp+1
while(True):
    if pali(bp):
        bp=bp
        break
    bp=bp-1
if n-bp>fp-n:
    print(fp)
elif n-bp<fp-n:
    print(bp)
else:
    print(bp,fp)