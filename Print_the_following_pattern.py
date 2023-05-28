n=int(input())
for i in range(1,n+1):
    t=i
    for j in range(1,n-i+2):
        print(t,end=' ')
        t+=1
    print( )