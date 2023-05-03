def dev(n):
    s=0
    for i in range(1,1+int(n/2)):
        if n%i==0:
            s=s+i
    return s
n=int(input())
m=int(input())
if dev(n)==m and dev(m)==n:
    print("Amicable")
else:
    print("Not Amicable")
