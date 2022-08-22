#O/P:- Dic={'a':[3,4,8],'b':[1,4,6],'c':[9,16,89]}
Dic={'a':[4,8,3],'b':[6,1,4],'c':[9,89,16]}
dict={}
for key in Dic:
    a=Dic[key]
    i=0
    while i<len(a):
        j=0
        while j<len(a)-1:
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            j=j+1
        i=i+1
    dict[key]=a
print(dict)
