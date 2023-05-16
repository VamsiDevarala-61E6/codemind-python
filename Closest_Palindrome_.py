def pali(n):
    t=n
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return t==r
n=int(input())
i=n+1
while(1):
    if pali(i)==True:
        fp=i
        break
    i=i+1
j=n-1
while(1):
    if pali(j)==True:
        bp=j
        break
    j=j-1
if (fp-n)>(n-bp):
    print(bp)
elif (fp-n)==(n-bp):
    print(bp,fp)
else:
    print(fp)
    
    