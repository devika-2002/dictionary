# Q40. Write a Python program to convert more than one list to nested dictionary. 
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


serial_number=['S001', 'S002', 'S003', 'S004']
name_list=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
numbers_list=[85, 98, 89, 92]
dict={}
i=0
while i<len(serial_number):
    dict1={}
    dict1[name_list[i]]=numbers_list[i]
    dict[serial_number[i]] = dict1
    i=i+1
print(dict)

   
    

# x={}
# y={}
# z={}
# u={}
# v={}

# i=0
# while i<len(a):
#     x[b[0]]=c[0]
#     y[b[1]]=c[1]
#     z[b[2]]=c[2]
#     u[b[3]]=c[3]
#     v[a[0]]=x
#     v[a[1]]=y
#     v[a[2]]=z
#     v[a[3]]=u
#     i=i+1
# print(v)

# a=2//15-(4//2+4%5+12)%56/23+6**3
# print(a)

    
