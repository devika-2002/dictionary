# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# b=list(a)
# i=0
# while i<len(b):
#     j=0
#     while j<len(b)-1:
#         if a[b[j]][1]>a[b[j+1]][1]:
#             temp=b[j]
#             b[j]=a[j+1]
#             b[j+1]=temp
#         j+=1
#     i+=1
# print(b)
          

a=[3,1,9,4,2]
# a=[1,2,3,4,23,5,8,6,78]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)



# for i in a:
#     for j in a:
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#         if a[j]<a[i]:
#             a[j],a[i]=a[i],a[j]
# print(a)


# for i in a:
#     for j in a:
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
#         if a[j]>a[i]:
#             a[j],a[i]=a[i],a[j]
# print(a)

# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# b=list(a)
# # print(b)
# i=0
# j=0
# while i<len(b):
#     if b[i]>b[j]:
#         b[i],b[j]=b[j],b[i]
#     elif b[j]>b[i]:
#         b[j],b[i]=b[i],b[j]
#     j=j+1
#     i=i+1
# print(b)
    
    

# # descending ka hai
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# e = {}
# for v in reversed(sorted(d.values())):
#     for k in d:
#         if d[k] == v and k not in e:
#             e.update({k:v})
# print(e)

# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# lst=[]
# for key in sorted(dic, key=dic.get, reverse=False):
#     lst.append((key, dic[key]))
# print('Dictionary in ascending order by value :' ,list(lst))

