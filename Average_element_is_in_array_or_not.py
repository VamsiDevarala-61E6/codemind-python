n=int(input())
l=list(map(int,input().split()))
k=sum(l)//n
for i in l:
    if k==i:
        print("True")
        break
else:
    print("False")