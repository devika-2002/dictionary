# 51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
#O/P:- {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

                        # for_loop
# dict ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in dict:
#     x=dict[i]
#     j=0
#     b=[]
#     while j<len(x):
#         if x[j]%2==0:
#             b.append(x[j])
#         j=j+1
#     dict[i]=b
# print(dict) 


                        # while_loop
dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
convert_list=list(dict)
emti_dict={}
i=0
while i<len(convert_list):
    list=dict[convert_list[i]]
    j=0
    emti_list=[]
    while j<len(list):
        if list[j]%2==0:
            emti_list.append(list[j])
        j=j+1
    emti_dict[convert_list[i]]=emti_list
    i=i+1
print(emti_dict)
