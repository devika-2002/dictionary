# Q29.Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict ={ x: sorted(y) 
for x, y in num.items()}
print(sorted_dict)


# dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i, j in dict.items():
#     sorted_dict ={i:sorted(j)}
#     print(sorted_dict)

    



# a=[3,1,9,4,2]
# # a=[1,2,3,4,23,5,8,6,78]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#           a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
#     i=i+1
# print(a)

