n=int(input())
l=list(map(int,input().split()))
k=l[:n//2:]
h=l[n//2::]
h.reverse()
for i in h+k:
    print(i,end=" ")