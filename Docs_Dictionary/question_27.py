# Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
i=0
sum=0
while i<len(student):
    dict=student[i]
    sum=sum+dict['id']
    i=i+1
print(sum)


# print(sum(d['id'] for d in student))

# i=0
# while i<len(student):
#     dict=student[i]
#     l=list(dict)
#     print(dict[i])
#     sum=0
#     j=0
#     while j<len(l):
#         sum[l]+=dict[l[j]]
#         j=j+1
#     print(sum)
#     i=i+1