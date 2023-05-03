n=int(input())
s=str(n)
sq=n*n
st=str(sq)
new=st[len(st)//2::]
if s==new:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    