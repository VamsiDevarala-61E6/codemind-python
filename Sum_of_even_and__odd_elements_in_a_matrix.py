r,c=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(r)]
es=0
os=0
for i in range(r):
   for j in range(c):
       if lst[i][j]%2==0:
           es+=lst[i][j]
       else:
           os+=lst[i][j]
print(es,os,end=' ')