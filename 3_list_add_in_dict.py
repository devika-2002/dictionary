# #  out put  [160, 235, 270]
a={"jay":[45,25,30],"devika":[45,100,80],"love":[40,60,90],"laxmi":[30,50,70]}
l=[]
for i in a:
    for j in range(len(a[i])):
        if not l:
            l=[0]*len(a[i])
        l[j]+=a[i][j]
print(l)

