# O/P:-['2', '7', '9', '5', '1']
dic=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, 
 {"six":"9"},{"seven":"7"}]
i=0
b=[]
while i<len(dic):
    for j in dic[i]:
        if dic[i][j] not in b:
            b.append(dic[i][j])
        i=i+1
print(b)


# for i in a:
#     for j in i:
#         print(a[j])
