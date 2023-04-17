r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
s1=0
for k in range(r):
        if k%2==0:
            s=s+sum(mat[k])
        else:
            s1=s1+sum(mat[k])
print(s,s1,end=' ')

    