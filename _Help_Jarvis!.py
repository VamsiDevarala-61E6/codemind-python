t=int(input())
for i in range(t):
    s=input()
    n=[]
    for i in s:
        n.append(int(i))
    n.sort()
    for j in range(len(n)-1):
        if abs(n[j]-n[j+1])!=1:
            print("NO")
            break
    else:
        print("YES")