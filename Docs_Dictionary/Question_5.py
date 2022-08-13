# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
c=[]
for i in dict:
    c.append(dict[i])
    c.sort()
a={}
for j in c:
    for k in dict:
        if dict[k]==j:
            a[k]=j
print(a)

    
    
# print(sorted(d.items(), key=lambda x:x[1]))
# print(sorted(d.items(), key=lambda x:x[1], reverse=True ))
      


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




