# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=list(dict)


a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in a:
    for j in a:
        if a[i]>a[i]:
            a[i],a[i]=a[i],a[i]
        if a[j]>a[j]:
            a[j],a[j]=a[j],a[j]
print(a)



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




