# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
convert_list=list(dict)
dict1={}
i=0
while i<len(dict):
    if dict[convert_list[i]] is not None:
        dict1[convert_list[i]]=dict[convert_list[i]]
    i=i+1
print(dict1)


    

# a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# x={}
# for k, v in a.items():
#     if v!=None:
#         x[k]=v
# print(x)
