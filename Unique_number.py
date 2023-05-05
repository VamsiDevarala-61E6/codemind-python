n=int(input())
s=str(n)
v=len(s)
p=set(s)
l=len(p)
if v==l:
    print("Unique Number")
else:
    print("Not Unique Number")