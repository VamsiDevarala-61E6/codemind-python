t=int(input())
for _ in range(t):
    n=int(input())
    sq=n**0.5
    k=int(sq)
    f=sq-k
    if f==0:
        print("True")
    else:
        print("False")
    