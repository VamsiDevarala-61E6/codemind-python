def fact(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    return f
def dig(k):
    s=0
    while(k!=0):
        x=k%10
        s=s+fact(x)
        k=k//10
    return s
n=int(input())
if n==dig(n):
    print(f"The number {n} is a strong number")
else:
    print(f"The number {n} is not a strong number")
    
