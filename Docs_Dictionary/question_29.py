# Q29.Write a Python program to sort a list alphabetically in a dictionary.
# o/p:={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
dict={}
for key in sorted(num):
    # print(sorted(num[key]))
    dict[key]=sorted(num[key])
print(dict)






# a=[1,2,3,4,23,5,8,6,78]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#           a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
#     i=i+1
# print(a)
