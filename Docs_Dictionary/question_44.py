# Q44.Write a Python program to split a given dictionary of lists into list of 
# dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
#  {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

# def list_of_dicts(marks):
#     keys = marks.keys()
#     vals = zip(*[marks[k] for k in keys])
#     result = [dict(zip(keys, v)) for v in vals]
#     return result
# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# print(list_of_dicts(marks))

# dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# convert_list=list(dict)
# emti_list=[]
# i=0
# while i<len(convert_list):
#     # print(convert_list[i])
#     dict1={}
#     a=dict[convert_list[i]]
#     j=0
#     emti_list=[]
#     while j<len(a):
#         # dict1[convert_list[i]]=a[j]
#         d=[convert_list[i]]
#         emti_list.append(dict1)
#         # emti_list.append(dict1)
        
#         # dict1[convert_list[i]]=a[j]
#         # print(dict1)
#         j=j+1
#     i=i+1
# print(emti_list)
# # print(dict1)


dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
convert_list=list(dict)
emti_list=[]
i=0
# dict1={}
while i<len(convert_list):
    dict1={}
    a=dict[convert_list[i]]
    j=0
    emti_list=[]
    while j<len(a):
        # print(a[j])
        # dict1[convert_list[i]]=a[0]
        
        emti_list.append(dict1)
        # print(emti_list)
        j=j+1
    i=i+1
print(emti_list)  

