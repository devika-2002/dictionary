# # # Sample output: 5
# # dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# count=0
# for i in d.values():
#     for j in i:
#         count+=1
# print(count)

d= {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count = 0
a=list(d)
i=0
j=0
while i<len(a):
    while j<len(a[i]):
        count+=1
        j=j+1
    i=i+1
print(count)


# for i in d:
#     for x in d[i]:
#         count +=1
# print(count)

# for i,j in d.items():
#     s =s+len(j)
# print(s)

