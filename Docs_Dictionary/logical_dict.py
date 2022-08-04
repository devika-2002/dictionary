a={"list1":[7,8,9,1],"list2":[9,3,4,8],"list3":[9,4,2,1,9]}
d = []
for i in a.values():
    for j in i:
        if j not in d:
            d.append(j)
print(d)


        
        