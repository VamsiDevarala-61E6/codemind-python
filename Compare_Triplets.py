a=list(map(int,input().split()))
b=list(map(int,input().split()))
al=0
bo=0
for i in range(0,3):
    if a[i]>b[i]:
        al=al+1
    elif a[i]<b[i]:
        bo=bo+1
print(al,bo,sep=" ")