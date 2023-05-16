def pali(n):
    t=n;
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    print(r==t)
n=int(input()) 
pali(n)