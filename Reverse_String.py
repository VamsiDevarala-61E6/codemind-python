s=input()
k=""
v=[]
for i in s:
    if i!=" ":
        k+=i
    elif i==" ":
        v.append(k)
        k=""
v.append(k)
v.reverse()
for j in v:
    print(j,end=" ")