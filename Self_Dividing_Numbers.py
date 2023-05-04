a=int(input())
b=int(input())
sd=[]
def selfd(n):
    if '0' in list(str(n)):
        return False
    else:
        t=n
        n=str(n)
        for i in n:
            if int(n)%int(i)!=0:
                return False
        else:
            return True
for i in range(a,b+1):
    if selfd(i):
        sd.append(i)
for i in sd:
    print(i,end=' ')