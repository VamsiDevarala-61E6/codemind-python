def pali(s):
    f=s[::-1]
    return s==f
t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    if pali(s):
        if n%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
