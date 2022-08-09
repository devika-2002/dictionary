# Q54.
#  Write a Python program to create a key-value list pairings in a given dictionary. 
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]


# dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# e={}
# for i in dict:
#     # print(e[i])
#     # print(dict[i][0])
#     e[i]=dict[i][0]
# print([e])

dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
convert_list=list(dict)
emti_dict={}
i=0
while i<len(convert_list):
    emti_dict[convert_list[i]]=dict[convert_list[i]][0]
    i=i+1
print(emti_dict)
