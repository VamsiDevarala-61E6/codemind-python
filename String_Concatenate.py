s=input()
s1=input()
s2=s+s1
v=[]
for i in s2:
    v.append(i)
v.sort()
for i in v:
    print(i,end="")